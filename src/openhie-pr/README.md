# OpenHIE Health Worker Registry (`openhie-pr`)

> OpenHIE Health Worker Registry is a Care Services Discovery (CSD) compliant health worker registry based on the iHRIS/I2CE framework.

**Instance of** the [iHRIS Knowledge Base](../../README.md). **Upstream:** [`lp:openhie-pr`](https://launchpad.net/openhie-pr) (Bazaar, Apache Licence). The source is **described here, not copied**.

## What is here

- [`catalogue/`](catalogue/): 2 release series with their `lp:` branches, and 0 releases. Each release lists its files with MD5s taken from Launchpad.
- Modules and data model: **not yet described**. The verified 4.3.3 suite tarball does not contain `openhie-pr`. To describe it, upload a `openhie-pr` release tarball; its Launchpad MD5 is already recorded in `catalogue/records/`, so the upload can be verified.

## Regenerate

`python3 src/tools/build_kg.py && python3 src/tools/validate.py` (from the repo root). Everything in this directory except this README and the declaration is build output.
