#!/usr/bin/env python3
"""Validate every generated node against its declared schema.

- ihris-* records: against the JSON Schemas in src/schemas/ (jsonschema, pip).
- folio-catalogue-node/v1, folio-catalogue/v1 and folio-glossary/v1: against folio-assistant's own
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

# Files with no $schema tag are bound to a schema by path (src/schemas/bindings.json),
# instance declarations get the extension schema for the keys folio-assistant's zod drops,
# and every JSON file in the repository must be covered by SOMETHING.
import fnmatch
BIND = json.load(open(os.path.join(ROOT, "src/schemas/bindings.json")))
FOLIO_TAGS = {"folio-catalogue/v1", "folio-catalogue-node/v1", "folio-document-images/v1", "folio-glossary/v1"}  # zod: validate-folio.ts


def _match(rel, pattern):
    return fnmatch.fnmatchcase(rel, pattern) or ("**/" in pattern and fnmatch.fnmatchcase(rel, pattern.replace("**/", "")))


def _check(rel, tag, doc):
    if tag not in SCHEMAS:
        errors.append(f"{rel}: bound to {tag}, which src/schemas does not define")
        return
    counts[tag] = counts.get(tag, 0) + 1
    for e in SCHEMAS[tag].iter_errors(doc):
        errors.append(f"{rel}: {tag}: {'/'.join(map(str, e.path))} {e.message[:200]}")


decl_root = json.load(open(os.path.join(ROOT, "ihris.json")))
declarations = ["ihris.json"] + [f"{i['path']}/{i['name']}.json" for i in decl_root["instances"]]
for rel in declarations:
    _check(rel, BIND["declarations"]["schema"], json.load(open(os.path.join(ROOT, rel))))

elsewhere = [g for k, gs in BIND["coveredElsewhere"].items() if not k.startswith("_") for g in gs]
uncovered = []
SKIP = ("node_modules/", "uploads/", ".build/", "_site/", ".git/", "src/schemas/")
for path in sorted(glob.glob(os.path.join(ROOT, "**/*.json"), recursive=True)):
    rel = os.path.relpath(path, ROOT)
    if rel.startswith(SKIP):
        continue
    try:
        doc = json.load(open(path))
    except ValueError:
        continue  # reported above for src/ and library/
    tag = doc.get("$schema") if isinstance(doc, dict) else None
    if tag in SCHEMAS or tag in FOLIO_TAGS or rel in declarations or any(_match(rel, g) for g in elsewhere):
        continue
    hit = [b for b in BIND["bindings"] if _match(rel, b["glob"])
           and all(isinstance(doc, dict) and doc.get(k) == v for k, v in b.get("when", {}).items())]
    if hit:
        _check(rel, hit[0]["schema"], doc)
    else:
        uncovered.append(rel)
for rel in uncovered:
    errors.append(f"{rel}: no schema covers this file (add a $schema tag or a binding in src/schemas/bindings.json)")
counts["json files with no schema"] = len(uncovered)

# Semantic QA for every schema and node type (src/tools/qa.py). A schema with no QA
# check is itself a finding (qa-missing): missing QA is a QA failure.
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("qa", os.path.join(ROOT, "src/tools/qa.py"))
_qa = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_qa)
_findings, _coverage = _qa.run()
errors += [f"qa: {x}" for x in _findings]
counts["qa schemas covered"] = sum(1 for c in _coverage if c["checks"])
counts["qa checks"] = sum(len(c["checks"]) for c in _coverage)

# Generated BPMN must match its spec (src/tools/gen_bpmn.py).
r = subprocess.run([sys.executable, os.path.join(ROOT, "src/tools/gen_bpmn.py"), "--check"], capture_output=True, text=True)
if r.returncode != 0:
    errors.append("processes: " + (r.stdout + r.stderr).strip())
counts["bpmn process"] = len(glob.glob(os.path.join(ROOT, "processes", "*.bpmn")))

# The glossary is generated from committed inputs (src/tools/build_glossary.py) and must be current.
r = subprocess.run([sys.executable, os.path.join(ROOT, "src/tools/build_glossary.py"), "--check"], capture_output=True, text=True)
if r.returncode != 0:
    errors.append("glossary: " + (r.stdout + r.stderr).strip()[-2000:])
counts["glossary scheme"] = len(glob.glob(os.path.join(ROOT, "glossary", "*.glossary.json")))

# The site theme is derived from the verified release (src/tools/extract_theme.py), and the
# site must build with every internal link resolving (src/tools/build_site.py).
r = subprocess.run([sys.executable, os.path.join(ROOT, "src/tools/extract_theme.py"), "--check"], capture_output=True, text=True)
sys.stderr.write(r.stderr)
if r.returncode != 0:
    errors.append("site theme: " + (r.stdout + r.stderr).strip())
r = subprocess.run([sys.executable, os.path.join(ROOT, "src/tools/build_site.py"), "--out", ".build/site", "--check-links"],
                   capture_output=True, text=True)
if r.returncode != 0:
    errors.append("site: " + (r.stdout + r.stderr).strip()[-2000:])
counts["site page"] = sum(1 for _, _, fs in os.walk(os.path.join(ROOT, ".build", "site")) for f in fs if f.endswith(".html"))

fa = os.environ.get("FOLIO_ASSISTANT", os.path.join(ROOT, "..", "litlfred", "folio-assistant"))

if os.path.isdir(os.path.join(fa, "folio-assistant-core")):
    sys.path.insert(0, os.path.join(ROOT, "src", "tools"))
    import build_glossary  # the instance namespace, one answer: validate-folio.ts compares its SKOS with core's toSkos
    r = subprocess.run(["bun", "run", os.path.join(ROOT, "src/tools/validate-folio.ts"), ROOT, build_glossary.NS], cwd=fa,
                       capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.returncode != 0:
        errors.append("folio-assistant zod validation failed:\n" + (r.stdout + r.stderr)[-3000:])
else:
    print(f"WARNING: no folio-assistant checkout at {fa}; folio-catalogue(-node)/v1 NOT validated")
    if os.environ.get("CI"):  # a skipped check is not a pass, and CI must not report one as such
        errors.append(f"CI: no folio-assistant checkout at {fa}, so the zod checks did not run")

# FHIR R4 structure of the generated terminology, with fhir.resources in its own venv (needs pydantic<2).
venv_py = os.path.join(ROOT, ".build", "fhir-venv", "bin", "python")
if glob.glob(os.path.join(ROOT, "src/ihris-data-dictionary/terminology/*.json")):
    if os.path.exists(venv_py):
        r = subprocess.run([venv_py, os.path.join(ROOT, "src/tools/validate_fhir.py")], capture_output=True, text=True)
        sys.stdout.write(r.stdout)
        if r.returncode != 0:
            errors.append("FHIR R4 validation failed:\n" + (r.stdout + r.stderr)[-3000:])
    else:
        print("WARNING: .build/fhir-venv missing; FHIR terminology NOT validated (see src/tools/validate_fhir.py)")
        if os.environ.get("CI"):
            errors.append("CI: .build/fhir-venv missing, so FHIR R4 validation did not run")

print(json.dumps(counts, indent=1))
if errors:
    print(f"{len(errors)} error(s):")
    print("\n".join(errors[:80]))
    sys.exit(1)
print("OK")
