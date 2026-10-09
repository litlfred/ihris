# iHRIS 4 on FHIR (`ihris-4-on-fhir`)

**New derived content** (owner, 2026-09-23): the iHRIS 4.3.3 data model expressed in FHIR, derived from `src/ihris-data-dictionary` (the data dictionary and terminology).

**Built on [fhir-harness](https://github.com/litlfred/fhir-harness)**, the bare FHIR IG pipeline with no WHO in it (owner, 2026-10-09). It replaced the smart-base harness and IG this subgraph depended on from 2026-09-23, so nothing in this folio depends on smart-base. The IG depends on `hl7.fhir.r4.core#4.0.1` only (D5).

| status | item |
|---|---|
| documented, not run | skill [`ihris-4-on-fhir`](../skills/ihris-4-on-fhir.md), process [`processes/ihris-4-on-fhir.bpmn`](../../processes/ihris-4-on-fhir.bpmn), Tool `ihris-sushi` |
| later (owner: "do sushi later") | F1: pinned SUSHI and skeleton (bean `ihris-dipr`); F2: terminology as FSH (`ihris-ej94`) |
| blocked on folio-assistant `cz17` | logical models (`ihris-ct58`) |
| blocked on the logical models | StructureMaps to the three iHRIS 5 IGs (`ihris-7gl8`) |
| blocked on the lightweight IG render pipeline | render and publication (`ihris-bwls`) |

Design: [`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md).
