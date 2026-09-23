---
# ihris-dmgf
title: 'DESIGN STRATEGY: how the iHRIS DAK becomes FHIR — for owner review'
status: draft
type: task
tags:
    - fhir
    - needs-owner
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-09-23T06:04:45Z
parent: ihris-g768
---

The gate. Everything else under the epic is blocked by this bean. Only the owner completes it.

## Questions the strategy must answer

1. **Source format.** Keep generating FHIR JSON from Python, or author/generate FSH and make sushi the build (per the owner's rule: sushi must run clean before commit)?
2. **Where the IG lives.** A DAK IG in this repo (`src/ihris-dak`), contributions to `iHRIS/iHRIS` (the iHRIS 5 IG, canonical `http://ihris.org/fhir`), or both.
3. **Canonical URL.** Provisional `https://litlfred.github.io/ihris/dak` is unconfirmed.
4. **Logical model format.** Follow smart-base's DAK Logical Model once upstream settles (folio-assistant cz17), or define one now.
5. **Layering.** Bare FHIR IG base with DAK/SMART overlays (folio-assistant nsbb), and which pipeline phase (kn0t) this folio targets.
6. **Relationship to iHRIS 5.** Is iHRIS 5's IG the implementation the DAK is checked against, a migration target, or both?
