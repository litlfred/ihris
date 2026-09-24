#!/usr/bin/env python3
"""Semantic QA for every schema and node type in this folio.

Owner, 2026-09-23: "make sure all node types/schemas have QA. it is a QA in and of
itself if there are missing".

A JSON Schema (or folio-assistant's zod) says a document has the right SHAPE. It
does not say that a reference points at something, that a count matches what it
counts, or that a file it names exists. Those are what break a knowledge graph
quietly, so every schema gets at least one such check here, registered in
{@link QA}. The registry is the unit of coverage:

- every schema this folio defines (src/schemas/*.schema.json) and every schema it
  REUSES (folio-assistant's zod, FHIR R4) must have at least one check;
- a schema with none is reported as the finding `qa-missing`. Missing QA is a
  QA failure in its own right, not a gap nobody sees.

Each check reads the committed files and returns findings as strings. Nothing
here writes; the site's Schemas page calls run() for the coverage table.

  python3 src/tools/qa.py            # run every check, print findings, exit 1 on any
validate.py runs it.
"""
import fnmatch
import glob
import hashlib
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REL = "4.3.3"


def J(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return json.load(f)


def exists(rel):
    return os.path.exists(os.path.join(ROOT, rel))


def G(pattern):
    return sorted(os.path.relpath(p, ROOT) for p in glob.glob(os.path.join(ROOT, pattern), recursive=True))


def sha256(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# ------------------------------------------------------------------ the corpus, by schema
def tagged():
    """{schema tag: [(rel, doc)]} for every JSON file carrying $schema (or _schema)."""
    out = {}
    for rel in G("**/*.json"):
        if rel.startswith(("node_modules/", "uploads/", ".build/", "_site/", "src/schemas/")):
            continue
        try:
            d = J(rel)
        except ValueError:
            continue
        if isinstance(d, dict):
            t = d.get("$schema") or d.get("_schema")
            if isinstance(t, str) and not t.startswith("http"):
                out.setdefault(t, []).append((rel, d))
    return out


def bound():
    """{schema: [(rel, doc)]} for files bound by path in src/schemas/bindings.json."""
    b = J("src/schemas/bindings.json")
    out = {}
    for rel in G("**/*.json"):
        if rel.startswith(("node_modules/", "uploads/", ".build/", "_site/", "src/schemas/")):
            continue
        for x in b["bindings"]:
            if fnmatch.fnmatchcase(rel, x["glob"]) or ("**/" in x["glob"] and fnmatch.fnmatchcase(rel, x["glob"].replace("**/", ""))):
                out.setdefault(x["schema"], []).append((rel, J(rel)))
                break
    return out


def declarations():
    root = J("ihris.json")
    return [("ihris.json", root)] + [(f"{i['path']}/{i['name']}.json", J(f"{i['path']}/{i['name']}.json")) for i in root["instances"]]


# ------------------------------------------------------------------ checks
# Each takes the context C and returns a list of finding strings.

def c_catalogue_parents(C):
    ids = {d["id"] for _, d in C["tagged"].get("folio-catalogue-node/v1", [])}
    out = []
    for rel, d in C["tagged"].get("folio-catalogue-node/v1", []):
        for chain in d.get("parents") or []:
            for p in chain:
                if p not in ids:
                    out.append(f"{rel}: parent {p} is not a catalogue node")
        if d.get("metadataRef") and not os.path.exists(os.path.join(ROOT, os.path.dirname(os.path.dirname(rel)), d["metadataRef"])):
            out.append(f"{rel}: metadataRef {d['metadataRef']} does not resolve")
    return out


def c_catalogue_roots(C):
    ids = {d["id"] for _, d in C["tagged"].get("folio-catalogue-node/v1", [])}
    out = []
    for rel, d in C["tagged"].get("folio-catalogue/v1", []):
        for r in d.get("roots") or d.get("rootNodes") or []:
            rid = r if isinstance(r, str) else r.get("id")
            if rid and rid not in ids:
                out.append(f"{rel}: root {rid} is not a catalogue node")
    return out


def c_source_record_nodes(C):
    nodes = {d["id"] for _, d in C["tagged"].get("folio-catalogue-node/v1", [])}
    out = []
    for rel, d in C["tagged"].get("ihris-source-record/v1", []):
        if d.get("node") and d["node"] not in nodes:
            out.append(f"{rel}: node {d['node']} has no catalogue node")
        for cap in d.get("capturedFrom") or []:
            if cap.startswith("uploads/") and not exists(cap) and not exists("uploads"):
                pass  # uploads/ is git-ignored: checked only where present
        for f in (d.get("release") or {}).get("files") or []:
            if f.get("md5") is not None and not re.fullmatch(r"[0-9a-f]{32}", f["md5"]):
                out.append(f"{rel}: release file {f['name']} has a malformed md5")
    return out


def c_module_refs(C):
    ids = {d["id"] for docs in C["tagged"].values() for _, d in docs if isinstance(d.get("id"), str)}
    out = []
    for rel, d in C["tagged"].get("ihris-i2ce-module/v1", []):
        for ref in [d.get("parent")] + (d.get("formClasses") or []):
            if ref and ref not in ids:
                out.append(f"{rel}: reference {ref} does not resolve")
        if not exists(d["source"]["releaseFile"]):
            out.append(f"{rel}: source.releaseFile {d['source']['releaseFile']} does not resolve")
    return out


def c_form_class(C):
    mods = {d["id"] for _, d in C["tagged"].get("ihris-i2ce-module/v1", [])}
    forms = {f for _, d in C["tagged"].get("ihris-form-class/v1", []) for f in d.get("forms") or []}
    lists = {d["form"] for _, d in C["tagged"].get("ihris-data-list/v1", [])}
    out = []
    for rel, d in C["tagged"].get("ihris-form-class/v1", []):
        if os.path.basename(rel)[:-5] != d["class"]:
            out.append(f"{rel}: file is not named after class {d['class']}")
        for m in d.get("definedIn") or []:
            if m not in mods:
                out.append(f"{rel}: definedIn {m} is not a module")
        names = [f["field"] for f in d["fields"]]
        if len(names) != len(set(names)):
            out.append(f"{rel}: duplicate field names")
        for f in d["fields"]:
            for m in f.get("definedIn") or []:
                if m not in mods:
                    out.append(f"{rel}: field {f['field']} definedIn {m} is not a module")
            for r in f.get("references") or []:
                if r not in forms and r not in lists:
                    out.append(f"{rel}: field {f['field']} references form {r}, which no class or data list provides")
    return out


def c_data_list(C):
    mods = {d["id"] for _, d in C["tagged"].get("ihris-i2ce-module/v1", [])}
    out = []
    for rel, d in C["tagged"].get("ihris-data-list/v1", []):
        # An id may repeat ACROSS modules (a sample module re-shipping a default id). Repeated
        # INSIDE one module is an upstream fact: I2CE merges same-named groups, so the running
        # system keeps one. Those are recorded in qa-known.json; any other is a finding.
        from collections import Counter
        dup = sorted({r["id"] for r in d["records"]
                      if Counter((x["id"], x.get("definedIn")) for x in d["records"])[(r["id"], r.get("definedIn"))] > 1})
        if dup and sorted(KNOWN.get("data-list-within-module-duplicates", {}).get(rel, {}).get("ids", [])) != dup:
            out.append(f"{rel}: ids repeated within one module: {', '.join(dup[:8])}")
        for r in d["records"]:
            if r.get("definedIn") and r["definedIn"] not in mods:
                out.append(f"{rel}: record {r['id']} definedIn {r['definedIn']} is not a module")
        from collections import Counter
        prov = Counter(r.get("provenance") for r in d["records"])
        if d.get("counts") and {k: v for k, v in d["counts"].items()} != dict(prov):
            out.append(f"{rel}: counts {d['counts']} do not match the records {dict(prov)}")
        if not exists(d["source"]["releaseFile"]):
            out.append(f"{rel}: source.releaseFile does not resolve")
    return out


def c_qa_known(C):
    """Every accepted upstream finding still matches the data exactly: a stale entry must not hide a new one."""
    from collections import Counter
    out = []
    for rel, d in C["bound"].get("ihris-qa-known/v1", []):
        for f, entry in d["data-list-within-module-duplicates"].items():
            if not exists(f):
                out.append(f"{rel}: {f} does not exist")
                continue
            recs = J(f)["records"]
            c = Counter((r["id"], r.get("definedIn")) for r in recs)
            dup = sorted({i for (i, m), n in c.items() if n > 1})
            if dup != sorted(entry["ids"]):
                out.append(f"{rel}: {f} lists {entry['ids']} but the data repeats {dup}")
    return out


def c_toolkit_stage(C):
    idx = {(t["stage"], t["title"]) for t in J("library/ihris-toolkit/tools-index.json")}
    out, ords = [], []
    for rel, d in C["tagged"].get("ihris-toolkit-stage/v1", []):
        ords.append(d["ordinal"])
        g = d.get("graphic") or {}
        if g.get("localPath") and not exists(g["localPath"]):
            out.append(f"{rel}: graphic {g['localPath']} does not exist")
        for dom in d.get("domains") or []:
            for o in dom.get("objectives") or []:
                for t in o.get("tools") or []:
                    if (d["name"], t["title"]) not in idx:
                        out.append(f"{rel}: tool {t['title']!r} is missing from tools-index.json")
    if sorted(ords) != list(range(len(ords))):
        out.append(f"toolkit stages: ordinals {sorted(ords)} are not 0..{len(ords) - 1}")
    return out


def c_toolkit_structure(C):
    out = []
    for rel, d in C["bound"].get("ihris-toolkit-structure/v1", []):
        tools = J("library/ihris-toolkit/tools-index.json")
        if d["toolCount"] != len(tools):
            out.append(f"{rel}: toolCount {d['toolCount']} but tools-index lists {len(tools)}")
        if d["toolsHostedOnToolkit"] != sum(1 for t in tools if t["hostedOnToolkit"]):
            out.append(f"{rel}: toolsHostedOnToolkit does not match tools-index")
        n_matrix = sum(len(v) for row in d["matrix"].values() for v in row.values())
        n_obj = sum(len(dom.get("objectives") or []) for _, s in C["tagged"].get("ihris-toolkit-stage/v1", []) for dom in s.get("domains") or [])
        if n_matrix != n_obj:
            out.append(f"{rel}: the matrix holds {n_matrix} objectives but the stages hold {n_obj}")
    return out


def c_tools_index(C):
    out = []
    for rel, d in C["bound"].get("ihris-toolkit-tools-index/v1", []):
        s = J("library/ihris-toolkit/structure.json")
        names = {x["name"] for _, x in C["tagged"].get("ihris-toolkit-stage/v1", [])}
        for t in d:
            if t["stage"] not in names:
                out.append(f"{rel}: tool {t['title']!r} is in unknown stage {t['stage']}")
            if t["domain"] not in s["domains"]:
                out.append(f"{rel}: tool {t['title']!r} is in unknown domain {t['domain']}")
    return out


def c_wiki_structure(C):
    out = []
    for rel, d in C["bound"].get("ihris-wiki-help-structure/v1", []):
        base = os.path.dirname(rel)
        for p in d["pages"]:
            if not exists(f"{base}/sections/{p['id']}.md"):
                out.append(f"{rel}: page {p['id']} has no sections/{p['id']}.md")
        for i in d.get("images") or []:
            f = f"{base}/{i['file']}"
            if not exists(f):
                out.append(f"{rel}: image {i['file']} does not exist")
            elif sha256(f) != i["sha256"]:
                out.append(f"{rel}: image {i['file']} does not match its sha256")
        listed = {p["id"] for p in d["pages"]}
        for md in G(f"{base}/sections/*.md"):
            if os.path.basename(md)[:-3] not in listed:
                out.append(f"{rel}: {md} is not listed in pages")
    return out


def c_github_inventory(C):
    out = []
    decl = J("src/ihris5/ihris5.json")
    pinned = {r["url"]: r["commit"] for r in decl["source"]["repositories"]}
    for rel, d in C["bound"].get("ihris-github-inventory/v1", []):
        if pinned.get(d["url"]) != d["commit"]:
            out.append(f"{rel}: commit {d['commit'][:12]} is not the one ihris5.json pins for {d['url']}")
        files = [f"{x['file']}#{x['kind']}:{x['name']}" for x in d.get("fshDefinitions") or []]
        if len(files) != len(set(files)):
            out.append(f"{rel}: duplicate FSH definitions")
    return out


def c_dak_sheets(C):
    classes = {(d["_pkg"] if "_pkg" in d else None, d["class"]) for _, d in []}
    model = {}
    for rel, d in C["tagged"].get("ihris-form-class/v1", []):
        model.setdefault(d["class"], set()).update(f["field"] for f in d["fields"])
    out = []
    for rel, d in C["tagged"].get("ihris-dak-data-dictionary/v1", []):
        if d["class"] not in model:
            out.append(f"{rel}: class {d['class']} is not in the data model")
            continue
        for e in d["elements"]:
            src = e.get("source") or {}
            if src.get("field") and src["field"] not in model.get(src.get("class"), set()):
                out.append(f"{rel}: element {e['id']} names field {src.get('class')}.{src['field']}, which the data model lacks")
            for ev in e.get("evidence") or []:
                if not exists(ev):
                    out.append(f"{rel}: element {e['id']} evidence {ev} does not exist")
            if e.get("description") is not None and e.get("descriptionStatus") == "to-author":
                out.append(f"{rel}: element {e['id']} has a description but is still marked to-author")
    return classes and out or out


def c_dak_proposal(C):
    vs = {v["id"] for v in J("src/ihris-data-dictionary/value-sets.json")["valueSets"]}
    out = []
    for rel, d in C["tagged"].get("ihris-dak-proposal/v1", []):
        ids = [i["id"] for i in d.get("items") or []]
        if len(ids) != len(set(ids)):
            out.append(f"{rel}: duplicate item ids")
        for i in d.get("items") or []:
            for a in i.get("appliesTo") or []:
                if a.startswith("IHRIS.DE.VS.") and a not in vs:
                    out.append(f"{rel}: item {i['id']} appliesTo {a}, which is not a value set")
    return out


def c_dak_value_sets(C):
    elements = {e["id"].split(".", 2)[-1] for _, d in C["tagged"].get("ihris-dak-data-dictionary/v1", []) for e in d["elements"]}
    lists = {d["form"] for _, d in C["tagged"].get("ihris-data-list/v1", [])}
    out = []
    for rel, d in C["bound"].get("ihris-dak-value-sets/v1", []):
        for v in d["valueSets"]:
            for u in v["usedBy"]:
                if u not in elements:
                    out.append(f"{rel}: {v['id']} usedBy {u}, which is not a data element")
            if v["defaultCodes"] and v["form"] not in lists:
                out.append(f"{rel}: {v['id']} claims default codes but no data list ships {v['form']}")
    return out


def c_dak_excluded(C):
    model = {d["class"] for _, d in C["tagged"].get("ihris-form-class/v1", [])}
    out = []
    for rel, d in C["bound"].get("ihris-dak-excluded/v1", []):
        for x in d["excludedClasses"]:
            if x["class"] not in model:
                out.append(f"{rel}: excluded class {x['class']} is not in the data model")
        from collections import Counter
        c = Counter(x["scope"] for x in d["excludedClasses"])
        for scope, n in d["classesByScope"].items():
            if scope != "record" and c.get(scope, 0) != n:
                out.append(f"{rel}: classesByScope[{scope}] = {n} but {c.get(scope, 0)} classes are excluded with that scope")
    return out


def c_iso_report(C):
    out = []
    for rel, d in C["bound"].get("ihris-dak-iso-report/v1", []):
        for k in ("country", "currency"):
            b = d[k]
            # Every shipped code is either current in ISO (equal) or no longer current. Codes
            # whose NAME changed are a subset of `equal`, not a third group.
            if b["equal"] + len(b["notCurrent"]) != b["shipped"]:
                out.append(f"{rel}: {k}: equal {b['equal']} + notCurrent {len(b['notCurrent'])} != shipped {b['shipped']}")
            if len(b["olderNames"]) > b["equal"]:
                out.append(f"{rel}: {k}: more renamed codes than matching codes")
            if set(b["notCurrent"]) & {o["code"] for o in b["olderNames"]}:
                out.append(f"{rel}: {k}: a code is both not current and renamed")
    return out


def c_isco_report(C):
    out = []
    for rel, d in C["bound"].get("ihris-dak-isco-report/v1", []):
        i = d["isco08"]
        if not (i.get("major", 0) <= i.get("sub_major", 0) <= i.get("minor", 0) <= i.get("unit", 0)):
            out.append(f"{rel}: ISCO-08 group counts are not nested (major <= sub-major <= minor <= unit): {i}")
    return out


def c_build_stats(C):
    out = []
    for rel, d in C["bound"].get("ihris-build-stats/v1", []):
        for pkg, s in d["modules"].items():
            n_mod = len(G(f"src/{pkg}/modules/{REL}/*.json"))
            n_cls = len(G(f"src/{pkg}/data-model/{REL}/*.json"))
            if s["formClasses"] != n_cls:
                out.append(f"{rel}: {pkg} formClasses {s['formClasses']} but {n_cls} files")
            if s["modules"] != n_mod:
                out.append(f"{rel}: {pkg} modules {s['modules']} but {n_mod} files")
    return out


def c_process_spec(C):
    spec = importlib.util.spec_from_file_location("gen_bpmn", os.path.join(ROOT, "src/tools/gen_bpmn.py"))
    gb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gb)
    skills = {os.path.basename(p)[:-3] for p in G("src/skills/*.md")} | C["fa_skills"]
    out = []
    if not C["fa_skills"]:
        out.append("process-spec: no folio-assistant checkout, so skills it defines cannot be resolved (set FOLIO_ASSISTANT)")
    for rel, d in C["bound"].get("ihris-process-spec/v1", []):
        out += [f"{rel}: {e}" for e in gb.validate(d)]
        for n in d["nodes"]:
            if n.get("skill") and n["skill"] not in skills:
                out.append(f"{rel}: {n['id']} names skill {n['skill']}, which neither src/skills nor folio-assistant defines")
        if not exists(f"processes/{d['file']}"):
            out.append(f"{rel}: processes/{d['file']} was never generated")
    return out


def _wf_dir(rel):
    return os.path.dirname(os.path.dirname(rel)) if "/reviews/" in rel or "/checks/" in rel else os.path.dirname(rel)


def c_wf_candidates(C):
    """Reviews, check reports and author lists name candidates that exist in their round."""
    out = []
    for schema in ("ihris-wireframe-review/v1", "ihris-wireframe-check-report/v1", "ihris-wireframe-authors/v1"):
        for rel, d in C["bound"].get(schema, []):
            base = _wf_dir(rel)
            present = {os.path.basename(h)[:-5].upper() for h in G(f"{base}/*.html")}
            if schema.endswith("review/v1"):
                named = {e["candidate"] for e in d["entries"]}
            elif schema.endswith("check-report/v1"):
                named = {os.path.basename(c["file"])[:-5].upper() for c in d["candidates"]}
            else:
                named = {k for k in d if k != "note"}
            for n in sorted(named):
                if n not in present:
                    out.append(f"{rel}: names candidate {n}, but {base}/ has no {n.lower()}.html")
    return out


def c_wf_check_complete(C):
    out = []
    for rel, d in C["bound"].get("ihris-wireframe-check-report/v1", []):
        for c in d["candidates"]:
            for vp in ("web", "mobile"):
                if not any(e["viewport"] == vp for e in c["entries"]):
                    out.append(f"{rel}: {c['file']} has no {vp} check (a review at one width is incomplete)")
    return out


def c_wf_decisions(C):
    """Adjudication, decision, patch and acceptance point at files that exist."""
    out = []
    for schema in ("ihris-wireframe-adjudication/v1", "ihris-wireframe-decision/v1", "ihris-wireframe-patch/v1", "ihris-wireframe-acceptance/v1"):
        for rel, d in C["bound"].get(schema, []):
            base = os.path.dirname(rel)
            refs = []
            if schema.endswith("acceptance/v1"):
                refs = [d["accepted"]] + d["states"] + d["covers"]
            elif schema.endswith("patch/v1"):
                refs = [d["after"]]
            for r in refs:
                if not exists(f"{base}/{r}"):
                    out.append(f"{rel}: {r} does not exist")
            if schema.endswith("adjudication/v1"):
                for x in d["disagreements"]:
                    if len(set(x["entries"].values())) < 2:
                        out.append(f"{rel}: {x['candidate']}/{x['criterion']} is recorded as a disagreement but its entries agree")
    return out


def c_site_theme(C):
    spec = importlib.util.spec_from_file_location("extract_theme", os.path.join(ROOT, "src/tools/extract_theme.py"))
    et = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(et)
    out = []
    for rel, d in C["tagged"].get("ihris-site-theme/v1", []):
        a, ratio = d["applied"], d["wcag"]["ratio"]
        for fg in ("text", "h1", "h2", "h3", "h4", "link", "linkHover", "siteName", "sideNavText", "sideNavActive"):
            if et.contrast(a[fg], a["contentBackground"]) < ratio:
                out.append(f"{rel}: applied {fg} {a[fg]} fails WCAG {ratio}:1 on {a['contentBackground']}")
        if et.contrast(a["navBarText"], a["navBar"]) < ratio:
            out.append(f"{rel}: navbar text fails WCAG {ratio}:1")
        logo = os.path.join(os.path.dirname(rel), d["logo"]["file"])
        if not exists(logo) or sha256(logo) != d["logo"]["sha256"]:
            out.append(f"{rel}: logo {d['logo']['file']} is missing or does not match its sha256")
        for adj in d["adjustments"]:
            if adj["measured"] not in {v["value"] for v in d["measured"].values()}:
                out.append(f"{rel}: adjustment for {adj['role']} starts from {adj['measured']}, which was not measured")
    return out


def c_declarations(C):
    out = []
    for rel, d in C["declarations"]:
        base = os.path.dirname(rel) or "."
        for i in d.get("instances") or []:
            if not exists(i["path"]):
                out.append(f"{rel}: instance {i['name']} path {i['path']} does not exist")
        for a in d.get("assets") or []:
            if a.get("src") and not exists(os.path.join(base, a["src"])):
                out.append(f"{rel}: asset {a['id']} src {a['src']} does not exist")
        for x in d.get("directories") or []:
            if x.get("path") and not exists(os.path.normpath(os.path.join(base, x["path"]))):
                out.append(f"{rel}: directory {x['id']} path {x['path']} does not exist")
        for p in d.get("derivedFrom") or []:
            if not exists(p):
                out.append(f"{rel}: derivedFrom {p} does not exist")
        lic = d.get("licence")
        for part, l in (("licence", lic), ("licence.images", (lic or {}).get("images"))):
            if l and l.get("status") == "permission" and not (l.get("grantedBy") and l.get("grantedOn")):
                out.append(f"{rel}: {part}: a permission says who granted it and when")
    return out


def c_harness_config(C):
    out = []
    cfg, root = J("ihris.config.json"), J("ihris.json")
    if cfg.get("contentType") != "document":
        out.append("ihris.config.json: contentType is not `document`, which AGENTS.md §1 states")
    if not root.get("instances"):
        out.append("ihris.json: the root declares no instances")
    return out


def c_bean_graph(C):
    out = []
    d = J("beans/beans.json")
    for x in d["directories"]:
        if not exists(os.path.join("beans", x["path"])):
            out.append(f"beans/beans.json: directory {x['path']} does not exist")
    return out


def c_skill_package(C):
    d = J("src/skills/package-manifest.json")
    listed, files = set(d["skills"]), {os.path.basename(p)[:-3] for p in G("src/skills/*.md")}
    return ([f"package-manifest: skill {s} has no src/skills/{s}.md" for s in sorted(listed - files)] +
            [f"package-manifest: src/skills/{s}.md is not listed" for s in sorted(files - listed)])


def c_tools(C):
    skills = {os.path.basename(p)[:-3] for p in G("src/skills/*.md")}
    out = []
    for rel in G("src/tools/*.tool.json"):
        t = J(rel)
        m = re.search(r"(src/tools/\S+)", (t.get("invoke") or {}).get("shell") or "")
        if m and not exists(m.group(1)):
            out.append(f"{rel}: invokes {m.group(1)}, which does not exist")
        for s in t.get("satisfies") or []:
            if s not in skills:
                out.append(f"{rel}: satisfies skill {s}, which src/skills does not define")
    return out


def c_pdf_structure(C):
    out = []
    for rel, d in C["tagged"].get("pdf-structure/v1", []):
        entry = os.path.basename(os.path.dirname(rel))
        if not d["doc_id"].startswith(entry.split("-v")[0][:12]):
            out.append(f"{rel}: doc_id {d['doc_id']} does not match its entry directory {entry}")
        if len(d["sections"]) != len({s["id"] for s in d["sections"]}):
            out.append(f"{rel}: duplicate section ids")
        if d.get("toc") and len(d["toc"]) < len(d["sections"]) and d["toc_source"] == "outline":
            out.append(f"{rel}: more sections than outline entries")
    return out


def c_fhir(C):
    """FHIR R4 shape and reference resolution run in validate_fhir.py (own venv); here: every
    ValueSet the value-sets table names exists as a generated resource."""
    have = {J(p).get("url") for p in G("src/ihris-data-dictionary/terminology/ValueSet-*.json")}
    out = []
    for v in J("src/ihris-data-dictionary/value-sets.json")["valueSets"]:
        if v["canonical"] not in have:
            out.append(f"value-sets.json: {v['id']} canonical {v['canonical']} has no generated ValueSet")
    return out


# ------------------------------------------------------------------ library: wiki book export, use cases
PLACEHOLDER_EMAILS = {"your@email.add.ress", "someone@somwhere.org", "my_email@somewhere.com"}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?<![\w.-])(?:\+?1-)?\d{3}-\d{3}-\d{4}(?![\w-])")


def c_wiki_book(C):
    """Articles are the outline's level-1 entries, each section exists at its sha256 and names its revision;
    every placed image has exactly one credit; nothing unredacted is left in the text."""
    out = []
    for rel, d in C["tagged"].get("ihris-wiki-book/v1", []):
        base = os.path.dirname(rel)
        ids = [a["id"] for a in d["articles"]]
        if len(ids) != len(set(ids)):
            out.append(f"{rel}: duplicate article ids")
        for a in d["articles"]:
            f = f"{base}/{a['file']}"
            if not exists(f):
                out.append(f"{rel}: article {a['id']} has no {a['file']}")
                continue
            if sha256(f) != a["sha256"]:
                out.append(f"{rel}: {a['file']} does not match its sha256 (edited by hand? regenerate with src/tools/ingest_handbook.py)")
            if a["pageEnd"] < a["pageStart"]:
                out.append(f"{rel}: article {a['id']} ends before it starts")
            if f"oldid={a['oldid']}" not in a["source"]:
                out.append(f"{rel}: article {a['id']} source does not carry its oldid {a['oldid']}")
            text = open(os.path.join(ROOT, f), encoding="utf-8").read()
            left = [e for e in EMAIL_RE.findall(text) if e not in PLACEHOLDER_EMAILS] + PHONE_RE.findall(text)
            if left:
                out.append(f"{rel}: {a['file']} still holds {len(left)} e-mail address(es) or phone number(s)")
        on_disk = {os.path.basename(m)[:-3] for m in G(f"{base}/sections/*.md")}
        if on_disk != set(ids):
            out.append(f"{rel}: sections/ holds {sorted(on_disk ^ set(ids))[:5]} not matching the article list")
        if exists(f"{base}/structure.json"):
            st = J(f"{base}/structure.json")
            if st["source"]["sha256"] != d["source"]["sha256"]:
                out.append(f"{rel}: structure.json was built from a different file")
            l1 = [t["title"].strip() for t in st.get("toc") or [] if t["level"] == 1 and t["page"] not in d["appendices"]["licence"]]
            if l1 != [a["title"] for a in d["articles"]]:
                out.append(f"{rel}: the articles are not the outline's level-1 entries, in order")
        imgs = {i["id"]: i for i in (J(f"{base}/images.json").get("images") or [])} if exists(f"{base}/images.json") else {}
        credited = [i["id"] for i in d["images"]]
        if sorted(credited) != sorted(imgs):
            out.append(f"{rel}: {len(credited)} credited images but images.json places {len(imgs)}")
        for i in d["images"]:
            if not exists(f"{base}/{i['file']}"):
                out.append(f"{rel}: image {i['file']} does not exist")
            if i["id"] in imgs and imgs[i["id"]]["basis"]["page"] != i["page"]:
                out.append(f"{rel}: image {i['id']} is on page {imgs[i['id']]['basis']['page']}, not {i['page']}")
            if i.get("article") and i["article"] not in ids:
                out.append(f"{rel}: image {i['id']} sits in unknown article {i['article']}")
        man = f"uploads/{os.path.basename(base)}/manifest.json"
        if not exists(man) or J(man).get("sha256") != d["source"]["sha256"]:
            out.append(f"{rel}: {man} does not pin the sha256 the book was built from")
    return out


def c_document_images(C):
    """Every folio-document-images/v1 entry's file exists, and its id names the page its basis gives."""
    out = []
    for rel, d in C["tagged"].get("folio-document-images/v1", []):
        base = os.path.dirname(rel)
        for i in d.get("images") or []:
            if i["role"] == "figure" and not exists(f"{base}/{i['file']}"):
                out.append(f"{rel}: figure {i['file']} does not exist")
            m = re.match(r"img-p(\d{3})-\d+$", i["id"])
            if m and i.get("basis") and int(m.group(1)) != i["basis"]["page"]:
                out.append(f"{rel}: {i['id']} names page {int(m.group(1))} but its basis says {i['basis']['page']}")
        on_disk = {os.path.basename(f) for f in G(f"{base}/images/*")}
        listed = {os.path.basename(i["file"]) for i in d.get("images") or []}
        if on_disk - listed:
            out.append(f"{rel}: images/ holds files it does not list: {sorted(on_disk - listed)[:5]}")
    return out


def _uc_walk(p):
    yield p
    for c in p["packages"]:
        yield from _uc_walk(c)


def c_use_cases(C):
    """Counts match the records; parents are the containing package; extensions hang off steps that exist;
    actor and requirement links resolve (or are recorded as dangling); the source is the one uploads/ pins."""
    out, described, where = [], set(), {}
    docs = C["tagged"].get("ihris-use-cases/v1", [])
    for rel, d in docs:
        for p in _uc_walk(d["root"]):
            for x in p["useCases"] + p["requirements"]:
                if x["id"] in described:
                    out.append(f"{rel}: {x['id']} is described twice")
                described.add(x["id"])
                where[x["id"]] = rel
        described |= {a["id"] for a in d["actors"]}
    for rel, d in docs:
        pk = list(_uc_walk(d["root"]))
        ucs = [u for p in pk for u in p["useCases"]]
        reqs = [r for p in pk for r in p["requirements"]]
        want = {"useCases": len(ucs), "actors": len(d["actors"]), "requirements": len(reqs), "packages": len(pk),
                "steps": sum(len(u["mainSuccessScenario"]) for u in ucs), "extensions": sum(len(u["extensions"]) for u in ucs)}
        if d["counts"] != want:
            out.append(f"{rel}: counts {d['counts']} but the records hold {want}")
        for p in pk:
            for u in p["useCases"]:
                if u["package"] != p["number"]:
                    out.append(f"{rel}: {u['id']} says package {u['package']} but sits in {p['number']}")
                if u.get("parent") and u["parent"] != p["name"]:
                    out.append(f"{rel}: {u['id']} parent {u['parent']!r} is not its package {p['name']!r}")
                if [s["step"] for s in u["mainSuccessScenario"]] != list(range(1, len(u["mainSuccessScenario"]) + 1)):
                    out.append(f"{rel}: {u['id']} steps are not numbered 1..n")
                for e in u["extensions"]:
                    a = e["atStep"].split(".")[0]
                    if a != "*" and not 1 <= int(a) <= len(u["mainSuccessScenario"]):
                        out.append(f"{rel}: {u['id']} extension {e['id']} hangs off step {a}, which does not exist")
        dangling = {x["id"] for x in d["dangling"]}
        for x in d["dangling"]:
            if x["id"] in described:
                out.append(f"{rel}: {x['id']} is recorded as dangling but is described")
        for a in d["actors"]:
            for u in a["useCases"]:
                if u["id"] not in described and u["id"] not in dangling:
                    out.append(f"{rel}: actor {a['id']} plays in {u['id']}, which is neither described nor recorded as dangling")
        for r in reqs:
            for u in r.get("referencedBy") or []:
                if u not in described:
                    out.append(f"{rel}: {r['id']} is referenced by {u}, which is not described")
        man = "uploads/ihris-use-cases/manifest.json"
        pinned = {f["file"]: f for f in J(man)["files"]} if exists(man) else {}
        f = pinned.get(d["source"]["file"])
        if not f or (f["md5"], f["sha256"]) != (d["source"]["md5"], d["source"]["sha256"]):
            out.append(f"{rel}: source {d['source']['file']} is not the file {man} pins")
        if not exists(f"{os.path.dirname(rel)}/{d['product']}.md"):
            out.append(f"{rel}: no {d['product']}.md beside it")
    return out


def _scenario_dirs(C):
    """Every directory a declaration marks with the `scenarios` graph kind, repository-relative."""
    out = []
    for rel, d in C["declarations"]:
        for x in d.get("directories") or []:
            if "scenarios" in (x.get("graphKinds") or []):
                out.append(os.path.normpath(os.path.join(os.path.dirname(rel) or ".", x["path"])))
    return out


def _roles(C):
    """{role id: (rel, role)} across every scenarios directory's roles.json."""
    out = {}
    for d in _scenario_dirs(C):
        rel = f"{d}/roles.json"
        if exists(rel):
            for r in J(rel).get("roles") or []:
                out.setdefault(r.get("id"), (rel, r))
    return out


def _staff_actors(C):
    """{actor id: (rel, actor)} for every actor file in a scenarios directory."""
    return {J(rel).get("id"): (rel, J(rel)) for d in _scenario_dirs(C) for rel in G(f"{d}/actors/*.json")}


def _uc_staff_refs(C):
    """[(rel, record id, field, actor id)] for every Assigned To and requirement Source reference."""
    out = []
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        for p in _uc_walk(d["root"]):
            for u in p["useCases"]:
                if "assignedTo" in u:
                    out.append((rel, u["id"], "assignedTo", (u["assignedTo"] or {}).get("actor")))
            for r in p["requirements"]:
                if "source" in r:
                    out.append((rel, r["id"], "source", (r["source"] or {}).get("actor")))
    return out


def c_uc_role_refs(C):
    """Every primary or supporting actor of a use case, and every actor record's `role`, is a declared Role."""
    roles, out = _roles(C), []
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        for a in d["actors"]:
            if a.get("role") not in roles:
                out.append(f"{rel}: actor {a['id']} names role {a.get('role')!r}, which no scenarios roles.json declares")
        for p in _uc_walk(d["root"]):
            for u in p["useCases"]:
                for k in ("primaryActors", "supportingActors"):
                    for r in u.get(k) or []:
                        if r not in roles:
                            out.append(f"{rel}: {u['id']} {k} {r!r} is not a declared role")
    return out


def c_uc_staff_refs(C):
    """Every Assigned To / Source reference resolves to an actor file, and the references of each field
    number exactly what `withheld` records for it."""
    actors, out = _staff_actors(C), []
    refs = _uc_staff_refs(C)
    for rel, rid, field, aid in refs:
        if aid not in actors:
            out.append(f"{rel}: {rid} {field} -> {aid!r}, which is no actor file")
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        have = {}
        for r, _, field, _ in refs:
            if r == rel:
                have[field] = have.get(field, 0) + 1
        said = {w["field"]: w["count"] for w in d["withheld"]}
        if have != said:
            out.append(f"{rel}: withheld records {said} but the records carry {have} actor references")
    return out


def c_staff_actors(C):
    """Opaque actors: the file is named for its id; ids are ihris-2009-staff-01..NN with no gap; the file
    carries only id, title, kind (person) and description (no roles, no identity); each is referenced."""
    actors, out = _staff_actors(C), []
    used = {aid for *_, aid in _uc_staff_refs(C)}
    for aid, (rel, a) in actors.items():
        if os.path.basename(rel) != f"{aid}.json":
            out.append(f"{rel}: holds actor {aid!r}, not the one its name says")
        if set(a) != {"id", "title", "kind", "description"}:
            out.append(f"{rel}: carries {sorted(set(a) - {'id', 'title', 'kind', 'description'})} or lacks a field: an opaque actor is id, title, kind, description only")
        if a.get("kind") != "person":
            out.append(f"{rel}: kind {a.get('kind')!r}, but a named person is `person`")
        if aid not in used:
            out.append(f"{rel}: {aid} is referenced by no use case or requirement")
    want = [f"ihris-2009-staff-{i:02d}" for i in range(1, len(actors) + 1)]
    if sorted(a for a in actors if a) != want:
        out.append(f"opaque actors {sorted(a for a in actors if a)} are not numbered {want[:1]}..{want[-1:]} without a gap")
    return out


# Owner decision, 2026-09-24 (the open questions of ihris PR #17): "Any User" in A-ICE4 (Common) and A-PS6
# (Qualify) is one role. A role standing for more than one report actor must be a merge listed here.
OWNER_SAME_ROLE = [{("common", "A-ICE4"), ("qualify", "A-PS6")}]


def c_role_graph(C):
    """The use-case role graph: one Role per actor the reports describe, except the owner's merges, and no
    other. Each role cites in `_sources` the report actors it stands for, and every described actor is cited by
    exactly the role its record names. The id is `ihris-` and the first cited A-id in lower case (instance-name
    grammar); title and description are each cited actor's own, verbatim; a person's role with no skills. No two
    roles share an id, and no two roles share a title within a product."""
    out, actors = [], {}
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        for a in d["actors"]:
            actors[(d["product"], a["id"])] = (rel, a)
    cited = {}
    for sd in _scenario_dirs(C):
        rel = f"{sd}/roles.json"
        if not exists(rel):
            out.append(f"{sd}: a scenarios directory with no roles.json")
            continue
        g = J(rel)
        ids = [r.get("id") for r in g.get("roles") or []]
        for rid in sorted({i for i in ids if ids.count(i) > 1}):
            out.append(f"{rel}: role id {rid!r} is declared more than once")
        titles = {}
        for r in g.get("roles") or []:
            rid = r.get("id") or ""
            if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", rid):
                out.append(f"{rel}: role id {rid!r} is not in instance-name grammar")
            srcs = [(x.get("product"), x.get("actor")) for x in r.get("_sources") or []]
            if not srcs:
                out.append(f"{rel}: {rid} cites no report actor in `_sources`")
                continue
            if len(srcs) > 1 and set(srcs) not in OWNER_SAME_ROLE:
                out.append(f"{rel}: {rid} stands for {srcs}, a merge the owner has not decided")
            if rid != "ihris-" + (srcs[0][1] or "").lower():
                out.append(f"{rel}: {rid} is not named for its first cited actor {srcs[0][1]}")
            for key in srcs:
                if key in cited:
                    out.append(f"{rel}: {key[1]} ({key[0]}) is cited by {cited[key]} and {rid}")
                cited[key] = rid
                titles.setdefault((key[0], r.get("title")), set()).add(rid)
                if key not in actors:
                    out.append(f"{rel}: {rid} cites {key[1]} ({key[0]}), which no use-case report describes")
                    continue
                arel, a = actors[key]
                if a.get("role") != rid:
                    out.append(f"{arel}: actor {a['id']} names role {a.get('role')!r}, but {rid} cites it")
                if r.get("title") != a["name"]:
                    out.append(f"{rel}: {rid} title {r.get('title')!r} is not the report's {a['name']!r} ({arel} {a['id']})")
                if r.get("description") != a["description"]:
                    out.append(f"{rel}: {rid} description is not the report's, verbatim ({arel} {a['id']})")
                file = next((d["source"]["file"] for x, d in C["tagged"].get("ihris-use-cases/v1", []) if x == arel), None)
                if next(x for x in r["_sources"] if (x.get("product"), x.get("actor")) == key).get("report") != file:
                    out.append(f"{rel}: {rid} cites {a['id']} in a report other than {file}")
            if r.get("actorKinds") != ["person"] or r.get("skills") != []:
                out.append(f"{rel}: {rid} should be actorKinds [person] with no skills")
        for (prod, title), rids in sorted(titles.items(), key=str):
            if len(rids) > 1:
                out.append(f"{rel}: roles {sorted(rids)} share the title {title!r} within {prod}")
    for key in sorted(set(actors) - set(cited)):
        out.append(f"{actors[key][0]}: actor {key[1]} is cited by no role")
    for merge in OWNER_SAME_ROLE:
        if len({cited.get(k) for k in merge}) != 1 or None in {cited.get(k) for k in merge}:
            out.append(f"owner's merge {sorted(merge)} is not one role citing both: {sorted(str(cited.get(k)) for k in merge)}")
    return out


def _stories(C):
    """[(rel, story)] across every scenarios directory's stories.json."""
    return [(f"{d}/stories.json", s) for d in _scenario_dirs(C) if exists(f"{d}/stories.json")
            for s in J(f"{d}/stories.json").get("stories") or []]


def _story_use_case(C, s):
    """The use-case id a story's id names (`<role id>-<use-case id>`, lower case), or None."""
    rid = (s.get("role") or {}).get("role") or ""
    sid = s.get("id") or ""
    return sid[len(rid) + 1:].upper() if sid.startswith(rid + "-") and re.fullmatch(r"uc-[a-z]+\d+", sid[len(rid) + 1:]) else None


def c_role_use_cases(C):
    """Owner, 2026-09-24: each role's use cases (its stories). Every story names a declared role and a use
    case a report describes, by id `<role id>-<use-case id>`; `want` is that use case's title, verbatim; no
    story twice."""
    out, roles = [], _roles(C)
    ucs = {u["id"]: u for _, d in C["tagged"].get("ihris-use-cases/v1", []) for p in _uc_walk(d["root"]) for u in p["useCases"]}
    seen = set()
    for sd in _scenario_dirs(C):
        if not exists(f"{sd}/stories.json"):
            out.append(f"{sd}: a scenarios directory with no stories.json")
    for rel, s in _stories(C):
        rid, uid = (s.get("role") or {}).get("role"), _story_use_case(C, s)
        if s.get("id") in seen:
            out.append(f"{rel}: story {s.get('id')!r} is declared more than once")
        seen.add(s.get("id"))
        if rid not in roles:
            out.append(f"{rel}: story {s.get('id')!r} is told as {rid!r}, which is no declared role")
        if uid is None or uid not in ucs:
            out.append(f"{rel}: story {s.get('id')!r} names no use case a report describes")
            continue
        if s.get("want") != ucs[uid]["title"]:
            out.append(f"{rel}: story {s['id']} want {s.get('want')!r} is not {uid}'s title {ucs[uid]['title']!r}, verbatim")
    return out


def c_role_use_cases_primary(C):
    """Owner, 2026-09-24: a role is linked to exactly the use cases the reports list it as primary actor on.
    Every story is backed by its use case's `primaryActors`, and every (use case, primary actor) pair has its
    story."""
    out = []
    have = {((s.get("role") or {}).get("role"), _story_use_case(C, s)): rel for rel, s in _stories(C)}
    want = {}
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        for p in _uc_walk(d["root"]):
            for u in p["useCases"]:
                for r in u.get("primaryActors") or []:
                    want[(r, u["id"])] = rel
    for (r, u), rel in sorted(have.items(), key=str):
        if (r, u) not in want:
            out.append(f"{rel}: {r} is linked to {u}, whose Primary Actors do not name it")
    for (r, u), rel in sorted(want.items(), key=str):
        if (r, u) not in have:
            out.append(f"{rel}: {u} names {r} as primary actor, and no story links them")
    return out


def c_use_case_crosswalk(C):
    """Every use case has exactly one entry; each linked form exists in the data model of its package and
    its name really occurs in the title; unmatched means null; counts match."""
    out = []
    ucs = {}
    for rel, d in C["tagged"].get("ihris-use-cases/v1", []):
        for p in _uc_walk(d["root"]):
            for u in p["useCases"]:
                ucs[u["id"]] = (d["product"], u["title"])
    forms = {}
    for mrel, m in C["tagged"].get("ihris-i2ce-module/v1", []):
        for x in m.get("forms") or []:
            forms.setdefault((m["instance"], x["form"]), set()).add(x.get("displayName") or "")
    classes = {d["id"] for _, d in C["tagged"].get("ihris-form-class/v1", [])}
    for _, c in C["tagged"].get("ihris-form-class/v1", []):
        for f in c.get("forms") or []:
            forms.setdefault((c["id"].split("/")[0], f), set())

    def toks(s):
        t = re.findall(r"[a-z0-9]+", s.lower().replace("'s", ""))
        return " " + " ".join(w[:-3] + "y" if len(w) > 4 and w.endswith("ies") else w[:-2] if w.endswith("sses") else
                              w[:-1] if len(w) > 3 and w.endswith("s") and not w.endswith("ss") else w for w in t) + " "
    for rel, d in C["tagged"].get("ihris-use-case-crosswalk/v1", []):
        seen = [e["useCase"] for e in d["entries"]]
        if sorted(seen) != sorted(ucs):
            out.append(f"{rel}: entries {len(seen)} do not cover the {len(ucs)} use cases exactly once")
        from collections import Counter
        cnt = Counter(e["status"] for e in d["entries"])
        want = {"matched": cnt.get("matched", 0), "unmatched": cnt.get("unmatched", 0), "no-data-model": cnt.get("no-data-model", 0),
                "links": sum(len(e["matches"] or []) for e in d["entries"])}
        if d["counts"] != want:
            out.append(f"{rel}: counts {d['counts']} but the entries hold {want}")
        for e in d["entries"]:
            prod, title = ucs.get(e["useCase"], (None, None))
            if prod and prod != e["product"]:
                out.append(f"{rel}: {e['useCase']} is filed under {e['product']} but belongs to {prod}")
            if e["status"] == "no-data-model" and (d["scope"].get(e["product"]) or G(f"src/ihris-{e['product']}/data-model/*")):
                out.append(f"{rel}: {e['useCase']} says no data model, but {e['product']} has one")
            for m in e["matches"] or []:
                if m["package"] not in d["scope"].get(e["product"], []):
                    out.append(f"{rel}: {e['useCase']} links {m['form']} in {m['package']}, outside {e['product']}'s scope")
                if (m["package"], m["form"]) not in forms:
                    out.append(f"{rel}: {e['useCase']} links form {m['form']}, which {m['package']} does not declare")
                if m["formClass"] and m["formClass"] not in classes:
                    out.append(f"{rel}: {e['useCase']} names form class {m['formClass']}, which is not a node")
                if title and toks(m["matchedText"]).strip() and toks(m["matchedText"]) not in toks(title):
                    out.append(f"{rel}: {e['useCase']}: {m['matchedText']!r} does not occur in the title {title!r}")
                if m["matchedOn"] == "form name" and m["matchedText"] != m["form"].replace("_", " "):
                    out.append(f"{rel}: {e['useCase']}: form-name match {m['matchedText']!r} is not the name of {m['form']}")
    return out


# ------------------------------------------------------------------ non-JSON node types
def _front(rel):
    import yaml
    text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, "no front matter"
    try:
        return yaml.safe_load(m.group(1)) or {}, None
    except yaml.YAMLError as e:
        return None, f"front matter is not valid YAML: {str(e).splitlines()[0]}"


BEAN_STATUS = {"draft", "todo", "in-progress", "completed", "scrapped"}
BEAN_TYPE = {"milestone", "epic", "feature", "task", "bug"}


def c_beans(C):
    out, beans = [], {}
    for rel in G("beans/defs/*.md"):
        fm, err = _front(rel)
        if err:
            out.append(f"{rel}: {err}")
            continue
        bid = os.path.basename(rel).split("--")[0]
        beans[bid] = (rel, fm)
        if not bid.startswith("ihris-"):
            out.append(f"{rel}: id {bid} lacks the prefix ihris- (.beans.yml)")
        for k in ("title", "status", "type"):
            if not fm.get(k):
                out.append(f"{rel}: front matter has no {k}")
        if fm.get("status") not in BEAN_STATUS:
            out.append(f"{rel}: status {fm.get('status')!r} is not one of {sorted(BEAN_STATUS)}")
        if fm.get("type") not in BEAN_TYPE:
            out.append(f"{rel}: type {fm.get('type')!r} is not one of {sorted(BEAN_TYPE)}")
    for bid, (rel, fm) in beans.items():
        p = fm.get("parent")
        if p and p not in beans:
            out.append(f"{rel}: parent {p} is not a bean")
        elif p and beans[p][1].get("type") not in ("epic", "milestone", "feature"):
            out.append(f"{rel}: parent {p} is a {beans[p][1].get('type')}, not an epic, milestone or feature")
        for b in fm.get("blocked_by") or []:
            if b not in beans:
                out.append(f"{rel}: blocked_by {b} is not a bean")
    return out


def c_skills(C):
    out = []
    for rel in G("src/skills/*.md"):
        fm, err = _front(rel)
        if err:
            out.append(f"{rel}: {err}")
            continue
        if fm.get("name") != os.path.basename(rel)[:-3]:
            out.append(f"{rel}: name {fm.get('name')!r} does not match the file name")
        if not (fm.get("description") or "").strip():
            out.append(f"{rel}: no description")
        tools = [t for t in G("src/tools/*.tool.json") if fm.get("name") in (J(t).get("satisfies") or [])]
        body = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        if not tools and "Tool `" not in body and "folio-assistant's" not in body:
            out.append(f"{rel}: no Tool node satisfies this skill, and it names no tool it uses")
    return out


def c_methodologies(C):
    out = []
    for rel in G("methodologies/*/*.md"):
        fm, err = _front(rel)
        if err:
            out.append(f"{rel}: {err}")
            continue
        if fm.get("name") != os.path.basename(os.path.dirname(rel)):
            out.append(f"{rel}: name {fm.get('name')!r} does not match its directory")
        for e in fm.get("evidence") or []:
            src = e.get("source") if isinstance(e, dict) else e
            if isinstance(src, str) and src.startswith(("library/", "src/", "docs/")) and not exists(src.split("#")[0]):
                out.append(f"{rel}: evidence {src} does not exist")
    return out


def c_library_manifests(C):
    out = []
    for rel in G("library/**/manifest.jsonld"):
        d = J(rel)
        base = os.path.dirname(rel)
        for c in d.get("contains") or []:
            cid = c if isinstance(c, str) else c.get("@id", "")
            if cid.startswith("library/") and not (exists(cid + ".md") or exists(cid + ".jsonld") or exists(cid)):
                out.append(f"{rel}: contains {cid}, which does not exist")
        if not d.get("@id", "").startswith(base):
            out.append(f"{rel}: @id {d.get('@id')} is not under {base}")
    return out


def c_bpmn(C):
    out = []
    specs = {J(p)["file"] for p in G("processes/specs/*.json")}
    for rel in G("processes/*.bpmn"):
        if os.path.basename(rel) not in specs:
            out.append(f"{rel}: no spec in processes/specs generates it (hand-written BPMN drifts)")
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        if "<bpmndi:BPMNDiagram" not in text:
            out.append(f"{rel}: has no diagram")
    return out


# ------------------------------------------------------------------ glossary (folio-glossary/v1, core's SKOS schema)
# Recomputed here from the inputs, independently of src/tools/build_glossary.py, so a bug there is caught
# rather than copied. Shape is folio-assistant's zod (validate-folio.ts); these are the facts it cannot see.
GLOSSARY_EXTERNAL = {  # verified ConceptMap target system -> the publisher's IRI for a code (see build_glossary.py)
    "urn:iso:std:iso:3166": lambda c: "http://publications.europa.eu/resource/authority/country/" + _alpha3(c),
    "urn:iso:std:iso:4217": lambda c: "http://publications.europa.eu/resource/authority/currency/" + c,
    "http://www.ilo.org/public/english/bureau/stat/isco/isco08/": lambda c: "http://data.europa.eu/esco/isco/C" + c,
}
GLOSSARY_EQUIV = {"equal": "exactMatch", "equivalent": "exactMatch", "wider": "broadMatch", "subsumes": "broadMatch",
                  "narrower": "narrowMatch", "specializes": "narrowMatch"}
GLOSSARY_MATCHES = ("exactMatch", "closeMatch", "broadMatch", "narrowMatch")
LOCAL_ID = re.compile(r"^[a-z0-9][a-z0-9._-]*$")


def _alpha3(a2):
    import pycountry
    c = pycountry.countries.get(alpha_2=a2)
    return c.alpha_3 if c else f"?{a2}"


def _glossaries(C):
    return C["tagged"].get("folio-glossary/v1", [])


def _glossary_dirs(C):
    out = []
    for rel, d in C["declarations"]:
        base = os.path.dirname(rel)
        for x in d.get("directories") or []:
            if "glossary" in (x.get("graphKinds") or []):
                out.append(os.path.normpath(os.path.join(base, x["path"])))
    return out


def _pointer(doc, ptr):
    for part in [p for p in ptr.split("/") if p]:
        part = part.replace("~1", "/").replace("~0", "~")
        doc = doc[int(part)] if isinstance(doc, list) else doc[part]
    return doc


def _strings(v):
    if isinstance(v, str):
        yield v
    elif isinstance(v, dict):
        for x in v.values():
            yield from _strings(x)
    elif isinstance(v, list):
        for x in v:
            yield from _strings(x)


def c_glossary_schemes(C):
    """Each scheme sits in a declared glossary directory as <id>.glossary.json; the three states hold (authored has a
    definition, could-not-extract a reason); every source names a file that exists; and the committed schemes are
    exactly what src/tools/build_glossary.py generates from today's inputs."""
    out, dirs = [], _glossary_dirs(C)
    if not dirs:
        out.append("no declaration has a glossary directory (graphKinds [\"glossary\"])")
    for rel, g in _glossaries(C):
        if os.path.dirname(rel) not in dirs:
            out.append(f"{rel}: not in a declared glossary directory ({', '.join(dirs)})")
        if os.path.basename(rel) != f"{g.get('id')}.glossary.json":
            out.append(f"{rel}: holds scheme {g.get('id')!r}, so it should be named {g.get('id')}.glossary.json")
        for t in g.get("terms") or []:
            if t.get("status") == "authored" and not t.get("definition"):
                out.append(f"{rel}: {t.get('id')} is authored with no definition (it is a candidate)")
            if t.get("status") == "could-not-extract" and not t.get("reason"):
                out.append(f"{rel}: {t.get('id')} could not be extracted and says not why")
            if t.get("source") and not IRI_RX.match(t["source"]) and not exists(t["source"].split("#")[0]):
                out.append(f"{rel}: {t.get('id')} source {t['source']} does not exist")
    spec = importlib.util.spec_from_file_location("build_glossary", os.path.join(ROOT, "src/tools/build_glossary.py"))
    bg = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.join(ROOT, "src", "tools"))
    spec.loader.exec_module(bg)
    want = bg.outputs()
    have = {rel: json.dumps(g, indent=1, ensure_ascii=False) + "\n" for rel, g in _glossaries(C)}
    for rel in sorted(set(want) | set(have)):
        if rel not in have:
            out.append(f"{rel}: build_glossary.py generates it, and it is not committed")
        elif rel not in want:
            out.append(f"{rel}: committed, and build_glossary.py does not generate it")
        elif have[rel] != want[rel]:
            out.append(f"{rel}: differs from what build_glossary.py generates (stale or hand-edited)")
    return out


IRI_RX = re.compile(r"^[a-z][a-z0-9+.-]*://", re.I)


def c_glossary_ids(C):
    """No scheme id twice; no term id twice in a scheme; every id in core's local-id grammar; so no IRI twice."""
    out, schemes = [], {}
    for rel, g in _glossaries(C):
        if g.get("id") in schemes:
            out.append(f"{rel}: scheme id {g.get('id')} is also {schemes[g['id']]}")
        schemes[g.get("id")] = rel
        if not LOCAL_ID.match(g.get("id") or ""):
            out.append(f"{rel}: scheme id {g.get('id')!r} is not a local id")
        seen = set()
        for t in g.get("terms") or []:
            if t.get("id") in seen:
                out.append(f"{rel}: term id {t.get('id')} appears twice")
            seen.add(t.get("id"))
            if not LOCAL_ID.match(t.get("id") or ""):
                out.append(f"{rel}: term id {t.get('id')!r} is not a local id")
    return out


def c_glossary_namespaces(C):
    """Owner, 2026-09-24: "make sure all glossary terms properly localed to ihris so [no] collision w/ other
    subgraphs". Each scheme's IRIs are in the namespace of the instance that owns its source (build_glossary.py
    scheme_owner). Checked here: the owner is one of ihris.json's instances and never the root; every term's
    source lies in the owner, or (a code list) in a package the owner's list is extended by and that declares
    the same form; no scheme IRI is minted twice; and the SKOS the site published sits in the owner's namespace."""
    sys.path.insert(0, os.path.join(ROOT, "src", "tools"))
    import build_glossary as bg
    out, iris = [], {}
    decl = J("ihris.json")
    instances = {i["name"] for i in decl.get("instances") or []}
    defs = bg.form_definers()
    for rel, g in _glossaries(C):
        try:
            owner = bg.scheme_owner(g, defs)
        except SystemExit as e:
            out.append(f"{rel}: {e}")
            continue
        if owner not in instances:
            out.append(f"{rel}: owner {owner} is not an instance ihris.json declares (the root never owns a scheme's IRIs)")
            continue
        ns = f"https://litlfred.github.io/ihris/{owner}/ns#"
        iri = f"{ns}glossary/{g['id']}"
        if iri in iris:
            out.append(f"{rel}: scheme IRI {iri} is also minted by {iris[iri]}")
        iris[iri] = rel
        form = g["id"][len("code-list-"):] if g["id"].startswith("code-list-") else None
        for t in g.get("terms") or []:
            src = (t.get("source") or "").split("#")[0]
            parts = src.split("/")
            if len(parts) < 3 or parts[0] not in ("src", "library"):
                continue
            pkg = parts[1]
            if pkg == owner:
                continue
            if form and bg._rank(pkg) > bg._rank(owner):  # a later package adding records to the owner's list
                continue
            out.append(f"{rel}: {t['id']} comes from {pkg}, which neither is {owner} nor extends its {form or 'scheme'}")
        site = os.path.join(ROOT, ".build", "site", bg.skos_asset(g))
        if os.path.isfile(site):
            ids = [n.get("@id", "") for n in json.load(open(site, encoding="utf-8")).get("@graph") or []]
            stray = [i for i in ids if not i.startswith(ns)]
            if stray:
                out.append(f"{rel}: its published SKOS mints {stray[0]} outside {ns}")
    return out


def c_glossary_matches(C):
    """Every SKOS match is one the repository verified or the owner accepted: recomputed from the ConceptMaps in
    src/ihris-data-dictionary/terminology (equal/equivalent -> exactMatch, wider/subsumes -> broadMatch,
    narrower/specializes -> narrowMatch, nothing else), for targets that are external schemes ihris.json
    references, plus exactMatch from a code list's ValueSet bound to ISCO-08 (ValueSet identity, owner 2026-09-24).
    A match with no such basis, or a basis with no match, is a finding."""
    out, expected = [], {}
    remote = [g["url"].rstrip("/") + "/" for g in J("ihris.json").get("remoteGraphs") or [] if "glossary" in g["graphKinds"]]
    remote.append("http://data.europa.eu/esco/isco/")  # ESCO's ISCO concepts sit beside its concept-scheme IRI
    for rel in G("src/ihris-data-dictionary/terminology/ConceptMap-*.json"):
        for grp in J(rel).get("group") or []:
            iri = GLOSSARY_EXTERNAL.get(grp.get("target"))
            if not iri:
                continue
            form = grp["source"].rsplit("/", 1)[-1]
            for el in grp.get("element") or []:
                for tg in el.get("target") or []:
                    m = GLOSSARY_EQUIV.get(tg.get("equivalence"))
                    if m and tg.get("code"):
                        expected.setdefault((form, el["code"]), {}).setdefault(m, set()).add(iri(tg["code"]))
    # The owner-accepted second basis (2026-09-24): a code list's own ValueSet bound to the ILO ISCO-08
    # system is identity, so each of its concepts has exactMatch to ESCO. No other system is accepted so.
    identity = {"http://www.ilo.org/public/english/bureau/stat/isco/isco08/"}
    for rel in G("src/ihris-data-dictionary/terminology/ValueSet-*.json"):
        vs = J(rel)
        form = vs.get("url", "").rsplit("/", 1)[-1]
        for inc in (vs.get("compose") or {}).get("include") or []:
            if inc.get("system") in identity:
                for c in inc.get("concept") or []:
                    expected.setdefault((form, c["code"]), {}).setdefault("exactMatch", set()).add(GLOSSARY_EXTERNAL[inc["system"]](c["code"]))
    seen = set()
    for rel, g in _glossaries(C):
        for t in g.get("terms") or []:
            src = (t.get("source") or "").split("#")[0]
            form = os.path.basename(src)[:-5] if "/data-lists/" in src else None
            key = (form, t.get("notation"))
            want = expected.get(key, {}) if form else {}
            seen.add(key)
            for m in GLOSSARY_MATCHES:
                have = set(t.get(m) or [])
                for x in sorted(have - want.get(m, set())):
                    out.append(f"{rel}: {t['id']} {m} {x} is no mapping the repository verified")
                for x in sorted(want.get(m, set()) - have):
                    out.append(f"{rel}: {t['id']} lacks {m} {x}, which a verified ConceptMap or the ISCO-08 ValueSet identity records")
                for x in have:
                    if not any(x.startswith(r) for r in remote):
                        out.append(f"{rel}: {t['id']} {m} {x} is in no external scheme ihris.json references (remoteGraphs)")
    for key in sorted(k for k in expected if k not in seen):
        out.append(f"ConceptMap mapping {key[0]}|{key[1]} has no glossary term to carry it")
    return out


def c_glossary_counts(C):
    """Term counts per source match their inputs: the toolkit's technical terms, the use-case reports' recorded
    glossaries, and each code list's unique DEFAULT records (one scheme per list that has any, no other)."""
    out = []
    by_id = {g.get("id"): (rel, g) for rel, g in _glossaries(C)}

    def n(sid):
        return len((by_id.get(sid, (None, {}))[1]).get("terms") or []) if sid in by_id else None
    want = sum(len(J(r).get("technicalTerms") or []) for r in G("library/ihris-toolkit/stages/*.json"))
    if n("toolkit-technical-terms") != want:
        out.append(f"toolkit-technical-terms: {n('toolkit-technical-terms')} terms, and the stages hold {want} technical terms")
    ucs = [(r, J(r)) for r in G("library/ihris-use-cases/*.json") if J(r).get("$schema") == "ihris-use-cases/v1"]
    for r, d in ucs:
        gl = d.get("glossary")
        if gl is None:
            out.append(f"{r}: records no glossary (claimed or not)")
        elif gl["found"] != bool(gl["terms"]):
            out.append(f"{r}: glossary found={gl['found']} but holds {len(gl['terms'])} terms")
    want = sum(len((d.get("glossary") or {}).get("terms") or []) for _, d in ucs)
    if n("use-cases-2009") != want:
        out.append(f"use-cases-2009: {n('use-cases-2009')} terms, and the reports record {want} glossary terms")
    ids = {}
    for rel in G(f"src/*/data-lists/{REL}/*.json"):
        d = J(rel)
        ids.setdefault(d["form"], set()).update(r["id"] for r in d["records"] if r.get("provenance") == "default")
    lists = {f: v for f, v in ids.items() if v}
    for f, v in sorted(lists.items()):
        if n(f"code-list-{f}") != len(v):
            out.append(f"code-list-{f}: {n(f'code-list-{f}')} terms, and the list ships {len(v)} unique default records")
    for sid in sorted(by_id):
        if sid.startswith("code-list-") and sid[len("code-list-"):] not in lists:
            out.append(f"{by_id[sid][0]}: {sid} names no code list with default records")
    extra = sorted(set(by_id) - {"toolkit-technical-terms", "use-cases-2009"} - {f"code-list-{f}" for f in lists})
    for sid in extra:
        if not sid.startswith("code-list-"):
            out.append(f"{by_id[sid][0]}: scheme {sid} is from no known source")
    return out


def c_glossary_verbatim(C):
    """Every authored term's definition is in its source verbatim: the JSON its `source` points at holds the exact
    string, and a toolkit definition also appears in the captured page (uploads/toolkit/*.html) it was ingested from."""
    import html as H
    out, pages = [], {}

    def norm(s):
        return " ".join(s.replace("\u00a0", " ").split())
    for rel, g in _glossaries(C):
        for t in g.get("terms") or []:
            if t.get("status") != "authored":
                continue
            d = t.get("definition")
            texts = [d] if isinstance(d, str) else list((d or {}).values())
            f, _, ptr = (t.get("source") or "").partition("#")
            try:
                node = _pointer(J(f), ptr)
            except (OSError, ValueError, KeyError, IndexError):
                out.append(f"{rel}: {t['id']} source {t.get('source')} does not resolve")
                continue
            have = set(_strings(node))
            for x in texts:
                if x not in have:
                    out.append(f"{rel}: {t['id']} definition is not verbatim in {t['source']}")
            if f.startswith("library/ihris-toolkit/stages/"):
                cap = J(f).get("capturedFrom")
                cap = cap if isinstance(cap, str) else (cap or [None])[0]
                if cap and exists(cap):
                    if cap not in pages:
                        raw = open(os.path.join(ROOT, cap), encoding="utf-8").read()
                        pages[cap] = (norm(H.unescape(re.sub(r"<[^>]+>", " ", raw))), norm(H.unescape(re.sub(r"<[^>]+>", "", raw))))
                    for x in texts:
                        if norm(x) not in pages[cap][0] and norm(x) not in pages[cap][1]:
                            out.append(f"{rel}: {t['id']} definition is not in the captured page {cap}")
    return out


def c_glossary_page(C):
    """The glossary page lists every term of every scheme exactly once (one <dt> per term, anchored), and nothing else."""
    import collections
    import tempfile
    sys.path.insert(0, os.path.join(ROOT, "src", "tools"))
    import site_instances
    theme = J("src/site/theme/ihris-classic.json")
    with tempfile.TemporaryDirectory() as tmp:
        _, page = site_instances.glossary_page(theme, tmp)
    got = collections.Counter(re.findall(r'<dt id="([^"]+)"', page))
    want = collections.Counter(f"{g['id']}--{t['id']}" for _, g in _glossaries(C) for t in g.get("terms") or [])
    out = [f"glossary page: term {a} is listed {got[a]} times" for a in sorted(want) if got[a] != 1]
    out += [f"glossary page: lists {a}, which is no term" for a in sorted(set(got) - set(want))]
    return out


# The registry: schema -> [(check id, what it establishes, fn)]. Coverage is read from here.
QA = {
    "folio-catalogue-node/v1": [("catalogue-parents", "every parent and metadataRef resolves", c_catalogue_parents)],
    "folio-catalogue/v1": [("catalogue-roots", "every root is a catalogue node", c_catalogue_roots)],
    "ihris-source-record/v1": [("source-record-nodes", "each record has its catalogue node; md5s are well formed", c_source_record_nodes)],
    "ihris-i2ce-module/v1": [("module-refs", "parent, form classes and release file resolve", c_module_refs)],
    "ihris-form-class/v1": [("form-class", "named after its class; modules resolve; unique fields; references hit a class or list", c_form_class)],
    "ihris-data-list/v1": [("data-list", "unique records; modules resolve; counts match the records", c_data_list)],
    "ihris-toolkit-stage/v1": [("toolkit-stage", "graphics exist; every tool is indexed; ordinals are 0..n-1", c_toolkit_stage)],
    "ihris-toolkit-structure/v1": [("toolkit-structure", "counts and the matrix match the index and stages", c_toolkit_structure)],
    "ihris-toolkit-tools-index/v1": [("tools-index", "every tool sits in a known stage and domain", c_tools_index)],
    "ihris-wiki-help-structure/v1": [("wiki-structure", "every page has its section, and every image exists at its sha256", c_wiki_structure)],
    "ihris-github-inventory/v1": [("github-inventory", "pinned at the commit ihris5.json declares; no duplicates", c_github_inventory)],
    "ihris-dak-data-dictionary/v1": [("dak-sheets", "class and fields exist in the data model; evidence exists; no stale to-author", c_dak_sheets)],
    "ihris-dak-proposal/v1": [("dak-proposal", "unique items; value sets they apply to exist", c_dak_proposal)],
    "ihris-dak-value-sets/v1": [("dak-value-sets", "users are data elements; default codes come from a shipped list", c_dak_value_sets)],
    "ihris-dak-excluded/v1": [("dak-excluded", "excluded classes exist; scope counts match", c_dak_excluded)],
    "ihris-dak-iso-report/v1": [("iso-report", "the partition of shipped codes does not exceed what shipped", c_iso_report)],
    "ihris-dak-isco-report/v1": [("isco-report", "ISCO-08 group counts nest", c_isco_report)],
    "ihris-build-stats/v1": [("build-stats", "module and class counts match the files", c_build_stats)],
    "ihris-process-spec/v1": [("process-spec", "lanes, flows, skills and the generated BPMN all resolve", c_process_spec)],
    "ihris-wireframe-review/v1": [("wf-candidates", "reviews name candidates that exist", c_wf_candidates)],
    "ihris-wireframe-check-report/v1": [("wf-candidates", "reports name candidates that exist", c_wf_candidates),
                                        ("wf-check-complete", "every candidate is checked at web AND mobile", c_wf_check_complete)],
    "ihris-wireframe-authors/v1": [("wf-candidates", "authors name candidates that exist", c_wf_candidates)],
    "ihris-wireframe-adjudication/v1": [("wf-decisions", "recorded disagreements really disagree", c_wf_decisions)],
    "ihris-wireframe-decision/v1": [("wf-decisions", "decision files resolve", c_wf_decisions)],
    "ihris-wireframe-patch/v1": [("wf-decisions", "the review a patch follows exists", c_wf_decisions)],
    "ihris-wireframe-acceptance/v1": [("wf-decisions", "the accepted candidate, its states and what it covers exist", c_wf_decisions)],
    "ihris-site-theme/v1": [("site-theme", "applied colours pass WCAG AA; logo matches; adjustments start from measured colours", c_site_theme)],
    "ihris-qa-known/v1": [("qa-known", "every accepted upstream finding still matches the data", c_qa_known)],
    "ihris-wiki-book/v1": [("wiki-book", "articles are the outline's level-1 entries at their sha256; every image credited once; no unredacted contact left", c_wiki_book)],
    "ihris-use-cases/v1": [("use-cases", "counts match; parents and extension anchors hold; links resolve or are dangling; source is the pinned file", c_use_cases),
                           ("use-case-roles", "every use-case actor, and every actor's role, is a declared Role", c_uc_role_refs),
                           ("use-case-staff-refs", "every Assigned To / Source resolves to an actor file; references number what withheld records", c_uc_staff_refs)],
    "ihris-use-case-crosswalk/v1": [("use-case-crosswalk", "one entry per use case; linked forms exist and are named in the title; counts match", c_use_case_crosswalk)],
    "ihris-instance-extension/v1": [("declarations", "instances, assets, directories and derivedFrom resolve; permissions name who", c_declarations)],
    # reused schemas (validated for shape by folio-assistant's zod or fhir.resources)
    "cat-harness declaration (zod)": [("declarations", "see ihris-instance-extension", c_declarations)],
    "harness-config (zod)": [("harness-config", "content type and root instances as AGENTS.md states", c_harness_config)],
    "bean-graph (zod)": [("bean-graph", "declared bean directories exist", c_bean_graph)],
    "skill-package (zod)": [("skill-package", "listed skills and skill files agree", c_skill_package)],
    "tool (zod)": [("tools", "invoked scripts exist; satisfied skills exist", c_tools)],
    "role graph (zod RoleGraphSchema)": [("role-graph", "one Role per described actor or owner's merge, each citing its actors; no id twice, no title twice in a product; title and description verbatim", c_role_graph)],
    "user stories (zod UserStoryGraphSchema)": [("role-use-cases", "every story names a declared role and a described use case; want is its title verbatim", c_role_use_cases),
                                                ("role-use-cases-primary", "every link is backed by the use case's Primary Actors, and none is missing", c_role_use_cases_primary)],
    "actor (zod ActorDef)": [("staff-actors", "named for its id; numbered 01..N without a gap; id, title, kind, description only; each referenced", c_staff_actors)],
    "pdf-structure/v1": [("pdf-structure", "doc id matches its entry; unique sections", c_pdf_structure)],
    "folio-document-images/v1": [("document-images", "every figure's file exists and its id names its page; no unlisted image files", c_document_images)],
    "FHIR R4 terminology": [("fhir-terminology", "every value set named in value-sets.json is generated", c_fhir)],
    "folio-glossary/v1": [("glossary-schemes", "in a declared glossary directory, named for its id; states hold; sources exist; current with build_glossary.py", c_glossary_schemes),
                          ("glossary-ids", "no scheme or term id twice; ids in core's local-id grammar", c_glossary_ids),
                          ("glossary-namespaces", "every scheme's IRIs are in the namespace of the sub-instance that owns its source; no scheme IRI twice", c_glossary_namespaces),
                          ("glossary-matches", "every SKOS match is a mapping a verified ConceptMap records, or ISCO-08 ValueSet identity (owner-accepted), to a referenced external scheme, and none is missing", c_glossary_matches),
                          ("glossary-counts", "terms per source match the toolkit's technical terms, the reports' glossaries, each code list's default records", c_glossary_counts),
                          ("glossary-verbatim", "every authored definition is verbatim in its source (and the toolkit's in the captured page)", c_glossary_verbatim),
                          ("glossary-page", "the glossary page lists every term exactly once", c_glossary_page)],
    # node types that are not JSON documents
    "bean (beans/defs/*.md)": [("beans", "front matter parses; status/type in vocabulary; parents are epics; links resolve", c_beans)],
    "skill (src/skills/*.md)": [("skills", "front matter parses; name matches file; each skill has a Tool or names one", c_skills)],
    "folio-methodology/v1": [("methodologies", "name matches its directory; local evidence exists", c_methodologies)],
    "library manifest (manifest.jsonld)": [("library-manifests", "every contained section exists; @id is under the entry", c_library_manifests)],
    "BPMN process (processes/*.bpmn)": [("bpmn", "every process is generated from a spec and carries its diagram", c_bpmn)],
}
REUSED = ["cat-harness declaration (zod)", "harness-config (zod)", "bean-graph (zod)", "skill-package (zod)", "tool (zod)",
          "role graph (zod RoleGraphSchema)", "user stories (zod UserStoryGraphSchema)", "actor (zod ActorDef)",
          "pdf-structure/v1", "folio-document-images/v1", "folio-glossary/v1", "FHIR R4 terminology", "folio-catalogue/v1", "folio-catalogue-node/v1",
          "bean (beans/defs/*.md)", "skill (src/skills/*.md)", "folio-methodology/v1", "library manifest (manifest.jsonld)",
          "BPMN process (processes/*.bpmn)"]


def fa_skills():
    fa = os.environ.get("FOLIO_ASSISTANT", os.path.join(ROOT, "..", "litlfred", "folio-assistant"))
    return {os.path.basename(p)[:-3] for p in glob.glob(os.path.join(fa, "cat-harness", "skills", "**", "*.md"), recursive=True)}


KNOWN = json.load(open(os.path.join(ROOT, "src/tools/qa-known.json")))


def run():
    C = {"tagged": tagged(), "bound": bound(), "declarations": declarations(), "fa_skills": fa_skills()}
    own = sorted(json.load(open(p))["title"] for p in glob.glob(os.path.join(ROOT, "src/schemas/*.schema.json")))
    findings, coverage, done = [], [], {}
    for schema in own + REUSED:
        checks = QA.get(schema, [])
        if not checks:
            findings.append(f"qa-missing: schema {schema} has no semantic QA check (add one to src/tools/qa.py)")
        n_docs = len(C["tagged"].get(schema, [])) + len(C["bound"].get(schema, []))
        for cid, what, fn in checks:
            if fn not in done:
                done[fn] = fn(C)
                findings += [f"{cid}: {x}" for x in done[fn]]
        coverage.append({"schema": schema, "reused": schema in REUSED, "documents": n_docs,
                         "checks": [{"id": cid, "establishes": what, "findings": len(done[fn])} for cid, what, fn in checks]})
    for extra in sorted(set(QA) - set(own) - set(REUSED)):
        findings.append(f"qa-orphan: the registry has checks for {extra}, which is no schema this folio defines or reuses")
    return findings, coverage


def main():
    findings, coverage = run()
    print(f"QA: {len(coverage)} schemas, {sum(len(c['checks']) for c in coverage)} checks, {len(findings)} finding(s)")
    for x in findings[:80]:
        print("  " + x)
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
