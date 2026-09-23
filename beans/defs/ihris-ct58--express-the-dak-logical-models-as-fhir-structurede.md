---
# ihris-ct58
title: Express the DAK logical models as FHIR StructureDefinitions (FSH), sushi-clean
status: draft
type: task
priority: normal
tags:
    - fhir
    - paused
    - blocked-upstream
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-09-23T06:23:09Z
parent: ihris-g768
blocked_by:
    - ihris-dmgf
---

Turn `src/ihris-dak/data-dictionary` into FHIR logical models. Format depends on the design decision (smart-base DAK Logical Model, folio-assistant cz17). Sushi must run without error before any commit.

## Owner decision D3 (2026-09-23)

Wait for smart-base's DAK model: [folio-assistant cz17](https://github.com/litlfred/folio-assistant/blob/main/beans/defs/folio-assistant-cz17--migrate-dakjson-in-the-dak-type-is-ours-and-its-lo.md). This is blocked upstream in addition to the gate.
