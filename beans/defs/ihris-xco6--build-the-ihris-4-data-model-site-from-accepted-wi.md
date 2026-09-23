---
# ihris-xco6
title: Build the iHRIS 4 data-model site from accepted wireframe H2
status: todo
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
