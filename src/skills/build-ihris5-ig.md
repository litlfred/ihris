---
name: build-ihris5-ig
description: >
  Build the iHRIS 5 FHIR IG with fhir-harness from the source src/ihris5/ihris5.json pins,
  and publish it only on gh-pages at /ihris/ihris5/: the AST fork of the IG Publisher, the
  artefact index and pages from the AST, the IG's own narrative in just-the-docs inside the
  platform chrome. Use when the pin moves, a build patch changes, or the IG site is wanted.
---

# Build the iHRIS 5 IG (fhir-harness)

Owner, 2026-10-09: *"i want litlfred/ihris to say that ihris-5 is a named subgraph using fhir-harness"*, *"there should be justthedocs which uses AST sushi etc."*, *"we only publish ihris 5 under gh-pages"*.

**The declaration is the pin.** `src/ihris5/ihris5.json` declares core's git source (`iHRIS/iHRIS`, a 40-character commit, `path: ig`) and `needs: ["fhir-harness"]`. Nothing names the IG anywhere else.

| step | what | Tool |
|---|---|---|
| mount | the source at the pin, at `ihris5-source/`, git-ignored, never committed | `ihris-mount-sources` |
| patch | declared fixes (`src/ihris5/ig-build-patches.json`) applied to a WORKSPACE copy only; each one is an upstream defect to report | `ihris-apply-ig-patches` |
| build | `bash src/tools/build_ihris5_ig.sh`: AST export, index, menu, pages, site, Publisher output | `ihris-build-ihris5-ig` |
| publish | `.github/workflows/ihris5-ig.yml`: by hand, or when the pin, patches, script or workflow change; a PR builds into its staging preview | the workflow |

## Rules

- **Never edit the mount or the upstream.** A defect is a patch entry with its reason, and the build fails when a patch no longer applies exactly once, so a fixed upstream is noticed.
- **Never commit the build.** Only gh-pages holds it: `/ihris5/` (the just-the-docs site), `/ihris5/publisher/` (the Publisher's own HTML) and `/ihris5/ast-data/` (the AST's resources).
- **Scoped chrome.** The site wears the platform chrome for ihris and what it needs, never the platform's whole harness list.
- **A package host refused is not a broken IG.** Seed with fhir-harness's `fhir-cache-seed-npm.ts` (npm, template repositories, `--mirror litlfred/fhir-package-mirror`); a version none of those carry needs adding to the mirror from a machine that reaches packages.fhir.org. Never substitute a version in a build that publishes.
