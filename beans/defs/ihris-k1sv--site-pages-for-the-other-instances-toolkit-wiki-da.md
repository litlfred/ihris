---
# ihris-k1sv
title: 'Site: pages for the other instances (toolkit, wiki, data dictionary, sources); harness KG viewer'
status: completed
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

## Outcome (2026-09-23)

The site grows from 163 to 655 pages. Every landing card now opens a page on the site:
- **Sources:** 37 Launchpad projects by classification; for each of the 6 Launchpad instances, its series, and its releases and milestones with release files and MD5s.
- **Release 4.3.3:** 351 module pages, one per site variant. `name@site` variants no longer overwrite each other; that was a real bug found in the first build. There is a data-lists page per package, and iHRIS 5 (FSH definitions by kind; ihris-documentation by path and heading only).
- **Library:**
  - The toolkit shows **structure only**, because no licence is recorded; see bean ihris-kngr.
  - The wiki has 61 GPL help pages in full. Their links are rewritten to this site, and a link to a page the release did not ship is kept as text. The 5 figures are now restored by `build_kg.py`, pinned by sha256.
- **Data dictionary:** 51 logical-model pages, a value-sets page with shipped codes, the ISO/ISCO reports, and CSV/XLSX downloads.
- **Other:** iHRIS 4 on FHIR, and a schemas index (19 ihris schemas plus the folio-assistant and FHIR ones reused).
- **Checks:** 0 broken links; 0 overflow at 1280 and 390 on all 655 pages.

**Not done:** mounting into folio-assistant (`/folio-assistant/ihris/`). The owner chose this repo's own site.
