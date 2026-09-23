---
name: ihris-4-on-fhir
description: >
  Express the iHRIS 4 data model in FHIR, as the derived subgraph
  src/ihris-4-on-fhir: generate FSH from the data dictionary and terminology,
  build with SUSHI, validate, and map to iHRIS 5 with StructureMaps. It depends
  on the smart-base harness and IG. Documented now; SUSHI runs later (owner,
  2026-09-23). Process: processes/ihris-4-on-fhir.bpmn.
---

# iHRIS 4 on FHIR

Design and owner decisions: [`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md) §0. This skill is the operating order.

## Rules

- **Generated only.** Python writes FSH from `src/ihris-dak/` into `src/ihris-4-on-fhir/`. Nobody edits the FSH or the SUSHI output.
- **SUSHI must run clean** (Tool `ihris-sushi`, version pinned at F1) before any commit that contains FSH.
- **Derived never invents.** An element carries only what the data dictionary states. Definitions, conditionality and linkages stay empty until authored in `src/ihris-dak/authored/`.
- **Only this subgraph depends on smart-base.** Nothing outside `src/ihris-4-on-fhir/` may take a smart-base type or dependency.
- **No IG Publisher and no HTML** until folio-assistant's lightweight IG render pipeline is done (bean `ihris-bwls`).

## Steps, and where each one stands

| step | Tool | state |
|---|---|---|
| F1: pin SUSHI; create `sushi-config.yaml` (canonical, FHIR 4.0.1, the smart-base IG dependency) | `ihris-sushi` | later |
| F2: terminology as FSH; content-equal to today's JSON; then retire the JSON | `ihris-build-dak`, `ihris-sushi` | later |
| F3: logical models | the generator, `ihris-sushi` | blocked on `cz17` |
| F4: StructureMaps to `ig/`, `ihris-backend-site/ig` and `qualify-ig` | the generator, `ihris-sushi` | blocked on F3 |
| F5: render and publication | the platform pipeline | blocked on `ihris-bwls` |
