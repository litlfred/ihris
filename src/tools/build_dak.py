#!/usr/bin/env python3
"""Derive a WHO SMART Guidelines DAK (L2) data dictionary from the iHRIS data model.

Input : src/<instance>/data-model/<release>/*.json   (ihris-form-class/v1, from build_kg.py)
        library/ihris-wiki/osi-help-<release>/sections/*.md (evidence only)
Output: src/ihris-dak/data-dictionary/<group>.json   (ihris-dak-data-dictionary/v1)
        src/ihris-dak/data-dictionary.csv / .xlsx    (WHO column order)
        src/ihris-dak/terminology/*.json             (FHIR R4 CodeSystem / ValueSet)
        docs/generated/dak-data-dictionary.md

What this does NOT do, on purpose:
- It never writes a description. The source has none per field, and a guessed
  definition would look authoritative. `description` stays null with
  `descriptionStatus: "to-author"`; wiki passages that mention the label are
  attached as `evidence` for whoever authors it.
- It never infers conditionality, indicator linkages or decision-table
  linkages. Those columns are left empty for a human, as the WHO guide intends.

Column semantics follow the "Form data mapping guide" in WHO's Digital
transformation handbook for primary health care (9789240093362, pp. 86-90).
The column layout is borrowed from that WHO guide; iHRIS is independent of
WHO SMART Guidelines and smart-base (owner ruling, 2026-09-23).
"""
from __future__ import annotations

import collections
import csv
import glob
import json
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RELEASE = "4.3.3"
OUT = os.path.join(ROOT, "src", "ihris-dak")
# PROVISIONAL canonical base. Not http://ihris.org/fhir, which is the iHRIS 5
# IG's canonical and is not ours to mint under. To be confirmed by the owner.
CANONICAL = "https://litlfred.github.io/ihris/dak"
DAK_PREFIX = "IHRIS.DE"
INSTANCES = ["i2ce", "ihris-common", "ihris-manage", "ihris-qualify"]

# I2CE formfield -> (WHO DAK data type, quantity sub-type, note)
TYPE_MAP = {
    "STRING_LINE": ("String", None, None),
    "STRING_MLINE": ("String", None, "multi-line text"),
    "STRING_TEXT": ("String", None, "long text"),
    "DATE_YMD": ("Date", None, None),
    "DATE_Y": ("Date", None, "year only"),
    "DATE_YM": ("Date", None, "year and month only"),
    "DATE_MD": ("Date", None, "month and day only (no year)"),
    "DATE_HMS": ("Time", None, None),
    "DATE_TIME": ("DateTime", None, None),
    "YESNO": ("Boolean", None, None),
    "BOOL": ("Boolean", None, None),
    "INT": ("Quantity", "Integer quantity", None),
    "PERCENT_INT": ("Quantity", "Integer quantity", "percentage (unit %)"),
    "FLOAT": ("Quantity", "Decimal quantity", None),
    "CURRENCY": ("Quantity", "Decimal quantity", "monetary amount; the currency is part of the value in iHRIS"),
    "INT_GENERATE": ("ID", None, "system-generated number"),
    "REFERENCE": ("ID", None, "reference to another record"),
    "MAP": ("List - select one", None, None),
    "ENUM": ("List - select one", None, "options are enumerated inline in the field configuration, not a list form"),
    "ASSOC_MAP": ("List - select one", None, "associative map: I2CE ASSOC_MAP"),
    "ASSOC_LIST": ("List - select all that apply", None, "associative list: I2CE ASSOC_LIST"),
    "ASSOC_MAP_RESULTS": ("List - select one", None, "associative map results: I2CE ASSOC_MAP_RESULTS"),
    "MAP_MULT": ("List - select all that apply", None, None),
    "DOCUMENT": ("Attachment", None, None),
    "IMAGE": ("Attachment", None, "image"),
}
EXCLUDED_TYPES = {"STRING_PASS": "a password; never a data element", "REMAP": "an I2CE remapping pointer, not data"}

LIST_ROOTS = {"I2CE_List", "I2CE_SimpleList", "I2CE_SimpleCodedList", "I2CE_ListLink"}
# Infrastructure, integration plumbing and application state: not health workforce data.
SYSTEM_EXACT = {"class", "formClass", "dep_class", "user_request_class_data", "iHRIS_Archive", "iHRIS_UUID_Map", "iHRIS_UserMap",
                "iHRIS_UserAlert", "iHRIS_UserCronReport", "iHRIS_UserTrigger", "iHRIS_Workflows", "iHRIS_DataElement",
                "iHRIS_DataSet", "iHRIS_DHIS_CodedList", "SVS_CodedList", "iHRIS_UserAccessDepartment", "iHRIS_UserAccessFacility",
                "iHRIS_RapidproFlowRun", "iHRIS_RapidproFlowRunSteps", "iHRIS_RapidproFlowRunValues"}


def write_json(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")


def short(cls: str) -> str:
    return re.sub(r"^(iHRIS|I2CE|CSD)_", "", cls)


def load_classes():
    """Merge each form class across instances. The same class name in two packages is one DAK element set."""
    merged = {}
    for inst in INSTANCES:
        for f in sorted(glob.glob(os.path.join(ROOT, "src", inst, "data-model", RELEASE, "*.json"))):
            d = json.load(open(f))
            m = merged.setdefault(d["class"], {"class": d["class"], "extends": d["extends"], "forms": set(), "sources": [], "fields": collections.OrderedDict()})
            m["extends"] = m["extends"] or d["extends"]
            m["forms"] |= set(d["forms"])
            m["sources"].append(d["id"])
            for fl in d["fields"]:
                cur = m["fields"].setdefault(fl["field"], {**fl, "definedIn": list(fl["definedIn"])})
                if cur is not fl:
                    for k in ("type", "label", "references"):
                        cur[k] = cur.get(k) or fl.get(k)
                    cur["required"] = cur["required"] or fl["required"]
                    cur["definedIn"] = sorted(set(cur["definedIn"]) | set(fl["definedIn"]))
    return merged


def root_of(cls, merged, seen=()):
    e = merged.get(cls, {}).get("extends")
    if not e or e in seen:
        return e or cls
    if e in LIST_ROOTS or e not in merged:
        return e
    return root_of(e, merged, seen + (cls,))


def scope_of(cls, merged):
    if cls in LIST_ROOTS:
        return "list"  # a form registered directly on a base list class IS a list
    if cls in SYSTEM_EXACT or cls.startswith("I2CE_"):
        return "system"
    if cls.startswith("CSD_"):
        return "system" if "Search" in cls else "interoperability"
    r = root_of(cls, merged)
    if r in LIST_ROOTS:
        return "list"
    return "record"


def form_display():
    """form name -> display name, from the module nodes (the class files only carry form names)."""
    out = {}
    for f in glob.glob(os.path.join(ROOT, "src", "*", "modules", RELEASE, "*.json")):
        for fm in json.load(open(f)).get("forms", []):
            dn = fm.get("displayName")
            if isinstance(dn, str) and fm["form"] not in out:
                out[fm["form"]] = dn
    return out


def wiki_index():
    idx = []
    for f in sorted(glob.glob(os.path.join(ROOT, "library", "ihris-wiki", f"osi-help-{RELEASE}", "sections", "*.md"))):
        idx.append((os.path.relpath(f, ROOT), open(f, encoding="utf-8").read()))
    return idx


def evidence_for(label, wiki):
    if not label or len(label) < 3:
        return []
    pat = re.compile(r"\*\*" + re.escape(label) + r"\*\*", re.I)
    return [p for p, t in wiki if pat.search(t)][:5]


def _pascal(s):
    return "".join(w[:1].upper() + w[1:] for w in re.split(r"[^A-Za-z0-9]+", s) if w)


def load_data_lists():
    """form -> records merged across packages (ihris-data-list/v1 from build_kg.py)."""
    out = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(ROOT, "src", "*", "data-lists", RELEASE, "*.json"))):
        d = json.load(open(f))
        out[d["form"]].extend(d["records"])
    return out


def _display(fields, rid):
    n = fields.get("name")
    if isinstance(n, str) and n:
        return n
    for v in fields.values():
        if isinstance(v, str) and v and "|" not in v:
            return v
    return rid


def build_terminology(forms, form_to_class, fdisp, merged):
    """FHIR R4 CodeSystem/ValueSet JSON for every list in `forms` and every list their records point at.

    default records -> CodeSystem <form>           content=complete  (as shipped; deployments extend it)
    sample records  -> CodeSystem <form>-example-<module>  content=example  (never in a ValueSet)
    ValueSet <form> includes the default CodeSystem only, and has no compose when iHRIS ships none.
    """
    lists = load_data_lists()

    def resolve(target, code, from_module):
        """The CodeSystem that actually holds `code` of list `target`: its default CodeSystem if a
        default record has that id; otherwise the example CodeSystem of the sample module that ships
        it, preferring the referring record's own package (Manage vs Qualify sample data)."""
        recs = lists.get(target, [])
        if any(r["id"] == code and r["provenance"] == "default" for r in recs):
            return f"{CANONICAL}/CodeSystem/{target}"
        mods = sorted({r["definedIn"] for r in recs if r["id"] == code and r["provenance"] == "sample"},
                      key=lambda mm: (mm.split("/")[0] != from_module.split("/")[0], mm))
        if mods:
            return f"{CANONICAL}/CodeSystem/{target}-example-{slug_(mods[0].split('/module/')[1])}"
        return None

    tdir = os.path.join(OUT, "terminology")
    if os.path.isdir(tdir):
        for f in glob.glob(os.path.join(tdir, "*.json")):
            os.remove(f)
    todo, done, summary = list(forms), set(), []
    while todo:
        form = todo.pop(0)
        if form in done:
            continue
        done.add(form)
        recs = lists.get(form, [])
        title = fdisp.get(form) or form.replace("_", " ").title()
        cs_url = f"{CANONICAL}/CodeSystem/{form}"
        entry = {"form": form, "title": title, "default": 0, "examples": {}, "duplicatesMerged": 0}

        def concepts_of(records):
            props, seen, concepts, dup = {}, {}, [], 0
            for r in records:
                if r["id"] in seen:
                    dup += 1
                    continue
                c = {"code": r["id"], "display": _display(r["fields"], r["id"])}
                pv = []
                for k, v in r["fields"].items():
                    if k == "name" or v in ("", [], None):
                        continue
                    vals = v if isinstance(v, list) else [v]
                    for one in vals:
                        cur = re.fullmatch(r"currency\|([^=]+)=(-?[0-9.]+)", one or "")
                        if cur:  # I2CE CURRENCY value: "currency|<currency id>=<amount>"
                            props.setdefault(k, {"code": k, "type": "decimal", "description": f"iHRIS CURRENCY field `{k}`: the amount"})
                            pv.append({"code": k, "valueDecimal": float(cur.group(2))})
                            csys = resolve("currency", cur.group(1), r["definedIn"])
                            if "currency" not in done:
                                todo.append("currency")
                            if csys:
                                props.setdefault(k + "_currency", {"code": k + "_currency", "type": "Coding",
                                                                   "description": f"iHRIS CURRENCY field `{k}`: its currency"})
                                pv.append({"code": k + "_currency", "valueCoding": {"system": csys, "code": cur.group(1)}})
                            continue
                        m = re.fullmatch(r"([a-z_0-9]+)\|(.+)", one or "")
                        if m:
                            if m.group(1) not in done:
                                todo.append(m.group(1))
                            sysurl = resolve(m.group(1), m.group(2), r["definedIn"])
                            if sysurl is None:
                                pk = k + "_unresolved"
                                props.setdefault(pk, {"code": pk, "type": "string",
                                                      "description": f"iHRIS MAP field `{k}` whose target record ships nowhere in {RELEASE}"})
                                pv.append({"code": pk, "valueString": one})
                                continue
                            props.setdefault(k, {"code": k, "type": "Coding", "description": f"iHRIS MAP field `{k}`: a code in the {m.group(1)} list"})
                            pv.append({"code": k, "valueCoding": {"system": sysurl, "code": m.group(2)}})
                        elif one:
                            props.setdefault(k, {"code": k, "type": "string", "description": f"iHRIS field `{k}`"})
                            pv.append({"code": k, "valueString": one})
                if pv:
                    c["property"] = pv
                seen[r["id"]] = c
                concepts.append(c)
            return concepts, list(props.values()), dup

        default = [r for r in recs if r["provenance"] == "default"]
        if default:
            concepts, props, dup = concepts_of(default)
            entry["default"], entry["duplicatesMerged"] = len(concepts), dup
            mods = sorted({r["definedIn"] for r in default})
            cs = {"resourceType": "CodeSystem", "id": f"ihris-{form.replace('_', '-')}", "url": cs_url, "version": RELEASE,
                  "name": f"IHRIS{_pascal(form)}", "title": f"iHRIS {title}", "status": "draft", "experimental": True,
                  "description": f"The `{form}` list as shipped by default in iHRIS {RELEASE} (modules: {', '.join(mods)}). "
                                 "Codes are the iHRIS record ids. Deployments add their own records, so this is the shipped "
                                 "baseline, not a closed international code set."
                                 + (f" {dup} record(s) sharing an id with an earlier one were merged, as I2CE's configuration tree merges them." if dup else ""),
                  "caseSensitive": True, "content": "complete", "count": len(concepts)}
            if props:
                cs["property"] = props
            cs["concept"] = concepts
            write_json(os.path.join(tdir, f"CodeSystem-{form}.json"), cs)
        by_mod = collections.defaultdict(list)
        for r in recs:
            if r["provenance"] == "sample":
                by_mod[r["definedIn"]].append(r)
        for mod, rs in sorted(by_mod.items()):
            mslug = slug_(mod.split("/module/")[1])
            concepts, props, dup = concepts_of(rs)
            entry["examples"][mod] = len(concepts)
            cs = {"resourceType": "CodeSystem", "id": f"ihris-{form.replace('_', '-')}-example-{mslug}"[:64],
                  "url": f"{CANONICAL}/CodeSystem/{form}-example-{mslug}", "version": RELEASE,
                  "name": f"IHRIS{_pascal(form)}Example{_pascal(mslug)}", "title": f"iHRIS {title}: sample data from {mod}",
                  "status": "draft", "experimental": True,
                  "description": f"SAMPLE records for `{form}` from the iHRIS {RELEASE} module `{mod}`. Illustrative data for one "
                                 "fictional or example deployment. NOT a standard code set, and no ValueSet includes it.",
                  "caseSensitive": True, "content": "example", "count": len(concepts)}
            if props:
                cs["property"] = props
            cs["concept"] = concepts
            write_json(os.path.join(tdir, f"CodeSystem-{form}-example-{mslug}.json"), cs)
        vs = {"resourceType": "ValueSet", "id": f"ihris-{form.replace('_', '-')}", "url": f"{CANONICAL}/ValueSet/{form}",
              "version": RELEASE, "name": f"IHRIS{_pascal(form)}VS", "title": f"iHRIS {title}", "status": "draft", "experimental": True}
        if form in ISO_SYSTEMS:
            iso = ISO_SYSTEMS[form]
            vs["description"] = (f"All current codes of {iso['name']} ({iso['system']}). The DAK binds to the standard, not to iHRIS's "
                                 f"shipped `{form}` list; that list is CodeSystem `{form}` here, mapped to the standard by "
                                 f"ConceptMap `{form}-to-{iso['slug']}`.")
            vs["compose"] = {"include": [{"system": iso["system"]}]}
        elif default:
            vs["description"] = f"All codes of the iHRIS `{form}` list as shipped by default in iHRIS {RELEASE}."
            vs["compose"] = {"include": [{"system": cs_url}]}
        else:
            vs["description"] = (f"The iHRIS `{form}` list. iHRIS {RELEASE} ships no default records for it: its codes are defined "
                                 "by each deployment" + (f" (sample data exists: {', '.join(sorted(by_mod))})" if by_mod else "") + ".")
        write_json(os.path.join(tdir, f"ValueSet-{form}.json"), vs)
        entry["valueSet"] = vs["url"]
        entry["inDak"] = form in forms
        summary.append(entry)
    return summary


def slug_(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# Standard code systems the DAK binds to instead of iHRIS's own lists. System URIs are the HL7 ones
# (terminology.hl7.org lists urn:iso:std:iso:3166 and urn:iso:std:iso:4217).
ISO_SYSTEMS = {
    "country": {"system": "urn:iso:std:iso:3166", "name": "ISO 3166-1 alpha-2", "slug": "iso-3166"},
    "currency": {"system": "urn:iso:std:iso:4217", "name": "ISO 4217", "slug": "iso-4217"},
}
ILO_ISCO08 = "http://www.ilo.org/public/english/bureau/stat/isco/isco08/"  # the ILO's own system URL for ISCO-08


def build_isco(fdisp):
    """ISCO-08 / ISCO-88 terminology and the occupation mappings the source itself supports.

    - ValueSet isco-08-unit: the 436 ISCO-08 unit groups iHRIS ships (default data), bound to the
      ILO's own ISCO-08 system URL. iHRIS's record ids ARE ISCO-08 codes, so no ConceptMap is
      needed between them; the level lists become ValueSets too.
    - ISCO-88 has no FHIR canonical we can cite, so iHRIS's shipped ISCO-88 lists become CodeSystems
      here (via build_terminology).
    - job -> ISCO-88 unit group: the first four digits of the job code, kept ONLY when that prefix
      is an ISCO-88 unit group iHRIS ships. classification -> ISCO-88 minor group: its own `code`.
      cadre -> ISCO-88 minor groups: through the jobs that name the cadre (inexact, sample data).
    - ISCO-88 -> ISCO-08 is NOT produced: it needs the ILO correspondence table, not guesswork.
    """
    lists = load_data_lists()
    tdir = os.path.join(OUT, "terminology")
    rec = lambda form: [r for r in lists.get(form, []) if r["provenance"] == "default"]  # noqa: E731
    report = {"isco08": {}, "maps": {}}
    for lvl, n in [("major", 1), ("sub_major", 2), ("minor", 3), ("unit", 4)]:
        rs = rec(f"isco_08_{lvl}")
        vs = {"resourceType": "ValueSet", "id": f"ihris-isco-08-{lvl.replace('_', '-')}", "url": f"{CANONICAL}/ValueSet/isco_08_{lvl}",
              "version": RELEASE, "name": f"IHRISISCO08{_pascal(lvl)}VS", "title": f"ISCO-08 {lvl.replace('_', '-')} groups (as shipped in iHRIS)",
              "status": "draft", "experimental": True,
              "description": f"The {len(rs)} ISCO-08 {lvl.replace('_', '-')} groups iHRIS {RELEASE} ships by default (`isco_08_{lvl}`), "
                             f"as codes of the ILO ISCO-08 system under the ILO's system URL ({ILO_ISCO08}).",
              "compose": {"include": [{"system": ILO_ISCO08, "concept": [{"code": r["id"], "display": r["fields"].get("name", r["id"])} for r in rs]}]}}
        write_json(os.path.join(tdir, f"ValueSet-isco_08_{lvl}.json"), vs)
        report["isco08"][lvl] = len(rs)
    u88 = {r["id"]: r["fields"].get("name") for r in rec("isco_88_unit")}
    m88 = {r["id"]: r["fields"].get("name") for r in rec("isco_88_minor")}
    samples = lambda form: [r for r in lists.get(form, []) if r["provenance"] == "sample"]  # noqa: E731

    def cmap(cid, title, src_form, tgt_form, elements, unmapped, desc):
        src_mods = sorted({r["definedIn"] for r in samples(src_form)})
        src = f"{CANONICAL}/CodeSystem/{src_form}-example-{slug_(src_mods[0].split('/module/')[1])}" if src_mods else f"{CANONICAL}/CodeSystem/{src_form}"
        cm = {"resourceType": "ConceptMap", "id": cid, "url": f"{CANONICAL}/ConceptMap/{cid}", "version": RELEASE,
              "name": _pascal(cid), "title": title, "status": "draft", "experimental": True, "description": desc,
              "sourceUri": f"{CANONICAL}/ValueSet/{src_form}", "targetUri": f"{CANONICAL}/ValueSet/{tgt_form}",
              "group": [{"source": src, "target": f"{CANONICAL}/CodeSystem/{tgt_form}", "element": elements + unmapped}]}
        write_json(os.path.join(tdir, f"ConceptMap-{cid}.json"), cm)
        report["maps"][cid] = {"mapped": len(elements), "unmapped": len(unmapped)}

    jobs = samples("job")
    el, un = [], []
    for r in jobs:
        p = re.match(r"(\d{4})-", r["id"])
        if p and p.group(1) in u88:
            el.append({"code": r["id"], "display": r["fields"].get("title"), "target": [{"code": p.group(1), "display": u88[p.group(1)],
                       "equivalence": "wider", "comment": "The job code's four-digit prefix is this ISCO-88 unit group (verified against iHRIS's shipped ISCO-88 list)."}]})
        else:
            un.append({"code": r["id"], "display": r["fields"].get("title"), "target": [{"equivalence": "unmatched",
                       "comment": (f"Prefix {p.group(1)} is not an ISCO-88 unit group iHRIS ships." if p else "The job code has no ISCO prefix.")}]})
    cmap("job-to-isco-88-unit", "iHRIS sample jobs to ISCO-88 unit groups", "job", "isco_88_unit", el, un,
         "Derived from the iHRIS SAMPLE job list, whose codes are an ISCO-88 unit group plus a local suffix (e.g. 2221-1D). Illustrative: a deployment's own jobs need their own map.")
    cls = samples("classification")
    el, un = [], []
    for r in cls:
        c = r["fields"].get("code")
        if c in m88:
            el.append({"code": r["id"], "display": r["fields"].get("name"), "target": [{"code": c, "display": m88[c], "equivalence": "equivalent",
                       "comment": "Asserted by the record's own `code` field; verified against iHRIS's shipped ISCO-88 minor groups."}]})
        else:
            un.append({"code": r["id"], "display": r["fields"].get("name"), "target": [{"equivalence": "unmatched",
                       "comment": "The record carries no ISCO-88 code." if not c else f"Code {c} is not an ISCO-88 minor group iHRIS ships."}]})
    cmap("classification-to-isco-88-minor", "iHRIS sample classifications to ISCO-88 minor groups", "classification", "isco_88_minor", el, un,
         "Derived from the iHRIS SAMPLE classification list, whose `code` field holds an ISCO-88 minor group.")
    cad = {r["id"]: r["fields"].get("name") for r in samples("cadre")}
    via = collections.defaultdict(lambda: collections.defaultdict(list))
    for r in jobs:
        cd = (r["fields"].get("cadre") or "").split("|")[-1]
        p = re.match(r"(\d{3})\d-", r["id"])
        if cd in cad and p and p.group(1) in m88:
            via[cd][p.group(1)].append(r["id"])
    el, un = [], []
    for cid_, name in sorted(cad.items()):
        if via[cid_]:
            el.append({"code": cid_, "display": name, "target": [{"code": g, "display": m88[g], "equivalence": "inexact",
                       "comment": f"Sample jobs of this cadre fall in this ISCO-88 minor group: {', '.join(sorted(js))}."} for g, js in sorted(via[cid_].items())]})
        else:
            un.append({"code": cid_, "display": name, "target": [{"equivalence": "unmatched", "comment": "No sample job of this cadre carries an ISCO-88 prefix."}]})
    cmap("cadre-to-isco-88-minor", "iHRIS sample cadres to ISCO-88 minor groups (via jobs)", "cadre", "isco_88_minor", el, un,
         "A cadre is broader than any one occupation group, so each target is `inexact` and lists the sample jobs that justify it. "
         "Derived from SAMPLE data only; a deployment's cadres need their own map.")
    report["isco88to08"] = "not produced: needs the ILO ISCO-88/ISCO-08 correspondence table (not reachable from the building session)"
    return report


def build_iso():
    """ConceptMaps from iHRIS's shipped country and currency lists to ISO 3166-1 / ISO 4217.

    Verified against the Debian iso-codes data packaged by pycountry (version recorded in the
    report): a shipped code that is a CURRENT ISO code maps `equal`; a withdrawn one is `unmatched`,
    naming the withdrawal where iso-codes records it. No successor is ever guessed (ZMK -> ZMW is
    a fact about a redenomination, not about the code, and the source does not state it)."""
    try:
        import pycountry
    except ImportError:
        print("  (pycountry missing: ISO ConceptMaps not built; pip install pycountry==24.6.1)")
        return None
    from importlib.metadata import version
    lists = load_data_lists()
    tdir = os.path.join(OUT, "terminology")
    report = {"verifiedWith": f"pycountry {version('pycountry')} (Debian iso-codes)"}
    cur_c = {c.alpha_2: c for c in pycountry.countries}
    hist_c = {c.alpha_2: c for c in pycountry.historic_countries if hasattr(c, "alpha_2")}
    cur_m = {c.alpha_3: c for c in pycountry.currencies}
    specs = [
        ("country", cur_c, lambda c: c.name, lambda code: (f"Withdrawn from ISO 3166-1; ISO 3166-3 code {hist_c[code].alpha_4}"
                                                           + (f", withdrawn {hist_c[code].withdrawal_date}" if getattr(hist_c[code], "withdrawal_date", None) else "")
                                                           if code in hist_c else "Not an ISO 3166-1 code")),
        ("currency", cur_m, lambda c: c.name, lambda code: "Not a current ISO 4217 code (withdrawn or superseded); no successor is inferred"),
    ]
    for form, current, disp, why in specs:
        iso = ISO_SYSTEMS[form]
        seen, el, un, names = set(), [], [], []
        for r in lists.get(form, []):
            if r["provenance"] != "default" or r["id"] in seen:
                continue
            seen.add(r["id"])
            shipped = r["fields"].get("name")
            if r["id"] in current:
                t = {"code": r["id"], "display": disp(current[r["id"]]), "equivalence": "equal"}
                if shipped and shipped.lower() != disp(current[r["id"]]).lower():
                    t["comment"] = f"iHRIS {RELEASE} ships the older name \"{shipped}\"."
                    names.append({"code": r["id"], "shipped": shipped, "iso": disp(current[r["id"]])})
                el.append({"code": r["id"], "display": shipped, "target": [t]})
            else:
                un.append({"code": r["id"], "display": shipped, "target": [{"equivalence": "unmatched", "comment": why(r["id"])}]})
        write_json(os.path.join(tdir, f"ValueSet-{form}-shipped.json"), {
            "resourceType": "ValueSet", "id": f"ihris-{form}-shipped", "url": f"{CANONICAL}/ValueSet/{form}-shipped", "version": RELEASE,
            "name": f"IHRIS{_pascal(form)}ShippedVS", "title": f"iHRIS {form} list as shipped", "status": "draft", "experimental": True,
            "description": f"Every code of the `{form}` list iHRIS {RELEASE} ships by default: the source side of ConceptMap `{form}-to-{iso['slug']}`.",
            "compose": {"include": [{"system": f"{CANONICAL}/CodeSystem/{form}"}]}})
        cid = f"{form}-to-{iso['slug']}"
        write_json(os.path.join(tdir, f"ConceptMap-{cid}.json"), {
            "resourceType": "ConceptMap", "id": cid, "url": f"{CANONICAL}/ConceptMap/{cid}", "version": RELEASE, "name": _pascal(cid),
            "title": f"iHRIS {form} list to {iso['name']}", "status": "draft", "experimental": True,
            "description": f"The `{form}` codes iHRIS {RELEASE} ships by default, mapped to {iso['name']}. Verified with {report['verifiedWith']}.",
            "sourceUri": f"{CANONICAL}/ValueSet/{form}-shipped", "targetUri": f"{CANONICAL}/ValueSet/{form}",
            "group": [{"source": f"{CANONICAL}/CodeSystem/{form}", "target": iso["system"], "element": el + un}]})
        report[form] = {"system": iso["system"], "shipped": len(seen), "equal": len(el), "notCurrent": [u["code"] for u in un],
                        "currentMissingFromIhris": sorted(set(current) - seen), "olderNames": names}
    return report


def _normalize_zip(path):
    """Rewrite a zip with fixed entry timestamps so the .xlsx is byte-identical across runs."""
    import zipfile
    with zipfile.ZipFile(path) as z:
        items = [(i.filename, z.read(i.filename)) for i in z.infolist()]
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in items:
            if name == "docProps/core.xml":  # openpyxl stamps `modified` with the wall clock on save
                data = re.sub(rb"(<dcterms:modified[^>]*>)[^<]*", rb"\g<1>2026-09-22T00:00:00Z", data)
            zi = zipfile.ZipInfo(name, date_time=(2026, 9, 22, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, data)


def main():
    merged = load_classes()
    fdisp = form_display()
    wiki = wiki_index()
    # form -> class from EVERY module node, across packages: a form is often
    # registered in one package (e.g. gender in ihris-common) on a class another
    # defines (I2CE_SimpleList in i2ce), which a per-package index misses.
    form_to_class = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "src", "*", "modules", RELEASE, "*.json"))):
        mod = json.load(open(f))
        for fm in mod.get("forms", []):
            if isinstance(fm.get("class"), str) and not mod.get("site"):
                form_to_class.setdefault(fm["form"], fm["class"])
    for c, m in merged.items():
        for fm in m["forms"]:
            form_to_class.setdefault(fm, c)
    for sub in ("data-dictionary",):
        d = os.path.join(OUT, sub)
        if os.path.isdir(d):
            for f in glob.glob(os.path.join(d, "*.json")):
                os.remove(f)

    sheets, rows, excluded, scopes = [], [], [], collections.Counter()
    lists_used = collections.defaultdict(set)
    for cls in sorted(merged):
        m = merged[cls]
        sc = scope_of(cls, merged)
        scopes[sc] += 1
        if sc != "record":
            continue
        group = short(cls)
        forms = sorted(m["forms"])
        form_labels = [fdisp.get(x, x) for x in forms]
        elements = []
        for fname_, fl in m["fields"].items():
            t = fl.get("type")
            t = t[0] if isinstance(t, list) else t
            if t in EXCLUDED_TYPES:
                excluded.append({"class": cls, "field": fname_, "type": t, "reason": EXCLUDED_TYPES[t]})
                continue
            dtype, qsub, tnote = TYPE_MAP.get(t, (None, None, f"unmapped I2CE type {t}"))
            refs = fl.get("references") or []
            ref_source = "meta/form" if refs else None
            if not refs and t in ("MAP", "MAP_MULT"):
                # I2CE default: a MAP with no meta/form maps to the form named after the field.
                refs, ref_source = [fname_], "i2ce-default (form named after the field)"
            vsets, lms, unresolved = [], [], []
            for r in refs:
                tc = form_to_class.get(r)
                tsc = scope_of(tc, merged) if tc else None
                if tsc == "list":
                    vsets.append(r)
                    lists_used[r].add(f"{group}.{fname_}")
                elif tsc in ("record", "interoperability"):
                    lms.append(short(tc))
                else:
                    unresolved.append(r)
            label = fl.get("label")
            de = {
                "id": f"{DAK_PREFIX}.{group}.{fname_}",
                "activityId": None,
                "formIds": forms,
                "formDataElementLabel": label,
                "dataElementLabel": label or fname_.replace("_", " "),
                "labelSource": "i2ce-header" if label else "field-name",
                "description": None,
                "descriptionStatus": "to-author",
                "dataType": dtype,
                "quantitySubType": qsub,
                "inputOptions": ([f"{CANONICAL}/ValueSet/{v}" for v in vsets] + [f"{CANONICAL}/StructureDefinition/{x}" for x in lms]) or None,
                "inputOptionsSource": ref_source,
                "calculation": None,
                "optionality": "R" if fl.get("required") else "O",
                "reasonForRequiring": None,
                "explainConditionality": None,
                "duplicates": "Yes" if len(forms) > 1 else "No",
                "functionalGrouping": form_labels[0] if form_labels else group,
                "linkagesToIndicators": None,
                "linkagesToDecisionSupport": None,
                "annotations": "; ".join(x for x in [tnote, ("unique" if fl.get("unique") else None),
                                                     (f"hierarchical selection across lists: {', '.join(vsets)}" if len(vsets) > 1 else None),
                                                     (f"selects a record of: {', '.join(lms)}" if lms else None),
                                                     (f"list form(s) not found in {RELEASE}: {', '.join(unresolved)}" if unresolved else None)] if x) or None,
                "source": {"release": RELEASE, "class": cls, "field": fname_, "i2ceType": t, "definedIn": fl["definedIn"]},
                "evidence": evidence_for(label, wiki),
            }
            elements.append(de)
            rows.append(de)
        sheet = {"$schema": "ihris-dak-data-dictionary/v1", "id": f"{DAK_PREFIX}.{group}", "group": group,
                 "title": form_labels[0] if form_labels else group, "class": cls, "extends": m["extends"],
                 "forms": forms, "instances": sorted({s.split("/")[0] for s in m["sources"]}), "sources": m["sources"],
                 "logicalModel": f"{CANONICAL}/StructureDefinition/{group}", "elements": elements}
        write_json(os.path.join(OUT, "data-dictionary", f"{group}.json"), sheet)
        sheets.append(sheet)

    term = {e["form"]: e for e in build_terminology(sorted(set(lists_used) | {"isco_88_unit", "isco_88_minor"}), form_to_class, fdisp, merged)}
    isco = build_isco(fdisp)
    write_json(os.path.join(OUT, "isco-report.json"), isco)
    iso = build_iso()
    if iso is not None:
        write_json(os.path.join(OUT, "iso-report.json"), iso)
    # value-set catalogue (which list backs which value set, who uses it, what codes ship)
    write_json(os.path.join(OUT, "value-sets.json"), {
        "note": "Each value set is backed by an iHRIS list form. `defaultCodes` ship with the module and are in the ValueSet; "
                "`sampleCodes` come from sample-data modules and live only in example CodeSystems (terminology/).",
        "valueSets": [{"id": f"{DAK_PREFIX}.VS.{f}", "form": f, "class": form_to_class.get(f), "displayName": fdisp.get(f),
                       "canonical": f"{CANONICAL}/ValueSet/{f}", "usedBy": sorted(lists_used.get(f, [])),
                       "defaultCodes": term[f]["default"], "sampleCodes": term[f]["examples"],
                       "status": "shipped" if term[f]["default"] else ("sample-only" if term[f]["examples"] else "deployment-defined")}
                      for f in sorted(term)]})
    write_json(os.path.join(OUT, "excluded.json"), {
        "classesByScope": dict(scopes),
        "excludedClasses": [{"class": c, "scope": scope_of(c, merged)} for c in sorted(merged) if scope_of(c, merged) not in ("record",)],
        "excludedFields": excluded})

    cols = [("Data element ID", "id"), ("Activity ID", "activityId"), ("Form ID", "formIds"),
            ("Form data element label", "formDataElementLabel"), ("Data element label", "dataElementLabel"),
            ("Description and definition", "description"), ("Data type", "dataType"), ("Input options", "inputOptions"),
            ("Quantity sub-type", "quantitySubType"), ("Calculation", "calculation"), ("Optionality", "optionality"),
            ("Reason for requiring data", "reasonForRequiring"), ("Explain conditionality", "explainConditionality"),
            ("Duplicates", "duplicates"), ("Functional grouping", "functionalGrouping"),
            ("Linkages to aggregate indicators", "linkagesToIndicators"), ("Linkages to decision support tables", "linkagesToDecisionSupport"),
            ("Annotations", "annotations"), ("Source (iHRIS 4.3.3)", None)]

    def cell(r, k):
        if k is None:
            s = r["source"]
            return f"{s['class']}.{s['field']} ({s['i2ceType']})"
        v = r[k]
        return "; ".join(v) if isinstance(v, list) else ("" if v is None else v)

    with open(os.path.join(OUT, "data-dictionary.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([c for c, _ in cols])
        for r in rows:
            w.writerow([cell(r, k) for _, k in cols])
    try:
        import openpyxl
        from openpyxl.styles import Font
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Data dictionary"
        ws.append([c for c, _ in cols])
        for c in ws[1]:
            c.font = Font(bold=True)
        for r in rows:
            ws.append([cell(r, k) for _, k in cols])
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        vs = wb.create_sheet("Value sets")
        vs.append(["Value set ID", "iHRIS list form", "Class", "Display name", "Used by", "Default codes", "Sample codes", "Status"])
        for c in vs[1]:
            c.font = Font(bold=True)
        for f_ in sorted(term):
            e = term[f_]
            vs.append([f"{DAK_PREFIX}.VS.{f_}", f_, form_to_class.get(f_), fdisp.get(f_), "; ".join(sorted(lists_used.get(f_, []))),
                       e["default"], sum(e["examples"].values()),
                       "shipped" if e["default"] else ("sample-only" if e["examples"] else "deployment-defined")])
        cs_ws = wb.create_sheet("Codes")
        cs_ws.append(["Value set ID", "Code", "Display", "Provenance", "Module"])
        for c in cs_ws[1]:
            c.font = Font(bold=True)
        for f_ in sorted(term):
            for path in sorted(glob.glob(os.path.join(OUT, "terminology", f"CodeSystem-{f_}.json")) +
                               glob.glob(os.path.join(OUT, "terminology", f"CodeSystem-{f_}-example-*.json"))):
                cs = json.load(open(path))
                prov = "sample" if cs["content"] == "example" else "default"
                for c in cs.get("concept", []):
                    cs_ws.append([f"{DAK_PREFIX}.VS.{f_}", c["code"], c["display"], prov, cs["title"]])
        wb.properties.creator = "src/tools/build_dak.py"
        wb.properties.created = wb.properties.modified = __import__("datetime").datetime(2026, 9, 22)
        xp = os.path.join(OUT, "data-dictionary.xlsx")
        wb.save(xp)
        _normalize_zip(xp)
    except ImportError:
        print("  (openpyxl missing: no .xlsx written)")

    types = collections.Counter(r["dataType"] for r in rows)
    opt = collections.Counter(r["optionality"] for r in rows)
    ev = sum(1 for r in rows if r["evidence"])
    L = ["# iHRIS DAK data dictionary (derived from iHRIS 4.3.3)\n",
         "*Generated by `src/tools/build_dak.py`. Do not edit by hand.*\n",
         f"{len(rows)} data elements in {len(sheets)} logical models; {len(lists_used)} value sets; "
         f"{len(excluded)} fields excluded by type. {ev} elements have wiki evidence to author a description from.\n",
         "| data type | count |", "|---|---|"] + [f"| {k} | {v} |" for k, v in types.most_common()] + [
         "", f"Optionality: {dict(opt)}. Classes by scope: {dict(scopes)}.\n", "## Logical models\n",
         "| group | title | class | instances | elements | required |", "|---|---|---|---|---|---|"]
    for s in sheets:
        L.append(f"| [`{s['group']}`](../../src/ihris-dak/data-dictionary/{s['group']}.json) | {s['title']} | `{s['class']}` | "
                 f"{', '.join(s['instances'])} | {len(s['elements'])} | {sum(1 for e in s['elements'] if e['optionality'] == 'R')} |")
    with open(os.path.join(ROOT, "docs", "generated", "dak-data-dictionary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(json.dumps({"elements": len(rows), "logicalModels": len(sheets), "valueSets": len(lists_used), "excludedFields": len(excluded),
                      "scopes": dict(scopes), "types": dict(types), "optionality": dict(opt), "withEvidence": ev,
                      "unmapped": sorted({r["source"]["i2ceType"] for r in rows if r["dataType"] is None})}, indent=1))


if __name__ == "__main__":
    main()
