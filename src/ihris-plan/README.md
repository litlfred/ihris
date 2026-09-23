# iHRIS Plan (`ihris-plan`)

> iHRIS Plan is planning and modeling software developed to improve how health sector planners and program decision makers plan for their health workforce needs in developing country settings. The software helps planners and decision makers model workforce needs and make effective policy decisions to meet those needs.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:ihris-plan`](https://launchpad.net/ihris-plan) (Bazaar, GNU GPL v2). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 2 release series with their `lp:` branches, and 5 releases. Each release lists its files with MD5s taken from Launchpad.
- Modules and data model: **not yet described**. The verified 4.3.3 suite tarball does not contain `ihris-plan`. To describe it, upload a `ihris-plan` release tarball; its Launchpad MD5 is already recorded in `catalogue/records/`, so the upload can be verified.

## Release notes recovered from Launchpad

- **1.0.0** (2008-08-15): This is the first release.
- **1.0.3** (2008-11-19): This release includes improved translation support.
- **1.0.4** (2008-12-02): Release includes some minor bug fixes to report paging and default list display.

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
