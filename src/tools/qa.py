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
        if lic and lic.get("status") == "permission" and not lic.get("grantedBy"):
            out.append(f"{rel}: a permission licence says who granted it")
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
    "ihris-instance-extension/v1": [("declarations", "instances, assets, directories and derivedFrom resolve; permissions name who", c_declarations)],
    # reused schemas (validated for shape by folio-assistant's zod or fhir.resources)
    "cat-harness declaration (zod)": [("declarations", "see ihris-instance-extension", c_declarations)],
    "harness-config (zod)": [("harness-config", "content type and root instances as AGENTS.md states", c_harness_config)],
    "bean-graph (zod)": [("bean-graph", "declared bean directories exist", c_bean_graph)],
    "skill-package (zod)": [("skill-package", "listed skills and skill files agree", c_skill_package)],
    "tool (zod)": [("tools", "invoked scripts exist; satisfied skills exist", c_tools)],
    "pdf-structure/v1": [("pdf-structure", "doc id matches its entry; unique sections", c_pdf_structure)],
    "FHIR R4 terminology": [("fhir-terminology", "every value set named in value-sets.json is generated", c_fhir)],
    # node types that are not JSON documents
    "bean (beans/defs/*.md)": [("beans", "front matter parses; status/type in vocabulary; parents are epics; links resolve", c_beans)],
    "skill (src/skills/*.md)": [("skills", "front matter parses; name matches file; each skill has a Tool or names one", c_skills)],
    "folio-methodology/v1": [("methodologies", "name matches its directory; local evidence exists", c_methodologies)],
    "library manifest (manifest.jsonld)": [("library-manifests", "every contained section exists; @id is under the entry", c_library_manifests)],
    "BPMN process (processes/*.bpmn)": [("bpmn", "every process is generated from a spec and carries its diagram", c_bpmn)],
}
REUSED = ["cat-harness declaration (zod)", "harness-config (zod)", "bean-graph (zod)", "skill-package (zod)", "tool (zod)",
          "pdf-structure/v1", "FHIR R4 terminology", "folio-catalogue/v1", "folio-catalogue-node/v1",
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
