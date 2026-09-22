#!/usr/bin/env python3
"""Validate every generated node against its declared schema.

- ihris-* records: against the JSON Schemas in src/schemas/ (jsonschema, pip).
- folio-catalogue-node/v1 and folio-catalogue/v1: against folio-assistant's own
  zod schemas, by running src/tools/validate-folio.ts with bun, when a
  folio-assistant checkout is available (FOLIO_ASSISTANT=<path>, default
  ../litlfred/folio-assistant). Skipped with a warning otherwise, never passed.

Also checks every metadataRef resolves, and every module's parent/formClasses
ids resolve. Exit status is non-zero on any failure.
"""
import glob
import json
import os
import subprocess
import sys

import jsonschema

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCHEMAS = {}
for f in glob.glob(os.path.join(ROOT, "src/schemas/*.schema.json")):
    s = json.load(open(f))
    SCHEMAS[s["title"]] = jsonschema.Draft202012Validator(s, format_checker=jsonschema.FormatChecker())

errors, counts, ids = [], {}, set()
files = [f for f in glob.glob(os.path.join(ROOT, "src/**/*.json"), recursive=True) + glob.glob(os.path.join(ROOT, "library/**/*.json"), recursive=True)
         if "/schemas/" not in f and "/inventory/" not in f]
docs = {}
for f in files:
    try:
        d = json.load(open(f))
    except ValueError as e:
        errors.append(f"{f}: invalid JSON: {e}")
        continue
    if not isinstance(d, dict) or "$schema" not in d:
        continue
    docs[f] = d
    tag = d["$schema"]
    counts[tag] = counts.get(tag, 0) + 1
    if "id" in d:
        ids.add(d["id"])
    if tag in SCHEMAS:
        for e in SCHEMAS[tag].iter_errors(d):
            errors.append(f"{os.path.relpath(f, ROOT)}: {'/'.join(map(str, e.path))}: {e.message[:200]}")

for f, d in docs.items():
    if d["$schema"] == "folio-catalogue-node/v1" and d.get("metadataRef"):
        target = os.path.join(os.path.dirname(os.path.dirname(f)), d["metadataRef"])
        if not os.path.exists(target):
            errors.append(f"{os.path.relpath(f, ROOT)}: metadataRef {d['metadataRef']} does not resolve")
    if d["$schema"] == "ihris-i2ce-module/v1":
        for ref in [d.get("parent")] + d.get("formClasses", []):
            if ref and ref not in ids:
                errors.append(f"{os.path.relpath(f, ROOT)}: reference {ref} does not resolve")
        if not os.path.exists(os.path.join(ROOT, d["source"]["releaseFile"])):
            errors.append(f"{os.path.relpath(f, ROOT)}: source.releaseFile {d['source']['releaseFile']} does not resolve")

fa = os.environ.get("FOLIO_ASSISTANT", os.path.join(ROOT, "..", "litlfred", "folio-assistant"))
if os.path.isdir(os.path.join(fa, "folio-assistant-core")):
    r = subprocess.run(["bun", "run", os.path.join(ROOT, "src/tools/validate-folio.ts"), ROOT], cwd=fa, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        errors.append("folio-assistant zod validation failed:\n" + (r.stdout + r.stderr)[-3000:])
else:
    print(f"WARNING: no folio-assistant checkout at {fa}; folio-catalogue(-node)/v1 NOT validated")

print(json.dumps(counts, indent=1))
if errors:
    print(f"{len(errors)} error(s):")
    print("\n".join(errors[:80]))
    sys.exit(1)
print("OK")
