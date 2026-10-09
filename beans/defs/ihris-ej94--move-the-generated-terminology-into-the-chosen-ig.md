---
# ihris-ej94
title: Move the generated terminology into the chosen IG build
status: completed
type: task
priority: normal
tags:
    - fhir
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-10-09T18:00:00Z
parent: ihris-g768
blocked_by:
    - ihris-dipr
---

44 CS / 57 VS / 5 CM in `src/ihris-data-dictionary/terminology` are JSON from build_dak.py. Once the design says FSH/sushi, generate them there instead and retire the JSON path; until then they are unchanged.

## Owner decisions D5, D7 and D8 (2026-09-23)

R4 core only; sushi and validation only; the JSON is retired once the sushi output is equal in content. This can proceed as soon as the gate is completed.

## Done (2026-10-09)

F2 and the D8 switch. build_dak.py writes the terminology as FSH (one Instance per resource, src/ihris-4-on-fhir/input/fsh/terminology/); gen_fsh.py runs SUSHI and writes src/ihris-data-dictionary/terminology/*.json from its build. Before the switch, SUSHI's build of FSH generated from the JSON was shown equal to all 106 resources; since, `gen_fsh.py --check` holds the committed JSON to SUSHI's build. Every reader of the JSON is unchanged.
