# iHRIS 5 (`ihris5`)

iHRIS 5 is the FHIR-based successor to the Launchpad PHP suite. Two repositories are described here, each **pinned by commit** and **not copied**:

| repository | commit | licence | what the inventory holds |
|---|---|---|---|
| [iHRIS/iHRIS](https://github.com/iHRIS/iHRIS) | `fa66e9b` (2026-09-07) | LGPL-3.0 | 684 FSH definitions (421 Instance, 85 Extension, 60 CodeSystem, 60 ValueSet, 45 Profile, 10 Alias, 3 Invariant), 24 Markdown pages, packages: ihris 0.1.0, ihrisigtemplate 0.1.0, ihris-backend 5.1.5, iHRIS-v5 0.1.0, site 1.0.0, ihris-tools 1.0.0 |
| [iHRIS/ihris-documentation](https://github.com/iHRIS/ihris-documentation) | `29a0a86` (2024-11-12) | **none found** | 43 pages of the *iHRIS V5 Technical Documentation* site (developer, sysadmin, user, FAQ, video) |

The documentation repository has **no licence file**, so its pages are listed by path and heading only, and their text is not reproduced.

- [`catalogue/`](catalogue/): the two repositories as catalogue nodes
- [`inventory/`](inventory/): the path-level inventories

Refresh: `git clone --depth 1` each repository, run `python3 src/tools/snapshot_github.py <clone> <owner/repo>`, then `python3 src/tools/build_kg.py`.
