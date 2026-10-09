---
name: ihris-4-on-fhir
description: >
  Express the iHRIS 4 data model in FHIR, as the derived subgraph
  src/ihris-4-on-fhir: generate FSH from the data dictionary and terminology,
  build with SUSHI, validate, and map to iHRIS 5 with StructureMaps. It is
  built on fhir-harness (the bare FHIR IG pipeline); R4 core is its only IG
  dependency. F1 to F3 are built (owner, 2026-10-09: "all"). Process: processes/ihris-4-on-fhir.bpmn.
input: src/schemas/skills/ihris-4-on-fhir/input.schema.json
output: src/schemas/skills/ihris-4-on-fhir/output.schema.json
---

# iHRIS 4 on FHIR

Design and owner decisions: [`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md) §0. This skill is the operating order.

## Rules

- **Generated only.** Python writes FSH from `src/ihris-data-dictionary/` into `src/ihris-4-on-fhir/`. Nobody edits the FSH or the SUSHI output.
- **SUSHI must run clean** (Tool `ihris-sushi`, version pinned at F1) before any commit that contains FSH.
- **Derived never invents.** An element carries only what the data dictionary states. Definitions, conditionality and linkages stay empty until authored in `src/ihris-data-dictionary/authored/`.
- **Built on fhir-harness, independent of smart-base** (owner, 2026-10-09). The pipeline is fhir-harness's (skills `ig-build-pipeline`, `ig-publication`, `fhir-validation`); nothing here takes a smart-base type or dependency, and the IG depends on `hl7.fhir.r4.core#4.0.1` only.
- **No IG Publisher and no HTML** until folio-assistant's lightweight IG render pipeline is done (bean `ihris-bwls`).

## Steps, and where each one stands

| step | Tool | state |
|---|---|---|
| F1: pin SUSHI; create `sushi-config.yaml` (canonical, FHIR 4.0.1, `hl7.fhir.r4.core` only) | `ihris-gen-fsh`, `ihris-sushi` | done |
| F2: terminology as FSH; content-equal to today's JSON; then retire the JSON | `ihris-build-dak`, `ihris-gen-fsh` | done: the JSON is SUSHI's build |
| F3: logical models | `ihris-gen-fsh` | done: 51, SUSHI clean |
| F4: StructureMaps to `ig/`, `ihris-backend-site/ig` and `qualify-ig` | the generator, `ihris-sushi` | next (owner, 2026-10-09: "all") |
| F5: render and publication | the platform pipeline | blocked on `ihris-bwls` |
