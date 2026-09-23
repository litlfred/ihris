---
# ihris-7gl8
title: Map the DAK logical models to the iHRIS 5 FHIR IG
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

Crosswalk each of the 49 logical models / 242 data elements (from iHRIS 4.3.3 form classes) to the iHRIS 5 profile, element or extension that holds it, e.g. Person→IhrisPractitioner, PersonPosition→IhrisPractitionerRole, Education→IhrisBasicEducationHistory, License→IhrisBasicLicense, Salary→IhrisBasicSalary. Output: ConceptMap(s) or a mapping table, plus a two-way gap report. Needs the iHRIS 5 FSH content (LGPL; only names are inventoried now). Uncertain matches go in `authored/` as proposals.
