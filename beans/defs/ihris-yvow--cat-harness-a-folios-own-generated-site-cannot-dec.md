---
# ihris-yvow
title: 'cat-harness: a folio''s own generated site cannot declare its pages to the rail (foreign-site rail gaps)'
status: todo
type: task
tags:
    - platform
    - upstream
created_at: 2026-10-09T12:19:34Z
updated_at: 2026-10-09T16:00:00Z
---

Found 2026-10-09 publishing ihris's work plan (bean ihris-mdzi) on its own Pages site, railed by cat-harness's rail-standalone-pages.ts --foreign-site --instance ihris. Three platform gaps, bridged in ihris by src/tools/own_site_links.py until cat-harness reconciles them:

1. sync-docs-harness.ts writes the root instance's own pages root-relative (/beans/), while lib/foreign-site-scope.ts keeps a state graph's link only under /<instance>/, so the folio's own /beans/ read as 'not published on this site'.
2. The rail writes the icon row's data-fa-root as the PLATFORM's address, and navbar-row.js composes every root-relative href AND the badge's count.json with it, so a folio's own beans icon opens, and counts, the platform's work plan. A folio's site needs a separate data root.
3. harness-tiles.ts accepts a declared visualiser only under the SITE OWNER's directory (sitePrefix = cat-harness/docs/), so a folio whose site is generated (not a docs/ Jekyll tree) cannot declare its pages: ihris's sources, schemas and library pages show 'no viewer yet'. beans and glossary resolve only because the platform happens to publish pages at the same conventional paths.
4. **A folio's own mark is placed at the platform's address.** The rail writes the root instance's declared `icon` image as `@fa-rail-root@/<path>`, and `@fa-rail-root@` is the platform (`#fa-rail` `data-fa-root`), so the avatar 404s on the folio's own site. Bridged by own_site_links.py --site (2026-10-09), which rewrites it per rail data file, relative to the one page depth each file serves.
5. **The rail draws its tone square behind an image avatar too** (navbar.js `fa-nav-tone`, inline `background:hsl(tone …)`). Card-art crops cover it; a transparent logo does not, and shows a coloured square. Cleared on this site for ihris's own mark by a rule in ihris.css (2026-10-09).


Upstream ask (litlfred/cat-harness): let a foreign-site rail take the folio's own site root for its own graphs' links and counts, and let a declaration name its published pages when its site is generated. Then delete src/tools/own_site_links.py.
