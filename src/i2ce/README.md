# I2CE (`i2ce`)

> IntraHealth Informatics Core Engine is a set of classes for handling database-driven HTML forms with templates and database abstraction. It is the core programming engine for the iHRIS Suite of software. The Informatics Core Engine is free and Open Source software distributed under the GPL.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:i2ce`](https://launchpad.net/i2ce) (Bazaar, GNU GPL v3). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 10 release series with their `lp:` branches, and 46 releases. Each release lists its files with MD5s taken from Launchpad.
- [`modules/4.3.3/`](modules/4.3.3/): 129 I2CE modules (113 with a description; 245 translation overlays folded into them as `locales`), taken from the verified `ihris-suite-4.3.3.tar.bz2`.
- [`data-model/4.3.3/`](data-model/4.3.3/): 12 form classes and 29 fields. This is the iHRIS data model as the source defines it.
- Module overview: [docs/generated/i2ce-modules-4.3.3.md](../../docs/generated/i2ce-modules-4.3.3.md)

## Release notes recovered from Launchpad

- **3.1.0** (2008-08-15): New in this release:
- **3.1.3** (2008-11-19): This release includes a few minor bug fixes and feature requests plus improved translation support.
- **3.1.4** (2008-12-02): The bug fixes are to report paging and default lists. See the changelog for details.

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
