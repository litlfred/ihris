---
# ihris-u3fg
title: Dark scheme for the iHRIS site theme (the folio rail's light/dark switch)
status: todo
type: task
tags:
    - site
created_at: 2026-10-09T11:11:29Z
updated_at: 2026-10-09T11:11:29Z
---

The folio chrome (bean ihris-0uoj's follow-up; Tool ihris-rail-site) gives every page the platform's light/dark switch, which sets data-fa-scheme on <html>. The iHRIS theme (src/site/theme/ihris-classic.json, measured from the 4.3.3 release CSS) has LIGHT colours only, so the page stays light when a reader picks dark, and folio-site-chrome-check reports 'scheme toggle changes the page' as failing.

A dark palette is a design decision, not something to derive or invent: it needs the owner's call (wireframe-design-review, web and mobile), then dark values in the theme with the same WCAG AA check, emitted through cat-harness's darkRules (scripts/lib/scheme-css.ts) so the switch and the OS setting both apply.
