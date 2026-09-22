#!/usr/bin/env python3
"""Validate src/ihris-dak/terminology/*.json as FHIR R4 resources (fhir.resources 6.5 = R4).

fhir.resources 6.x needs pydantic<2, so it runs from its own virtualenv:
  python3 -m venv .build/fhir-venv && .build/fhir-venv/bin/pip install "fhir.resources==6.5.0" "pydantic<2"
validate.py calls this with that interpreter when it exists. Also checks that
every ValueSet.compose system and every Coding property system resolves to a
CodeSystem generated here.
"""
import glob
import json
import os
import sys

from fhir.resources.codesystem import CodeSystem
from fhir.resources.valueset import ValueSet

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
files = sorted(glob.glob(os.path.join(ROOT, "src/ihris-dak/terminology/*.json")))
docs = {f: json.load(open(f)) for f in files}
urls = {d["url"] for d in docs.values() if d["resourceType"] == "CodeSystem"}
errs, n = [], {"CodeSystem": 0, "ValueSet": 0}
for f, d in docs.items():
    try:
        (CodeSystem if d["resourceType"] == "CodeSystem" else ValueSet).parse_obj(d)
        n[d["resourceType"]] += 1
    except Exception as e:  # noqa: BLE001 - report every structural failure
        errs.append(f"{os.path.relpath(f, ROOT)}: {str(e)[:300]}")
    for inc in d.get("compose", {}).get("include", []):
        if inc.get("system") not in urls:
            errs.append(f"{os.path.relpath(f, ROOT)}: include system {inc.get('system')} is not a generated CodeSystem")
    for c in d.get("concept", []):
        for p in c.get("property", []):
            if "valueCoding" in p and p["valueCoding"]["system"] not in urls:
                errs.append(f"{os.path.relpath(f, ROOT)}: {c['code']}.{p['code']} -> {p['valueCoding']['system']} has no CodeSystem")
print(f"FHIR R4: {n}; {len(errs)} error(s)")
print("\n".join(errs[:40]))
sys.exit(1 if errs else 0)
