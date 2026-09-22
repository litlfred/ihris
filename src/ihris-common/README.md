# iHRIS Common (`ihris-common`)

> iHRIS Common includes common page classes, template files and images for the iHRIS Suite of software: iHRIS Manage, iHRIS Qualify and iHRIS Plan. iHRIS Common is free and Open Source software distributed under the GPL.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:ihris-common`](https://launchpad.net/ihris-common) (Bazaar, GNU GPL v3). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 8 release series with their `lp:` branches, and 39 releases. Each release lists its files with MD5s taken from Launchpad.
- [`modules/4.3.3/`](modules/4.3.3/): 115 I2CE modules (115 with a description; 305 translation overlays folded into them as `locales`), taken from the verified `ihris-suite-4.3.3.tar.bz2`.
- [`data-model/4.3.3/`](data-model/4.3.3/): 93 form classes and 334 fields. This is the iHRIS data model as the source defines it.
- Module overview: [docs/generated/i2ce-modules-4.3.3.md](../../docs/generated/i2ce-modules-4.3.3.md)

## Release notes recovered from Launchpad

- **3.1.0** (2008-08-15): iHRIS Common includes common page classes, template files and images for the iHRIS Suite of software: iHRIS Manage, iHRIS Qualify and iHRIS Plan.

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
