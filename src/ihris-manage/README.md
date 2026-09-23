# iHRIS Manage (`ihris-manage`)

> iHRIS Manage is a human resources management tool that enables an organization to design and manage a comprehensive human resources strategy.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:ihris-manage`](https://launchpad.net/ihris-manage) (Bazaar, GNU GPL v3). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 9 release series with their `lp:` branches, and 46 releases. Each release lists its files with MD5s taken from Launchpad.
- [`modules/4.3.3/`](modules/4.3.3/): 78 I2CE modules (73 with a description; 182 translation overlays folded into them as `locales`), taken from the verified `ihris-suite-4.3.3.tar.bz2`.
- [`data-model/4.3.3/`](data-model/4.3.3/): 26 form classes and 124 fields. This is the iHRIS data model as the source defines it.
- Module overview: [docs/generated/i2ce-modules-4.3.3.md](../../docs/generated/i2ce-modules-4.3.3.md)

## Release notes recovered from Launchpad

- **3.1.0** (2008-08-15): New in this release:
- **3.1.3** (2008-11-19): This release fixes some minor bugs, converts the job application to a module and improves translation support.
- **3.1.4** (2008-12-02): This release includes bug fixes to problems in report paging and list default views.
- **4.1.0** (2011-06-30): Release Candidate 1

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
