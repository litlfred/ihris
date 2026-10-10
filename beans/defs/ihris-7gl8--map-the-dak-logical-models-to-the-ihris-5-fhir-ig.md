---
# ihris-7gl8
title: Map the DAK logical models to the iHRIS 5 FHIR IG
status: in-progress
type: task
priority: normal
tags:
    - fhir
created_at: 2026-09-23T06:04:45Z
updated_at: 2026-10-09T23:00:00Z
parent: ihris-g768
blocked_by:
    - ihris-dmgf
    - ihris-ct58
---

Crosswalk each of the 49 logical models / 242 data elements (from iHRIS 4.3.3 form classes) to the iHRIS 5 profile, element or extension that holds it, e.g. Person→IhrisPractitioner, PersonPosition→IhrisPractitionerRole, Education→IhrisBasicEducationHistory, License→IhrisBasicLicense, Salary→IhrisBasicSalary. Output: ConceptMap(s) or a mapping table, plus a two-way gap report. Needs the iHRIS 5 FSH content (LGPL; only names are inventoried now). Uncertain matches go in `authored/` as proposals.

## Target (owner, 2026-09-23)

All three iHRIS 5 IGs: `ig/`, `ihris-backend-site/ig` and `ihris-backend-site/qualify-ig`.

## Format (owner, 2026-09-23)

StructureMaps (D6 γ). The source structures are the logical models (`ihris-ct58`), so this is blocked by that bean too.

## Unblocked (2026-10-09)

The owner answered "all" to the iHRIS 5 FHIR options, which includes this mapping (F4). Its inputs, the logical models, now exist (bean ihris-ct58).

## In progress (2026-10-09): what is done

Tool `ihris-map-ihris5` (`src/tools/map_ihris5.py`) does the mapping on evidence alone: equality of names and labels, with no synonym table and no judgement.

- **Index:** the three IGs at the pin, compiled by SUSHI 3.20.1 in `.build/ihris5-sd/` (the backend IGs include `ig/` through their `input/fsh/core` symlink). It holds names, paths, labels, types, bindings and sha256s only, in `src/ihris-4-on-fhir/mapping/ihris5-index.json`. Declared workspace patches (`src/ihris5/ig-build-patches.json`) are applied to each copy before SUSHI builds it, and the index records which: `role-primary-context` on all three, and for qualify `qualify-include-location` (the manage IG's `IhrisLocation.fsh`, for `IhrisFacility`) and `qualify-residence-jurisdiction` (`IhrisJurisdiction`, defined nowhere, replaced by the manage IG's own target for the same extension, `IhrisCountry or IhrisRegion or IhrisDistrict`). All three compile with 0 errors (owner, 2026-10-09: "do the #2 qualify local fix"); each patch is an upstream defect in `docs/upstream/ihris5-ig-defects.md`.
- **Crosswalk:** `mapping/crosswalk.json`, with every candidate's evidence; tiers exact / accepted / ambiguous / none, per IG.
- **StructureMaps:** `input/fsh/maps/`, only for the exact matches, built clean by SUSHI. iHRIS 5 canonicals are URLs only.
- **Gap report:** `mapping/gaps.json` and `gaps.md`, and on the site's FHIR page.
- **QA:** `ihris5-index`, `fhir-crosswalk`, `fhir-gaps` and `dak-proposal-mapping` in `qa.py`, each shown to fail on a tampered input. `validate.py` runs `map_ihris5.py --check`, which needs no iHRIS 5 mount, so CI runs it.

## Waiting on the owner

- The proposals in `src/ihris-data-dictionary/authored/ihris5-mapping.json`: the ambiguous model and element matches, and the bean's example Person→IhrisPractitioner in the qualify IG, which the matcher did not reach. Accept one with `selected`; it then drives the next run.
- Whether exact matches to iHRIS 5's *test* profiles (`IhrisTestPractitioner` in `ig/`) should stand. Reject them with a mapping item with `status: rejected` to drop them.
- Whether the StructureMaps should also set the values the target profiles fix (e.g. `Basic.code`), and how coded fields map into `code` or `Reference` targets (ConceptMaps). Today these are `ambiguous`, never guessed.

This bean stays in progress while proposals are open.

