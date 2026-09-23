---
name: build-ihris-site
description: >
  Build and publish the iHRIS-themed harness site (litlfred.github.io/ihris/):
  derive the theme from the verified release's own stylesheets, generate the
  landing board and the data-model pages from committed data, check every link
  and both viewports, and let the Pages workflow deploy it.
---

# Build the ihris site

Owner, 2026-09-23: the site is published from this repository and styled like iHRIS (Classic Manage), with the iHRIS logo credited under the GPL. The data-model pages follow the accepted wireframe H2 (`docs/design/wireframes/data-model-site/acceptance.json`).

## 1. Theme (Tool `ihris-extract-theme`)

```sh
python3 src/tools/extract_theme.py          # needs uploads/ihris-suite-4.3.3/*.tar.bz2
```

- It reads `globalStyles.css`, then `themeStyles.css`, in cascade order, and writes `src/site/theme/ihris-classic.json` (`ihris-site-theme/v1`) and the logo.
- Every token records the selector and file it was measured from.
- **Never hand-edit a colour.** Where a measured colour fails WCAG AA in its role, the tool picks another colour *measured from the same stylesheets* and records the reason in `adjustments`.
- To change the look, change the rules in the tool.

## 2. Site (Tool `ihris-build-site`)

```sh
python3 src/tools/build_site.py --out .build/site --check-links
```

- Everything is generated:
  - the landing board, from `ihris.json` and each instance's `<name>.json`;
  - one page per package and per class, from `src/*/data-model/4.3.3`.
- Links are relative, so the site works under `/ihris/` and from a file.
- `_site/` is git-ignored. Never commit the output.

## 3. Check both viewports

Every page is checked for horizontal overflow at web 1280×800 and mobile 390×844. A page that overflows on either is a defect in the generator's CSS, not in the page. `validate.py` builds the site and fails on any broken link.

## 4. Publish

`.github/workflows/pages.yml` builds on every push to `main` and deploys with GitHub Pages (Actions). Before the first deploy, the owner sets **Settings → Pages → Source: GitHub Actions**.
