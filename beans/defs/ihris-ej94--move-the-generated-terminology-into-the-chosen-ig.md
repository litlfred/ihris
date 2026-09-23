---
# ihris-ej94
title: Move the generated terminology into the chosen IG build
status: draft
type: task
tags:
    - fhir
    - paused
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-09-23T06:04:45Z
parent: ihris-g768
blocked_by:
    - ihris-dmgf
---

44 CS / 57 VS / 5 CM in `src/ihris-dak/terminology` are JSON from build_dak.py. Once the design says FSH/sushi, generate them there instead and retire the JSON path; until then they are unchanged.
