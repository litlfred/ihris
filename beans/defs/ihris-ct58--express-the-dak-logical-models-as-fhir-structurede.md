---
# ihris-ct58
title: Express the DAK logical models as FHIR StructureDefinitions (FSH), sushi-clean
status: completed
type: task
priority: normal
tags:
    - fhir
    - paused
    - blocked-upstream
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-10-09T18:00:00Z
parent: ihris-g768
blocked_by:
    - ihris-dmgf
---

Turn `src/ihris-data-dictionary/data-dictionary` into FHIR logical models. Format depends on the design decision (smart-base DAK Logical Model, folio-assistant cz17). Sushi must run without error before any commit.

## Owner decision D3 (2026-09-23)

Wait for smart-base's DAK model: [folio-assistant cz17](https://github.com/litlfred/folio-assistant/blob/main/beans/defs/folio-assistant-cz17--migrate-dakjson-in-the-dak-type-is-ours-and-its-lo.md). This is blocked upstream in addition to the gate.

## Open after the independence ruling (2026-09-23)

D3 said to wait for folio-assistant cz17, which is smart-base's DAK model. iHRIS is now independent of smart-base, so whether to keep waiting is for the owner to decide.

## Done (2026-10-09)

Unblocked by the owner (2026-10-09, asked which iHRIS 5 FHIR work to do: "all"), so logical models no longer wait for folio-assistant cz17 (D3 superseded). src/tools/gen_fsh.py writes one FSH Logical per data-dictionary sheet (51): FHIR type from the I2CE field type, cardinality from optionality and duplicates, an extensible binding to the field's ValueSet, and a Mapping to each I2CE field name (elements are camelCase, eld-20). SUSHI clean. Element definitions are not written (the source has none); SUSHI repeats the short label as `definition`, as it does for any element without one.
