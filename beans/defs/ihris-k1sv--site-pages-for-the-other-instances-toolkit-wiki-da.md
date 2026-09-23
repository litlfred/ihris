---
# ihris-k1sv
title: 'Site: pages for the other instances (toolkit, wiki, data dictionary, sources); harness KG viewer'
status: todo
type: task
tags:
    - design
created_at: 2026-09-23T12:15:52Z
updated_at: 2026-09-23T12:15:52Z
---

On the landing board, only the four core packages and the data model link to generated pages. The toolkit, wiki, data dictionary, ihris5, ihris-plan, openhie-pr and ihris-4-on-fhir cards link to GitHub.

Next:
- Generate pages from their committed data. Licence rules apply: `iHRIS/ihris-documentation` is headings only.
- Decide whether to also mount into folio-assistant (`/folio-assistant/ihris/`). That needs a platform change: its site build clones only its own repo (explored 2026-09-23: mount-instance-docs.ts scans only top-level directories). The KG viewer would come with such a mount.
