---
# ihris-dipr
title: 'F1: pinned SUSHI and an empty R4-core IG skeleton, sushi-clean'
status: completed
type: task
tags:
    - fhir
created_at: 2026-09-23T06:28:07Z
updated_at: 2026-10-09T18:00:00Z
parent: ihris-g768
---

Design phase F1 (`docs/design/fhir-strategy.md`).
- Pin a SUSHI version.
- Add `sushi-config.yaml` with canonical `https://litlfred.github.io/ihris/dak`, FHIR 4.0.1, and dependencies on R4 core only (no smart-base).
- `validate.py` runs sushi and fails on any error.

Exit: sushi reports 0 errors and 0 warnings. No IG Publisher run and no HTML (D7).

## Done (2026-10-09)

src/ihris-4-on-fhir/sushi-config.yaml (R4 core only, FSHOnly), SUSHI pinned at fsh-sushi 3.20.1 in CI, and validate.py runs `src/tools/gen_fsh.py --check`, which fails unless SUSHI reports 0 errors and 0 warnings.
