---
# ihris-xco6
title: Build the iHRIS 4 data-model site from accepted wireframe H2
status: completed
type: task
tags:
    - design
    - build
created_at: 2026-09-23T11:51:21Z
updated_at: 2026-09-23T11:51:21Z
parent: ihris-um1h
---

H2 was accepted on 2026-09-23 (`docs/design/wireframes/data-model-site/acceptance.json`). Next:
- generate just-the-docs pages per package and class from `src/*/data-model/4.3.3`, following `round-3/h2.html` and `h2-menu.html` (sidebar, field table and cards, neighbourhood graph with its edge table, relationships list on phones, source);
- declare the harness visualiser on the data-model subgraph (`coverage.visualiser`) so it becomes a navbar and board tile;
- add a wireframe entry covering the new visualiser in folio-assistant `cat-harness/docs/wireframes/index.json`, or its ihris equivalent, so `check:wireframes` stays green.

Generated pages are build output: change the generator, never the pages (AGENTS.md §2.3).

## Outcome (2026-09-23)

The owner asked for a harness page "like litlfred.github.io/folio-assistant/smart-trust, but iHRIS-themed (see css in ihris suite)". The owner's choices:
- publish from this repo at litlfred.github.io/ihris/;
- use the Classic Manage theme;
- show the logo, with attribution.

**Built:**
- `src/tools/extract_theme.py` measures the theme from `globalStyles.css` and `themeStyles.css` in the verified tarball. Three colours are swapped for other measured ones to reach WCAG AA; each swap is recorded.
- `src/tools/build_site.py` generates 163 pages:
  - a landing board of 11 instances, plus the data-model card;
  - an overview, 4 package pages and 156 class pages in the H2 layout;
  - a search page.
- Checks: 0 broken links; 0 horizontal overflow at 1280 and 390 across all 163 pages.
- `.github/workflows/pages.yml` deploys it.

**Where it differs from H2:**
- The "Harness visualiser" tile opens this site's data model, not folio-assistant's KG viewer. That viewer only exists for instances inside folio-assistant (see bean ihris-k1sv).
- The sidebar excerpt shows one class above the current one and two below; H2 showed only the classes below.
