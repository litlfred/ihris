---
# ihris-ej94
title: Move the generated terminology into the chosen IG build
status: todo
type: task
priority: normal
tags:
    - fhir
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-09-23T06:28:07Z
parent: ihris-g768
blocked_by:
    - ihris-dipr
---

44 CS / 57 VS / 5 CM in `src/ihris-dak/terminology` are JSON from build_dak.py. Once the design says FSH/sushi, generate them there instead and retire the JSON path; until then they are unchanged.

## Owner decisions D5, D7 and D8 (2026-09-23)

R4 core only; sushi and validation only; the JSON is retired once the sushi output is equal in content. This can proceed as soon as the gate is completed.
