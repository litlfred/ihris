#!/usr/bin/env python3
"""Derive a WHO SMART Guidelines DAK (L2) data dictionary from the iHRIS data model.

Input : src/<instance>/data-model/<release>/*.json   (ihris-form-class/v1, from build_kg.py)
        library/ihris-wiki/osi-help-<release>/sections/*.md (evidence only)
Output: src/ihris-dak/data-dictionary/<group>.json   (ihris-dak-data-dictionary/v1)
        src/ihris-dak/core-data-elements/*.json      (smart-base CoreDataElement)
        src/ihris-dak/data-dictionary.csv / .xlsx    (WHO column order)
        docs/generated/dak-data-dictionary.md

What this does NOT do, on purpose:
- It never writes a description. The source has none per field, and a guessed
  definition would look authoritative. `description` stays null with
  `descriptionStatus: "to-author"`; wiki passages that mention the label are
  attached as `evidence` for whoever authors it.
- It never infers conditionality, indicator linkages or decision-table
  linkages. Those columns are left empty for a human, as the WHO guide intends.

Column semantics follow the "Form data mapping guide" in WHO's Digital
transformation handbook for primary health care (9789240093362, pp. 86-90),
held in folio-assistant's smart-base library.
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
    for sub in ("data-dictionary", "core-data-elements"):
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
        write_json(os.path.join(OUT, "core-data-elements", f"LM-{group}.json"), {
            "resourceType": "CoreDataElement", "type": "logicalmodel", "id": f"{DAK_PREFIX}.{group}",
            "canonical": f"{CANONICAL}/StructureDefinition/{group}"})

    for form in sorted(lists_used):
        cls = form_to_class[form]
        write_json(os.path.join(OUT, "core-data-elements", f"VS-{form}.json"), {
            "resourceType": "CoreDataElement", "type": "valueset", "id": f"{DAK_PREFIX}.VS.{form}",
            "canonical": f"{CANONICAL}/ValueSet/{form}"})

    # value-set catalogue (which list backs which value set, and who uses it)
    write_json(os.path.join(OUT, "value-sets.json"), {
        "note": "Each value set is backed by an iHRIS list form. Codes are not yet extracted from the shipped formsData; see README.",
        "valueSets": [{"id": f"{DAK_PREFIX}.VS.{f}", "form": f, "class": form_to_class[f], "displayName": fdisp.get(f),
                       "canonical": f"{CANONICAL}/ValueSet/{f}", "usedBy": sorted(u)} for f, u in sorted(lists_used.items())]})
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
        vs.append(["Value set ID", "iHRIS list form", "Class", "Display name", "Used by"])
        for c in vs[1]:
            c.font = Font(bold=True)
        for f_, u in sorted(lists_used.items()):
            vs.append([f"{DAK_PREFIX}.VS.{f_}", f_, form_to_class[f_], fdisp.get(f_), "; ".join(sorted(u))])
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
