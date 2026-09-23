# iHRIS Qualify (`ihris-qualify`)

> iHRIS Qualify is a health worker training, licensing and certification tracking system. The system enables a licensing or certification authority for a health worker cadre, such as nurses or physicians, to track data on the complete cadre in a country from pre-service training through attrition.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:ihris-qualify`](https://launchpad.net/ihris-qualify) (Bazaar, GNU GPL v3). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 8 release series with their `lp:` branches, and 43 releases. Each release lists its files with MD5s taken from Launchpad.
- [`modules/4.3.3/`](modules/4.3.3/): 29 I2CE modules (27 with a description; 39 translation overlays folded into them as `locales`), taken from the verified `ihris-suite-4.3.3.tar.bz2`.
- [`data-model/4.3.3/`](data-model/4.3.3/): 25 form classes and 98 fields. This is the iHRIS data model as the source defines it.
- Module overview: [docs/generated/i2ce-modules-4.3.3.md](../../docs/generated/i2ce-modules-4.3.3.md)

## Release notes recovered from Launchpad

- **3.1.0** (2008-08-15): New in this release:
- **3.1.3** (2008-11-19): This release includes some minor bug fixes and improved translation support.
- **3.1.4** (2008-12-02): This release includes a couple of minor bug fixes in report paging and default lists.

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
