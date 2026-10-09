---
# ihris-p1qg
title: 'iHRIS 5 IG: file the five drafted upstream defects on iHRIS/iHRIS'
status: in-progress
type: task
tags:
    - fhir
    - upstream
created_at: 2026-10-09T19:49:36Z
updated_at: 2026-10-09T19:49:36Z
parent: ihris-g768
---

Drafts in `docs/upstream/ihris5-ig-defects.md`, found building the three iHRIS 5 IGs with SUSHI 3.20.1 at iHRIS/iHRIS@fa66e9b (master, 2026-10-09):
1. IhrisRolePrimary sets ^context[1] with no context[0]; the IG Publisher cannot parse it (the one defect patched here: src/ihris5/ig-build-patches.json).
2. qualify-ig references IhrisFacility and IhrisJurisdiction, defined only in the manage IG (2 SUSHI errors).
3. The three IGs share canonical http://ihris.org/fhir and package ihris#0.1.0, yet define different content at 7 canonical URLs (ihris-practitioner, ...).
4. Duplicate FSH names (IhrisRole, IhrisJob, ...) make by-name references ambiguous.
5. ValueSet name Iso3166-1-2 is not computable.
Owner, 2026-10-09: "take iHRIS 5 defects upstream". This session cannot attach iHRIS/iHRIS (a checkout-name collision with litlfred/ihris), so a separate session files them. Record each issue's URL here; when the pin moves past a fix, delete its patch.
