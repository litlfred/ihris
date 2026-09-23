---
# ihris-dmgf
title: 'DESIGN STRATEGY: how the iHRIS DAK becomes FHIR — for owner review'
status: completed
type: task
priority: normal
tags:
    - fhir
    - needs-owner
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-09-23T06:28:07Z
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

## Draft

[`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md), 2026-09-23: decisions D1 to D8, each with a recommendation, and phases F0 to F5. Awaiting the owner's review. Nothing in it is decided.

## Completed by the owner, 2026-09-23

Approved with the decisions in the doc's §0. iHRIS is independent of smart-base.
