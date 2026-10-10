#!/usr/bin/env python3
"""F4: map the iHRIS 4 logical models to the three iHRIS 5 IGs, by evidence (bean ihris-7gl8).

  python3 src/tools/map_ihris5.py             # match and write everything (re-indexing first when the pin has moved)
  python3 src/tools/map_ihris5.py --index     # only (re)compile iHRIS 5 from ihris5-source/ and rewrite the element index
  python3 src/tools/map_ihris5.py --check     # fail if the crosswalk, gap report or StructureMap FSH is stale
  python3 src/tools/map_ihris5.py --propose   # add proposal items for what the matcher could not decide (additive)

Design: docs/design/fhir-strategy.md (D6 target: all three iHRIS 5 IGs; D6 format: gamma, StructureMaps). Skill
`ihris-4-on-fhir`, Tool `ihris-map-ihris5`.

1. INDEX. The three iHRIS 5 IGs (iHRIS/iHRIS at the commit src/ihris5/ihris5.json pins, mounted read-only at
   ihris5-source/) are copied to .build/ihris5-sd/<ig>/ and compiled to StructureDefinitions by SUSHI. What compiles is
   read: each profile's and extension's element paths, labels, types and bindings, the extension urls and titles, and
   the Questionnaire items whose `definition` names a profile element. Types SUSHI leaves out of a differential are
   resolved from FHIR R4 core. The result, names and labels only with the sha256 of each compiled file, is committed
   as src/ihris-4-on-fhir/mapping/ihris5-index.json, so CI (which does not mount iHRIS 5) checks against it. SUSHI's
   errors are recorded there. The copies get the declared workspace patches (src/ihris5/ig-build-patches.json: each
   an upstream defect drafted in docs/upstream/ihris5-ig-defects.md), and the index records which were applied.
2. MATCH. Deterministic, and only on equality after normalisation. No synonym table and no judgement:
   - model level, per IG: a logical model's names (its group, title, I2CE class, forms and the forms' display names
     in the module records) equal to a profile's name, id or title, or to those of a complex extension the profile
     carries at its top level; or the element-level majority (most of the model's elements have a label-equal element
     in one profile). One candidate is `exact`, several `ambiguous`, none `none`. An owner-ACCEPTED proposal in
     src/ihris-data-dictionary/authored/ decides a model (`accepted`), and the elements are then matched in it.
   - element level, inside the model's profile: the I2CE field's label equal to an element's label, the label of the
     value of the extension it holds, that extension's title, or the text of a Questionnaire item defined on it.
     `exact`: one candidate, type-compatible. `ambiguous`: several, or type-incompatible. `none`: no candidate.
3. GENERATE. crosswalk.json, gaps.json and gaps.md in src/ihris-4-on-fhir/mapping/, and one StructureMap per
   (logical model, IG) with a model-level match and at least one exact element, as FSH Instances in
   src/ihris-4-on-fhir/input/fsh/maps/. Rules cover only exact (and owner-accepted) element matches. The iHRIS 5
   canonicals are URLs only: they are not an IG dependency (D5, R4 core only).

Nothing here writes a value the sources do not hold (AGENTS.md section 7). --propose writes to authored/ only to ADD
items for the owner, never changing an existing item, and lists only candidates the matcher found (or, cited as
such, the bean's own examples).
"""
import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_fsh  # noqa: E402  element names and FHIR types of the logical models, one definition
import apply_ig_patches  # noqa: E402  the declared workspace patches, one implementation

SRC = os.path.join(ROOT, "ihris5-source")
PATCHES = os.path.join(ROOT, "src", "ihris5", "ig-build-patches.json")
BUILD = os.path.join(ROOT, ".build", "ihris5-sd")
MAPPING = os.path.join(ROOT, "src", "ihris-4-on-fhir", "mapping")
INDEX = os.path.join(MAPPING, "ihris5-index.json")
CROSSWALK = os.path.join(MAPPING, "crosswalk.json")
GAPS = os.path.join(MAPPING, "gaps.json")
GAPS_MD = os.path.join(MAPPING, "gaps.md")
MAPS_FSH = os.path.join(gen_fsh.FSH, "maps")
AUTHORED = os.path.join(ROOT, "src", "ihris-data-dictionary", "authored")
PROPOSAL = os.path.join(AUTHORED, "ihris5-mapping.json")
BEAN = os.path.join(ROOT, "beans", "defs", "ihris-7gl8--map-the-dak-logical-models-to-the-ihris-5-fhir-ig.md")
CANONICAL = "https://litlfred.github.io/ihris/dak"
SUSHI_VERSION = "3.20.1"
TOOL = "src/tools/map_ihris5.py"

# The three IGs (owner, D6 target). The id is this folio's short name for each; path is in iHRIS/iHRIS.
IGS = [("ig", "ig"), ("manage", "ihris-backend/ihris-backend-site/ig"), ("qualify", "ihris-backend/ihris-backend-site/qualify-ig")]

# FHIR R4 types a logical-model element's type may be COPIED into, by the StructureMap `copy` transform (or, for a
# Coding into a CodeableConcept, into its `coding`). A FHIR datatype rule, not a synonym table: anything else is
# type-incompatible, and so `ambiguous`, for the owner.
COMPATIBLE = {
    "date": {"date", "dateTime"}, "string": {"string", "markdown"}, "boolean": {"boolean"},
    "integer": {"integer", "positiveInt", "unsignedInt"}, "Money": {"Money"}, "Identifier": {"Identifier"},
    "Coding": {"Coding", "CodeableConcept"}, "Attachment": {"Attachment"},
}


def rel(p):
    return os.path.relpath(p, ROOT)


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def J(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def dump(d):
    return json.dumps(d, indent=1, ensure_ascii=False) + "\n"


# ------------------------------------------------------------------ 1. the iHRIS 5 index
def pin():
    s = J(os.path.join(ROOT, "src", "ihris5", "ihris5.json"))["source"]
    return s["repository"], s["ref"]


def mounted():
    """The mounted source's HEAD, when ihris5-source/ is mounted at the pinned commit; else None."""
    if not os.path.isdir(os.path.join(SRC, "ig")):
        return None
    r = subprocess.run(["git", "-C", SRC, "rev-parse", "HEAD"], capture_output=True, text=True)
    head = r.stdout.strip()
    if head != pin()[1]:
        raise SystemExit(f"map_ihris5: ihris5-source/ is at {head[:12]}, not the pinned {pin()[1][:12]}; "
                         "remount it (python3 src/tools/mount_sources.py)")
    return head


def r4_core():
    for base in [os.environ.get("FHIR_PACKAGES"), os.path.expanduser("~/.fhir/packages")]:
        p = base and os.path.join(base, "hl7.fhir.r4.core#4.0.1", "package")
        if p and os.path.isdir(p):
            return p
    raise SystemExit("map_ihris5: hl7.fhir.r4.core#4.0.1 is not in the FHIR package cache (SUSHI fetches it)")


_CORE = {}


def core_sd(t):
    if t not in _CORE:
        p = os.path.join(r4_core(), f"StructureDefinition-{t}.json")
        _CORE[t] = J(p) if os.path.exists(p) else None
    return _CORE[t]


def core_types(path):
    """The R4 core type codes of an element path (slice names removed), walking into datatypes as needed."""
    segs = [s.split(":")[0] for s in path.split(".")]
    sd, base = core_sd(segs[0]), [segs[0]]
    i = 1
    types = [segs[0]]
    while i < len(segs) and sd:
        want = ".".join(base + [segs[i]])
        el = next((e for e in sd["snapshot"]["element"] if e["path"] == want), None)
        if el is None:
            return []
        types = [t["code"] for t in el.get("type") or []]
        if el.get("contentReference"):
            return []
        i += 1
        if i < len(segs):
            if len(types) == 1 and types[0][0].isupper() and types[0] not in ("BackboneElement", "Element"):
                sd, base = core_sd(types[0]), [types[0]]
            else:
                base = want.split(".")
    return types


def compile_ig(ig_id, ig_path):
    """Copy one IG's sushi-config.yaml and input/ to .build/ihris5-sd/<id>/ (the backend IGs' `core` symlink resolved
    into the copy), apply the declared build patches (src/ihris5/ig-build-patches.json) to that copy, and build it.
    Returns (errors, warnings, unique error messages, ids of the patches applied). The mounted source is never written."""
    w = os.path.join(BUILD, ig_id)
    if os.path.isdir(w):
        shutil.rmtree(w)
    os.makedirs(w)
    shutil.copy(os.path.join(SRC, ig_path, "sushi-config.yaml"), w)
    shutil.copytree(os.path.join(SRC, ig_path, "input"), os.path.join(w, "input"))
    # Where each copied file came from in the repository, following the symlinks the copy resolved.
    ws_of_repo, src_real = {}, os.path.realpath(SRC)
    for d, _, files in os.walk(os.path.join(SRC, ig_path, "input"), followlinks=True):
        wd = os.path.join(w, os.path.relpath(d, os.path.join(SRC, ig_path)))
        ws_of_repo.setdefault(os.path.relpath(os.path.realpath(d), src_real), wd)
        for f in files:
            ws_of_repo.setdefault(os.path.relpath(os.path.realpath(os.path.join(d, f)), src_real), os.path.join(wd, f))
    applied = apply_ig_patches.apply(J(PATCHES), w, ws_of_repo, source_root=SRC, log=lambda m: None)
    r = subprocess.run(["sushi", "build", w], capture_output=True, text=True)
    text = r.stdout + r.stderr
    open(os.path.join(w, "sushi.log"), "w", encoding="utf-8").write(text)
    m = re.search(r"(\d+) Errors?\s.*?(\d+) Warnings?", text, re.S)
    if not m:
        raise SystemExit(f"map_ihris5: SUSHI did not report a result for {ig_id}:\n{text[-2000:]}")
    msgs = sorted({re.sub(r"\s+", " ", x).strip() for x in re.findall(r"^error\s+(.*)$", text, re.M)})
    return int(m.group(1)), int(m.group(2)), msgs, applied


def index_ig(ig_id, ig_path):
    errors, warnings, msgs, applied = compile_ig(ig_id, ig_path)
    out_dir = os.path.join(BUILD, ig_id, "fsh-generated", "resources")
    cfg = open(os.path.join(SRC, ig_path, "sushi-config.yaml"), encoding="utf-8").read()
    field = lambda k: (re.search(rf"^{k}:\s*(.+)$", cfg, re.M) or [None, None])[1]  # noqa: E731
    structures, questionnaires = [], []
    for p in sorted(glob.glob(os.path.join(out_dir, "StructureDefinition-*.json"))):
        sd = J(p)
        if sd.get("derivation") != "constraint":
            continue
        els = []
        for e in sd.get("differential", {}).get("element", []):
            x = {"id": e["id"]}
            if e.get("label"):
                x["label"] = e["label"]
            types = [t["code"] for t in e.get("type") or []]
            if types:
                x["types"], x["typeFrom"] = types, "differential"
            elif sd["type"] != "Extension" and not re.search(r"(^|\.)extension(:[^.]+)?(\.|$)|\.value\[x\]|\.url$", e["id"]):
                t = core_types(e["id"])
                if t:
                    x["types"], x["typeFrom"] = t, "r4-core"
            prof = [pr for t in e.get("type") or [] for pr in t.get("profile") or []]
            if prof:
                x["profiles"] = prof
            if (e.get("binding") or {}).get("valueSet"):
                x["binding"] = e["binding"]["valueSet"]
            for k in ("min", "max", "fixedUri"):
                if k in e:
                    x[k] = e[k]
            els.append(x)
        structures.append({k: sd.get(k) for k in ("url", "id", "name", "title", "type", "kind", "baseDefinition") if sd.get(k)}
                          | {"file": os.path.basename(p), "sha256": sha256_file(p), "elements": els})
    for p in sorted(glob.glob(os.path.join(out_dir, "Questionnaire-*.json"))):
        q = J(p)
        items = []

        def walk(xs):
            for i in xs:
                if i.get("definition") and "#" in i["definition"] and i.get("text"):
                    items.append({"linkId": i["linkId"], "text": i["text"], "definition": i["definition"]})
                walk(i.get("item") or [])
        walk(q.get("item") or [])
        questionnaires.append({"url": q.get("url"), "title": q.get("title"), "file": os.path.basename(p),
                               "sha256": sha256_file(p), "items": items})
    return {"id": ig_id, "path": ig_path, "title": field("title"), "canonical": field("canonical"),
            "compile": {"errors": errors, "warnings": warnings, "errorMessages": msgs, "patchesApplied": applied},
            "structures": structures, "questionnaires": questionnaires}


def build_index():
    head = mounted()
    if not head:
        raise SystemExit("map_ihris5: ihris5-source/ is not mounted (python3 src/tools/mount_sources.py)")
    repo, ref = pin()
    idx = {"$schema": "ihris-ihris5-element-index/v1",
           "_comment": f"GENERATED by {TOOL} --index. Do not edit. Names, element paths, labels, types and bindings of the "
                       "three iHRIS 5 IGs as SUSHI compiles them, with each compiled file's sha256: what the F4 matcher "
                       "reads, so CI can check the crosswalk without mounting iHRIS 5. No FSH and no definitions are copied.",
           "source": {"repository": repo, "commit": ref, "licence": "LGPL-3.0 (the repository); each IG's sushi-config.yaml declares CC0-1.0",
                      "attribution": "iHRIS 5, (c) IntraHealth International, https://github.com/iHRIS/iHRIS"},
           "sushi": SUSHI_VERSION, "igs": [index_ig(i, p) for i, p in IGS]}
    os.makedirs(MAPPING, exist_ok=True)
    open(INDEX, "w", encoding="utf-8").write(dump(idx))
    for ig in idx["igs"]:
        c = ig["compile"]
        print(f"map_ihris5: {ig['id']}: SUSHI {c['errors']} error(s), {c['warnings']} warning(s); "
              f"{len(ig['structures'])} profiles/extensions, {len(ig['questionnaires'])} Questionnaires")
    return idx


# ------------------------------------------------------------------ 2. the two sides
def norm_label(s):
    """Case, punctuation and spacing only; and 'Date of X' read as 'X Date' (the same words in English's other
    order), recorded on every match it makes."""
    n = " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())
    m = re.fullmatch(r"date of (.+)", n)
    return (m.group(1) + " date", "date-of") if m else (n, None)


def name_key(s, basic=False):
    """A name as a key: the publisher prefix iHRIS / Ihris / ihris- dropped (every iHRIS 4 class and iHRIS 5 profile
    carries it), and on a profile of the FHIR resource Basic the resource name `Basic` the profile names carry; then
    letters and digits only, lower case."""
    s = re.sub(r"(?i)^ihris[_\-\s]*", "", s.strip())
    if basic:
        s = re.sub(r"(?i)^basic[_\-\s]*", "", s)
    return re.sub(r"[^a-z0-9]", "", s.lower())


def form_display_names():
    out = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "src", "*", "modules", "*", "*.json"))):
        d = J(p)
        for f in d.get("forms") or []:
            if f.get("displayName"):
                out.setdefault(f["form"], []).append((f["displayName"], rel(p)))
    return out


def ihris4_models():
    forms = form_display_names()
    out = []
    for p in sorted(glob.glob(os.path.join(gen_fsh.DD, "*.json"))):
        d = J(p)
        names = [("group", d["group"], rel(p)), ("title", d["title"], rel(p)), ("class", d["class"], rel(p))]
        for f in d["forms"]:
            names.append(("form", f, rel(p)))
            names += [("form displayName", n, src) for n, src in forms.get(f, [])]
        els = []
        for e in d["elements"]:
            field = e["id"].rsplit(".", 1)[1]
            labels = []
            for k in ("dataElementLabel", "formDataElementLabel"):
                if e.get(k) and e[k] not in labels:
                    labels.append(e[k])
            els.append({"element": gen_fsh.element_name(field), "field": field, "labels": labels,
                        "type": gen_fsh.I2CE_TYPE[(e.get("source") or {}).get("i2ceType")]})
        out.append({"model": d["group"], "url": d["logicalModel"], "class": d["class"], "file": rel(p),
                    "names": names, "elements": els})
    return out


def ig_targets(ig, all_igs):
    """{profile url: profile}: each profile (a constraint on a resource) of one IG, with its target elements: every
    labelled element, and every element of an extension it carries (a simple extension's value; each part of a complex
    one), each with all its label evidence and its types. Elements inherited from an iHRIS 5 base profile are included."""
    ext = {}
    for g in all_igs:  # an extension is looked up in its own IG first, then the others (the backend IGs use ig/'s)
        for s in g["structures"]:
            if s["type"] == "Extension":
                ext.setdefault(s["url"], (g["id"], s))
    for s in ig["structures"]:
        if s["type"] == "Extension":
            ext[s["url"]] = (ig["id"], s)
    by_url = {s["url"]: s for s in ig["structures"]}
    qitems = {}
    for q in ig["questionnaires"]:
        for it in q["items"]:
            url, _, path = it["definition"].partition("#")
            path = re.sub(r"\.value\[x\]$", "", path)
            qitems.setdefault((url, path), []).append({"source": "questionnaire item text", "value": it["text"],
                                                        "file": q["file"], "path": it["linkId"]})

    def chain(s):
        out, seen = [], set()
        while s and s["url"] not in seen:
            seen.add(s["url"])
            out.insert(0, s)
            s = by_url.get(s.get("baseDefinition"))
        return out

    profiles = {}
    for s in ig["structures"]:
        if s["type"] == "Extension" or s.get("kind") != "resource":
            continue
        T = {}

        def add(eid, label, src, file, path, types=None, typeFrom=None, ext_url=None):
            t = T.setdefault(eid, {"path": eid, "labels": [], "types": [], "typeFrom": None})
            if label and not any(x["value"] == label and x["source"] == src and x["path"] == path for x in t["labels"]):
                t["labels"].append({"source": src, "value": label, "file": file, "path": path})
            if types and not t["types"]:
                t["types"], t["typeFrom"] = types, typeFrom
            if ext_url:
                t["extension"] = ext_url

        top_ext = []
        for layer in chain(s):
            for e in layer["elements"]:
                eid = re.sub(r"\.value\[x\]$", "", e["id"])
                if e.get("profiles") and re.search(r"\.extension:[^.]+$", eid):
                    url = e["profiles"][0]
                    add(eid, e.get("label"), "element label", layer["file"], e["id"], ext_url=url)
                    if url not in ext:
                        continue
                    xig, x = ext[url]
                    if eid.count(".") == 1:
                        top_ext.append((eid, url))
                    for xe in x["elements"]:
                        if xe["id"] == "Extension.value[x]" and xe.get("max") != "0":
                            add(eid, xe.get("label"), "extension value label", x["file"], xe["id"], xe.get("types"), f"extension {x['name']}")
                            add(eid, x.get("title"), "extension title", x["file"], "StructureDefinition.title")
                        m = re.fullmatch(r"Extension\.extension:([^.]+)\.value\[x\]", xe["id"])
                        if m and xe.get("max") != "0":
                            sub = f"{eid}.extension:{m.group(1)}"
                            add(sub, xe.get("label"), "extension value label", x["file"], xe["id"], xe.get("types"), f"extension {x['name']}")
                            T[sub]["subExtensionUrl"] = next((y.get("fixedUri") for y in x["elements"]
                                                             if y["id"] == f"Extension.extension:{m.group(1)}.url" and y.get("fixedUri")), m.group(1))
                    continue
                if not e.get("label") and eid not in T:
                    continue
                add(eid, e.get("label"), "element label", layer["file"], e["id"], e.get("types"), e.get("typeFrom"))
        for (url, path), labs in qitems.items():
            if url == s["url"] and path in T:
                T[path]["labels"] += labs
        for t in T.values():
            t["container"] = any(o.startswith(t["path"] + ".") for o in T if o != t["path"])
        profiles[s["url"]] = {"url": s["url"], "name": s["name"], "id": s["id"], "title": s.get("title"), "type": s["type"],
                              "file": s["file"], "targets": [t for t in T.values() if t["labels"]], "all": T,
                              "topExtensions": [(eid, url, ext[url][1]) for eid, url in top_ext if url in ext]}
    return profiles, ext


# ------------------------------------------------------------------ 3. matching
def label_match(model_el, target):
    """Evidence that one logical-model element and one target element carry an equal label, or []."""
    ev = []
    for a in model_el["labels"]:
        na, ra = norm_label(a)
        for b in target["labels"]:
            nb, rb = norm_label(b["value"])
            if na and na == nb:
                ev.append({"kind": "label", "ihris4": a, "ihris5": b["value"], "source": b["source"], "file": b["file"], "path": b["path"],
                           **({"normalisation": "date-of"} if (ra or rb) and ra != rb else {})})
    return ev


def type_ok(model_el, target):
    return bool(set(target["types"]) & COMPATIBLE[model_el["type"]])


def authored_decisions():
    """The owner's decisions on mapping items in authored/: an ACCEPTED item that selects one candidate gives
    {(model, ig): profile url} or {(model, ig, element): target path}; a REJECTED item's candidates are never matched
    again (returned as the set `rejected` of (model, ig, element or None, target))."""
    models, elements, rejected = {}, {}, set()
    for p in sorted(glob.glob(os.path.join(AUTHORED, "*.json"))):
        d = J(p)
        for it in d.get("items") or []:
            if it.get("kind") == "mapping" and it.get("status") == "rejected":
                rejected |= {(c["model"], c["ig"], c.get("element"), c["target"]) for c in it.get("candidates") or []}
            if it.get("kind") != "mapping" or it.get("status") != "accepted" or not it.get("selected"):
                continue
            c = next((c for c in it.get("candidates") or [] if c["id"] == it["selected"]), None)
            if not c:
                continue
            if c["level"] == "model":
                models[(c["model"], c["ig"])] = (c["target"], f"{rel(p)}#{it['id']}")
            else:
                elements[(c["model"], c["ig"], c["element"])] = (c["target"], f"{rel(p)}#{it['id']}")
    return models, elements, rejected


def match_model(m, profiles, ig_id, rejected):
    """Model-level candidates in one IG: name equality, and the element-level majority."""
    cands = {}
    for url, P in profiles.items():
        if (m["model"], ig_id, None, url) in rejected:
            continue
        basic = P["type"] == "Basic"
        keys = [("name", P["name"], P["file"], name_key(P["name"], basic)), ("id", P["id"], P["file"], name_key(P["id"], basic))]
        if P.get("title"):
            keys.append(("title", P["title"], P["file"], name_key(P["title"], basic)))
        for eid, xurl, x in P["topExtensions"]:
            if any(e["id"].startswith("Extension.extension:") for e in x["elements"]):  # complex: a group of fields, as a form is
                for k in ("name", "title"):
                    if x.get(k):
                        keys.append((f"extension {k} (at {eid})", x[k], x["file"], name_key(x[k])))
        for kind, value, src_file, key in keys:
            same = sorted({f"{nkind} {nval!r}" for nkind, nval, _ in m["names"] if key and key == name_key(nval)})
            if same:
                cands.setdefault(url, []).append({"kind": "name", "ihris4": same, "ihris4File": m["file"],
                                                  "ihris5": f"{kind} {value!r}", "file": src_file, "key": key})
        hits = [e["element"] for e in m["elements"] if any(label_match(e, t) for t in P["targets"])]
        if len(hits) >= 2 and len(hits) * 2 > len(m["elements"]):
            cands.setdefault(url, []).append({"kind": "majority", "matched": len(hits), "of": len(m["elements"]), "elements": hits})
    return [{"profile": u, "name": profiles[u]["name"], "evidence": ev} for u, ev in sorted(cands.items())]


def match_elements(m, P, ig_id, el_decisions, rejected):
    rows = []
    for e in m["elements"]:
        cands = []
        for t in P["targets"]:
            if (m["model"], ig_id, e["element"], t["path"]) in rejected:
                continue
            ev = label_match(e, t)
            if ev:
                cands.append({"path": t["path"], "types": t["types"], "typeCompatible": type_ok(e, t), "evidence": ev})
        dec = el_decisions.get((m["model"], ig_id, e["element"]))
        if dec and any(t["path"] == dec[0] for t in P["targets"]):
            tier, target, by = "accepted", dec[0], dec[1]
        elif len(cands) == 1 and cands[0]["typeCompatible"]:
            tier, target, by = "exact", cands[0]["path"], None
        else:
            tier, target, by = ("ambiguous" if cands else "none"), None, None
        rows.append({"element": e["element"], "field": e["field"], "labels": e["labels"], "type": e["type"], "tier": tier,
                     **({"target": target} if target else {}), **({"decidedBy": by} if by else {}), "candidates": cands})
    # Two elements on one target: the evidence does not say which, so neither is exact.
    taken = {}
    for r in rows:
        if r["tier"] == "exact":
            taken.setdefault(r["target"], []).append(r)
    for rs in taken.values():
        if len(rs) > 1:
            for r in rs:
                r["tier"], r["contention"] = "ambiguous", [x["element"] for x in rs if x is not r]
                del r["target"]
    return rows


def crosswalk(idx):
    models = ihris4_models()
    mdec, edec, rejected = authored_decisions()
    per_ig = {ig["id"]: ig_targets(ig, idx["igs"]) for ig in idx["igs"]}
    out_models = []
    for m in models:
        targets = []
        for ig in idx["igs"]:
            profiles, ext = per_ig[ig["id"]]
            cands = match_model(m, profiles, ig["id"], rejected)
            dec = mdec.get((m["model"], ig["id"]))
            if dec and dec[0] in profiles:
                tier, prof, by = "accepted", dec[0], dec[1]
            elif len(cands) == 1:
                tier, prof, by = "exact", cands[0]["profile"], None
            else:
                tier, prof, by = ("ambiguous" if cands else "none"), None, None
            t = {"ig": ig["id"], "tier": tier, "candidates": cands}
            if prof:
                t["profile"] = prof
                t["profileName"] = profiles[prof]["name"]
                if by:
                    t["decidedBy"] = by
                t["elements"] = match_elements(m, profiles[prof], ig["id"], edec, rejected)
                t["structureMap"] = map_ref(m, ig["id"]) if any(r["tier"] in ("exact", "accepted") for r in t["elements"]) else None
            targets.append(t)
        out_models.append({"model": m["model"], "url": m["url"], "class": m["class"], "file": m["file"],
                           "elements": len(m["elements"]), "targets": targets})
    counts = {}
    for ig in idx["igs"]:
        ts = [t for x in out_models for t in x["targets"] if t["ig"] == ig["id"]]
        c = {"models": {k: sum(t["tier"] == k for t in ts) for k in ("exact", "accepted", "ambiguous", "none")},
             "elements": {k: sum(r["tier"] == k for t in ts for r in t.get("elements") or []) for k in ("exact", "accepted", "ambiguous", "none")},
             "structureMaps": sum(bool(t.get("structureMap")) for t in ts)}
        counts[ig["id"]] = c
    return {"$schema": "ihris-fhir-crosswalk/v1",
            "_comment": f"GENERATED by {TOOL}. Do not edit: change the inputs, an owner decision in "
                        "src/ihris-data-dictionary/authored/, or the matcher.",
            "index": {"file": rel(INDEX), "sha256": sha256_file(INDEX)},
            "source": {"canonical": CANONICAL, "logicalModels": len(models), "elements": sum(len(m["elements"]) for m in models)},
            "method": {
                "modelLevel": "per IG: a logical model's names (group, title, I2CE class, forms, forms' display names) equal, "
                              "after name normalisation, to a profile's name, id or title, or to the name or title of a complex "
                              "extension the profile carries at its top level; or the element-level majority (at least 2, and "
                              "more than half, of the model's elements have a label-equal element in the profile). One "
                              "candidate: exact; several: ambiguous; none: none; an owner-accepted proposal: accepted.",
                "elementLevel": "inside the model's profile: an I2CE field label equal, after label normalisation, to an element "
                                "label, the label of an extension's value, an extension's title, or a Questionnaire item's text "
                                "defined on that element. One type-compatible candidate: exact; several, type-incompatible, or two "
                                "fields on one element: ambiguous; none: none.",
                "nameNormalisation": "drop a leading iHRIS/Ihris/ihris- (and, on a profile of Basic, a leading Basic); keep letters "
                                     "and digits; lower case",
                "labelNormalisation": "lower case; punctuation and spacing collapsed; 'Date of X' read as 'X Date' (recorded as "
                                      "normalisation date-of on each match it makes)",
                "typeCompatibility": {k: sorted(v) for k, v in COMPATIBLE.items()},
                "noSynonyms": "No synonym table and no judgement: candidates are equalities only.",
            },
            "igs": [{"id": ig["id"], "path": ig["path"], "title": ig["title"], "canonical": ig["canonical"],
                     "compile": {k: ig["compile"][k] for k in ("errors", "warnings")}} for ig in idx["igs"]],
            "counts": counts, "models": out_models}


def map_ref(m, ig_id):
    sid = f"{m['model'].replace('_', '-')}-to-ihris5-{ig_id}"
    return {"id": sid, "url": f"{CANONICAL}/StructureMap/{sid}", "file": f"src/ihris-4-on-fhir/input/fsh/maps/{sid}.fsh"}


# ------------------------------------------------------------------ 4. StructureMaps
def fs(s):
    return gen_fsh.fsh_string(s)


def structure_map(m, t, P, src_file):
    """One StructureMap as an FSH Instance: source the logical model, target the iHRIS 5 profile (by URL only). Each
    exact element is one rule; targets inside the same element or extension share one parent rule, so a complex
    extension's parts land in one extension."""
    ref = t["structureMap"]
    rules = [r for r in t["elements"] if r["tier"] in ("exact", "accepted")]
    tinfo = P["all"]
    root = P["type"]
    tree = {}  # segment -> {"_": [(rule)], children...}
    for r in rules:
        segs = r["target"].split(".")[1:]
        node = tree
        for s in segs[:-1]:
            node = node.setdefault(s, {})
        node.setdefault(segs[-1], {}).setdefault("__leaf__", []).append(r)
    title = f"iHRIS 4 {m['model']} to iHRIS 5 {P['name']} ({t['ig']})"
    lines = [gen_fsh.HEADER.format(src=src_file).replace("gen_fsh.py", "map_ihris5.py"),
             f"Instance: {ref['id']}", "InstanceOf: StructureMap", "Usage: #definition",
             f"* id = {fs(ref['id'])}", f"* url = {fs(ref['url'])}", f"* version = {fs(gen_fsh.RELEASE)}",
             f"* name = {fs(re.sub(r'[^A-Za-z0-9]', '', m['model'].title() if '_' in m['model'] else m['model']) + 'ToIhris5' + t['ig'].title())}",
             f"* title = {fs(title)}",
             "* status = #draft",
             f"* description = {fs('GENERATED from src/ihris-4-on-fhir/mapping/crosswalk.json: only the exact (and owner-accepted) element matches, by label equality. Values the target profile fixes (such as Basic.code) are not set here. iHRIS 5 is referenced by canonical only; it is not an IG dependency (D5).')}",
             f"* structure[0].url = {fs(m['url'])}", "* structure[0].mode = #source", f"* structure[0].alias = {fs(m['model'])}",
             f"* structure[1].url = {fs(P['url'])}", "* structure[1].mode = #target", f"* structure[1].alias = {fs(P['name'])}",
             f"* group[0].name = {fs(m['model'].replace('_', '-'))}", "* group[0].typeMode = #none",
             "* group[0].input[0].name = \"src\"", f"* group[0].input[0].type = {fs(m['model'])}", "* group[0].input[0].mode = #source",
             "* group[0].input[1].name = \"tgt\"", f"* group[0].input[1].type = {fs(P['name'])}", "* group[0].input[1].mode = #target"]
    n = [0]

    def var(prefix):
        n[0] += 1
        return f"{prefix}{n[0]}"

    def ext_url(path):
        x = tinfo.get(path) or {}
        return x.get("extension") or x.get("subExtensionUrl")

    def emit(prefix, rule_name, src_el, targets, children):
        lines.append(f"* {prefix}.name = {fs(rule_name)}")
        lines.append(f"* {prefix}.source[0].context = \"src\"")
        if src_el:
            lines.append(f"* {prefix}.source[0].element = {fs(src_el[0])}")
            lines.append(f"* {prefix}.source[0].variable = {fs(src_el[1])}")
        for i, tg in enumerate(targets):
            for k, v in tg.items():
                if k == "transform":
                    lines.append(f"* {prefix}.target[{i}].transform = #{v}")
                elif k == "param":
                    kind, val = v
                    lines.append(f"* {prefix}.target[{i}].parameter[0].{kind} = {fs(val)}")
                else:
                    lines.append(f"* {prefix}.target[{i}].{k} = {fs(v)}")
        for j, ch in enumerate(children):
            ch(f"{prefix}.rule[{j}]")

    def plan(node, path, ctx):
        """Rule emitters for one level of the target tree under context variable `ctx`."""
        out = []
        for seg, sub in node.items():
            if seg == "__leaf__":
                continue
            p = f"{path}.{seg}"
            elem = seg.split(":")[0]
            elem = "value" if elem == "value[x]" else elem
            url = ext_url(p) if elem == "extension" else None
            for r in sub.get("__leaf__", []):
                def leaf(prefix, r=r, p=p, elem=elem, url=url):
                    s = var("s")
                    tv = var("t")
                    tg = []
                    final_ctx = ctx
                    if url:  # an extension (or a part of one): its url, then its value
                        tg += [{"context": ctx, "element": "extension", "variable": tv},
                               {"context": tv, "element": "url", "transform": "copy", "param": ("valueString", url)},
                               {"context": tv, "element": "value", "transform": "copy", "param": ("valueId", s)}]
                    elif r["type"] == "Coding" and "CodeableConcept" in tinfo[p]["types"]:
                        tg += [{"context": final_ctx, "element": elem, "variable": tv},
                               {"context": tv, "element": "coding", "transform": "copy", "param": ("valueId", s)}]
                    else:
                        tg += [{"context": final_ctx, "element": elem, "transform": "copy", "param": ("valueId", s)}]
                    emit(prefix, r["element"], (r["element"], s), tg, [])
                out.append(leaf)
            kids = {k: v for k, v in sub.items() if k != "__leaf__"}
            if kids:
                def container(prefix, p=p, elem=elem, url=url, kids=kids, seg=seg):
                    tv = var("t")
                    tg = [{"context": ctx, "element": elem, "variable": tv}]
                    if url:
                        tg.append({"context": tv, "element": "url", "transform": "copy", "param": ("valueString", url)})
                    emit(prefix, re.sub(r"[^A-Za-z0-9\-.]", "-", seg).strip("-"), None, tg, plan(kids, p, tv))
                out.append(container)
        return out

    for j, em in enumerate(plan(tree, root, "tgt")):
        em(f"group[0].rule[{j}]")
    return "\n".join(lines) + "\n"


def all_maps(cw, idx):
    per_ig = {ig["id"]: ig_targets(ig, idx["igs"])[0] for ig in idx["igs"]}
    out = {}
    for m in cw["models"]:
        for t in m["targets"]:
            if t.get("structureMap"):
                P = per_ig[t["ig"]][t["profile"]]
                out[os.path.basename(t["structureMap"]["file"])] = structure_map(m, t, P, "src/ihris-4-on-fhir/mapping/crosswalk.json")
    return out


# ------------------------------------------------------------------ 5. the gap report
def gaps(cw, idx):
    per_ig = {ig["id"]: ig_targets(ig, idx["igs"]) for ig in idx["igs"]}
    ih4 = []
    for m in cw["models"]:
        tiers = {t["ig"]: t["tier"] for t in m["targets"]}
        mapped = {}
        for t in m["targets"]:
            for r in t.get("elements") or []:
                if r["tier"] in ("exact", "accepted"):
                    mapped.setdefault(r["element"], []).append(t["ig"])
        lm = next(x for x in ihris4_models() if x["model"] == m["model"])
        for e in lm["elements"]:
            if e["element"] not in mapped:
                per = {}
                for t in m["targets"]:
                    r = next((r for r in t.get("elements") or [] if r["element"] == e["element"]), None)
                    per[t["ig"]] = (r["tier"] if r else f"model {tiers[t['ig']]}")
                ih4.append({"model": m["model"], "element": e["element"], "label": e["labels"][0] if e["labels"] else None, "byIg": per})
    ih5 = {}
    for ig in idx["igs"]:
        profiles, ext = per_ig[ig["id"]]
        used = {}
        cands = set()
        for m in cw["models"]:
            for t in m["targets"]:
                if t["ig"] != ig["id"]:
                    continue
                for r in t.get("elements") or []:
                    if r.get("target"):
                        used.setdefault((t["profile"], r["target"]), []).append(f"{m['model']}.{r['element']}")
                    for c in r["candidates"]:
                        cands.add((t["profile"], c["path"]))
        rows = []
        covered_ext = set()
        for url, P in profiles.items():
            for x in P["targets"]:
                if (url, x["path"]) in used:
                    if x.get("extension"):
                        covered_ext.add(x["extension"])
                    for pre_url in [y.get("extension") for y in P["targets"] if x["path"].startswith(y["path"] + ".") and y.get("extension")]:
                        covered_ext.add(pre_url)
                    continue
                if x["container"]:
                    continue
                rows.append({"profile": P["name"], "path": x["path"], "label": x["labels"][0]["value"],
                             "candidateOnly": (url, x["path"]) in cands})
        exts = [{"extension": s["name"], "url": s["url"], "title": s.get("title")} for s in idx_structs(idx, ig["id"])
                if s["type"] == "Extension" and s["url"] not in covered_ext]
        ih5[ig["id"]] = {"profileElements": rows, "extensions": exts}
    return {"$schema": "ihris-fhir-gaps/v1",
            "_comment": f"GENERATED by {TOOL} from the crosswalk. Do not edit.",
            "crosswalk": {"file": rel(CROSSWALK), "sha256": hashlib.sha256(dump(cw).encode()).hexdigest()},
            "counts": {"ihris4ElementsWithNoTarget": len(ih4),
                       "ihris5": {k: {"profileElements": len(v["profileElements"]), "extensions": len(v["extensions"])} for k, v in ih5.items()}},
            "ihris4": ih4, "ihris5": ih5}


def idx_structs(idx, ig_id):
    return next(ig for ig in idx["igs"] if ig["id"] == ig_id)["structures"]


def gaps_md(cw, g):
    L = ["<!-- GENERATED by src/tools/map_ihris5.py from crosswalk.json and gaps.json. Do not edit. -->", "",
         "# iHRIS 4 to iHRIS 5: the crosswalk and its gaps", "",
         f"iHRIS 5 is iHRIS/iHRIS at `{J(INDEX)['source']['commit'][:12]}`, compiled with SUSHI {SUSHI_VERSION}. "
         "Matches are equalities of names and labels only (see `crosswalk.json` `method`); everything else is a proposal "
         "for the owner in `src/ihris-data-dictionary/authored/ihris5-mapping.json`.", "",
         "## Per IG", "", "| IG | SUSHI errors | models exact / accepted / ambiguous / none | elements exact / accepted / ambiguous / none | StructureMaps |",
         "|---|---|---|---|---|"]
    for ig in cw["igs"]:
        c = cw["counts"][ig["id"]]
        L.append(f"| `{ig['id']}` ({ig['path']}) | {ig['compile']['errors']} | " + " / ".join(str(c["models"][k]) for k in ("exact", "accepted", "ambiguous", "none"))
                 + " | " + " / ".join(str(c["elements"][k]) for k in ("exact", "accepted", "ambiguous", "none")) + f" | {c['structureMaps']} |")
    L += ["", "## Models with a candidate", "", "| logical model | IG | tier | target (or candidates) | elements exact / ambiguous / none |", "|---|---|---|---|---|"]
    for m in cw["models"]:
        for t in m["targets"]:
            if t["tier"] == "none":
                continue
            els = t.get("elements") or []
            cnt = " / ".join(str(sum(r["tier"] == k or (k == "exact" and r["tier"] == "accepted") for r in els)) for k in ("exact", "ambiguous", "none")) if els else "–"
            tgt = t.get("profileName") or ", ".join(c["name"] for c in t["candidates"])
            L.append(f"| {m['model']} | `{t['ig']}` | {t['tier']} | {tgt} | {cnt} |")
    L += ["", f"## iHRIS 4 elements with no target in any IG ({g['counts']['ihris4ElementsWithNoTarget']})", "",
          "| logical model | element | label | " + " | ".join(ig["id"] for ig in cw["igs"]) + " |", "|---|---|---|" + "---|" * len(cw["igs"])]
    for r in g["ihris4"]:
        L.append(f"| {r['model']} | `{r['element']}` | {r['label'] or ''} | " + " | ".join(r["byIg"][ig["id"]] for ig in cw["igs"]) + " |")
    for ig in cw["igs"]:
        v = g["ihris5"][ig["id"]]
        L += ["", f"## iHRIS 5 `{ig['id']}`: profile elements with no iHRIS 4 source ({len(v['profileElements'])})", "",
              "| profile | element | label | has a candidate |", "|---|---|---|---|"]
        L += [f"| {r['profile']} | `{r['path']}` | {r['label']} | {'yes' if r['candidateOnly'] else ''} |" for r in v["profileElements"]]
        L += ["", f"### Extensions with no iHRIS 4 source ({len(v['extensions'])})", ""]
        L += [f"- {x['extension']} ({x['title'] or ''}), `{x['url']}`" for x in v["extensions"]]
    return "\n".join(L) + "\n"


# ------------------------------------------------------------------ 6. proposals (additive, for the owner)
def bean_examples():
    """The bean's own examples, `Model→Profile`, as written in its text."""
    text = open(BEAN, encoding="utf-8").read()
    return re.findall(r"([A-Za-z_]+)→([A-Za-z]+)", text)


def propose(cw, idx):
    per_ig = {ig["id"]: ig_targets(ig, idx["igs"])[0] for ig in idx["igs"]}
    have = J(PROPOSAL) if os.path.exists(PROPOSAL) else {
        "$schema": "ihris-dak-proposal/v1", "id": "ihris5-mapping",
        "title": "F4: mapping the iHRIS 4 logical models to the three iHRIS 5 IGs: what the matcher could not decide",
        "author": f"{TOOL} --propose (candidates found by the matcher, or the bean's examples as cited), for owner review",
        "date": "2026-10-09", "refs": ["bean ihris-7gl8", "src/ihris-4-on-fhir/mapping/crosswalk.json"], "items": []}
    ids = {i["id"] for i in have["items"]}
    new = []

    def add(item):
        if item["id"] not in ids:
            new.append(item)
            ids.add(item["id"])
    for m in cw["models"]:
        for t in m["targets"]:
            if t["tier"] == "ambiguous":
                add({"id": f"model-{m['model']}-{t['ig']}", "kind": "mapping", "status": "proposed",
                     "appliesTo": [m["url"]],
                     "statement": f"Which profile of the iHRIS 5 `{t['ig']}` IG holds the logical model {m['model']}? The matcher found "
                                  f"{len(t['candidates'])} candidates and cannot choose. Accept with `selected` = one candidate id, or reject.",
                     "rationale": "Several profiles carry equal names or a majority of equal labels (see each candidate's evidence).",
                     "evidence": ["src/ihris-4-on-fhir/mapping/crosswalk.json"],
                     "candidates": [{"id": f"c{i + 1}", "level": "model", "model": m["model"], "ig": t["ig"], "target": c["profile"],
                                     "basis": "matcher", "evidence": [ev_text(e) for e in c["evidence"]]} for i, c in enumerate(t["candidates"])]})
            for r in t.get("elements") or []:
                if r["tier"] == "ambiguous" and r["candidates"]:
                    add({"id": f"element-{m['model']}-{r['element']}-{t['ig']}", "kind": "mapping", "status": "proposed",
                         "appliesTo": [f"{m['url']}#{m['model']}.{r['element']}"],
                         "statement": f"Which element of {t['profileName']} (`{t['ig']}`) holds {m['model']}.{r['element']} "
                                      f"({' / '.join(r['labels'])}, {r['type']})?",
                         "rationale": ("Several elements carry an equal label." if len(r["candidates"]) > 1 else
                                       "One element carries an equal label, but its type is not one the field's type copies into.")
                         + (f" Also contended by {', '.join(r['contention'])}." if r.get("contention") else ""),
                         "evidence": ["src/ihris-4-on-fhir/mapping/crosswalk.json"],
                         "candidates": [{"id": f"c{i + 1}", "level": "element", "model": m["model"], "element": r["element"], "ig": t["ig"],
                                         "target": c["path"], "basis": "matcher",
                                         "evidence": [ev_text(e) for e in c["evidence"]] + [f"types {c['types']}; type-compatible: {c['typeCompatible']}"]}
                                        for i, c in enumerate(r["candidates"])]})
    # The bean's examples, where the matcher did not already decide them: cited as the bean's, checked against the pin.
    for model, prof in bean_examples():
        found = [(ig, P) for ig, ps in per_ig.items() for P in ps.values() if P["name"] == prof]
        mm = next((x for x in cw["models"] if x["model"] == model), None)
        if not mm:
            continue
        for ig, P in found:
            t = next(t for t in mm["targets"] if t["ig"] == ig)
            if t.get("profile") == P["url"]:
                continue
            item = next((i for i in new if i["id"] == f"model-{model}-{ig}"), None)
            c = next((c for c in (item or {}).get("candidates") or [] if c["target"] == P["url"]), None)
            if c:  # the matcher already found it: the bean is one more source for that candidate
                c["evidence"].append(f"also named by bean ihris-7gl8: '{model}→{prof}'")
                continue
            add({"id": f"bean-{model}-{ig}", "kind": "mapping", "status": "proposed", "appliesTo": [mm["url"]],
                 "statement": f"The bean's example {model}→{prof}: the logical model {model} is held by {prof} in the iHRIS 5 `{ig}` IG.",
                 "rationale": f"Named in bean ihris-7gl8's text as an example. The matcher's own result here is `{t['tier']}`"
                              + (f" (candidates: {', '.join(c['name'] for c in t['candidates'])})" if t["candidates"] else "")
                              + f". {prof} exists at the pin as {P['url']}.",
                 "evidence": [rel(BEAN), "src/ihris-4-on-fhir/mapping/ihris5-index.json"],
                 "candidates": [{"id": "c1", "level": "model", "model": model, "ig": ig, "target": P["url"], "basis": "bean ihris-7gl8",
                                 "evidence": [f"bean ihris-7gl8: '{model}→{prof}'"]}]})
        if not found:
            add({"id": f"bean-{model}-absent", "kind": "upstream-observation", "status": "to-verify", "appliesTo": [mm["url"]],
                 "statement": f"The bean's example {model}→{prof} names a profile that is not in the three IGs at the pinned commit.",
                 "rationale": "Checked against the compiled index: no profile has that name. The bean's text may predate a rename.",
                 "evidence": [rel(BEAN), "src/ihris-4-on-fhir/mapping/ihris5-index.json"]})
    have["items"] += new
    open(PROPOSAL, "w", encoding="utf-8").write(json.dumps(have, indent=2, ensure_ascii=False) + "\n")
    print(f"map_ihris5: {len(new)} proposal item(s) added to {rel(PROPOSAL)} ({len(have['items'])} in all)")


def ev_text(e):
    if e["kind"] == "majority":
        return f"majority: {e['matched']} of {e['of']} elements label-equal ({', '.join(e['elements'])})"
    if e["kind"] == "name":
        return f"name: iHRIS 4 {', '.join(e['ihris4'])} ({e['ihris4File']}) = iHRIS 5 {e['ihris5']} ({e['file']}), key {e['key']!r}"
    return f"label: {e['ihris4']!r} = {e['source']} {e['ihris5']!r} ({e['file']} {e['path']})" + (" [date-of]" if e.get("normalisation") else "")


# ------------------------------------------------------------------ main
def outputs(idx):
    cw = crosswalk(idx)
    g = gaps(cw, idx)
    files = {rel(CROSSWALK): dump(cw), rel(GAPS): dump(g), rel(GAPS_MD): gaps_md(cw, g)}
    for name, text in all_maps(cw, idx).items():
        files[rel(os.path.join(MAPS_FSH, name))] = text
    return cw, files


def stale(files):
    have = {rel(p): open(p, encoding="utf-8").read() for p in glob.glob(os.path.join(MAPS_FSH, "*.fsh"))}
    for p in (CROSSWALK, GAPS, GAPS_MD):
        if os.path.exists(p):
            have[rel(p)] = open(p, encoding="utf-8").read()
    return sorted(set(have) ^ set(files)) + sorted(k for k in files if k in have and have[k] != files[k])


def main():
    if "--index" in sys.argv:
        build_index()
        return
    if "--check" in sys.argv:
        if not os.path.exists(INDEX):
            raise SystemExit(f"map_ihris5: {rel(INDEX)} is missing")
        cw, files = outputs(J(INDEX))
        bad = stale(files)
        if bad:
            raise SystemExit("map_ihris5: STALE (run python3 src/tools/map_ihris5.py): " + ", ".join(bad[:10]))
        print(f"map_ihris5: OK ({sum(c['structureMaps'] for c in cw['counts'].values())} StructureMaps; crosswalk and gaps current)")
        return
    # The index is a function of the pin and the SUSHI version: rebuilt when either moved (or with --index).
    have = J(INDEX) if os.path.exists(INDEX) else None
    if not have or (have["source"]["commit"], have["sushi"]) != (pin()[1], SUSHI_VERSION):
        idx = build_index()
    else:
        idx = have
    cw, files = outputs(idx)
    if os.path.isdir(MAPS_FSH):
        shutil.rmtree(MAPS_FSH)
    os.makedirs(MAPS_FSH, exist_ok=True)
    for r, text in files.items():
        open(os.path.join(ROOT, r), "w", encoding="utf-8").write(text)
    for ig, c in cw["counts"].items():
        print(f"map_ihris5: {ig}: models {c['models']}, elements {c['elements']}, {c['structureMaps']} StructureMap(s)")
    if "--propose" in sys.argv:
        propose(cw, idx)


if __name__ == "__main__":
    main()
