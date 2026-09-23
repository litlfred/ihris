# iHRIS 4 on FHIR (`ihris-4-on-fhir`)

**New derived content** (owner, 2026-09-23): the iHRIS 4.3.3 data model expressed in FHIR, derived from `src/ihris-data-dictionary` (the data dictionary and terminology).

**This is the one subgraph that depends on smart-base**: the smart-base harness and the `smart.who.int.base` IG. The ihris root and its other instances are independent of smart-base.

| status | item |
|---|---|
| documented, not run | skill [`ihris-4-on-fhir`](../skills/ihris-4-on-fhir.md), process [`processes/ihris-4-on-fhir.bpmn`](../../processes/ihris-4-on-fhir.bpmn), Tool `ihris-sushi` |
| later (owner: "do sushi later") | F1: pinned SUSHI and skeleton (bean `ihris-dipr`); F2: terminology as FSH (`ihris-ej94`) |
| blocked on folio-assistant `cz17` | logical models (`ihris-ct58`) |
| blocked on the logical models | StructureMaps to the three iHRIS 5 IGs (`ihris-7gl8`) |
| blocked on the lightweight IG render pipeline | render and publication (`ihris-bwls`) |

Design: [`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md).
