# iHRIS Knowledge Base

A [folio-assistant](https://github.com/litlfred/folio-assistant) folio that **ingests and describes** the knowledge assets of [iHRIS](https://www.ihris.org/), the open-source health workforce information system: its source code, its documentation, its implementation toolkit and its wiki. It is the base for building new knowledge assets on top of them.

**Described, not copied.** Source code stays where it lives (Launchpad, GitHub). This repository holds catalogue nodes that point at it by `lp:` branch or git commit, with checksums, and descriptions *derived* from verified copies.

## Instances

| instance | what | status |
|---|---|---|
| [`i2ce`](src/i2ce/) | I2CE, the framework engine (Launchpad) | series, releases, 129 modules, data model |
| [`ihris-common`](src/ihris-common/) | shared forms, pages, modules | series, releases, 115 modules, data model |
| [`ihris-manage`](src/ihris-manage/) | HR management application | series, releases, 78 modules, data model |
| [`ihris-qualify`](src/ihris-qualify/) | training, licensing and certification | series, releases, 29 modules, data model |
| [`ihris-plan`](src/ihris-plan/) | workforce planning and modelling | series and releases only; modules need a tarball |
| [`openhie-pr`](src/openhie-pr/) | OpenHIE Health Worker Registry (CSD) | series only; modules need a tarball |
| [`ihris5`](src/ihris5/) | iHRIS 5 (FHIR) on GitHub, plus its docs | pinned at a commit, with path inventories |
| [`ihris-toolkit`](library/ihris-toolkit/) | toolkit.ihris.org implementation stages | 6 stages ingested; 47 hosted tool documents still referenced |
| [`ihris-data-dictionary`](src/ihris-data-dictionary/) | **derived:** WHO SMART DAK (L2) data dictionary for health workforce data | 247 data elements, 51 logical models, 47 value sets as FHIR R4 terminology (12 with shipped codes); descriptions to author |
| [`ihris-wiki`](library/ihris-wiki/) | the old iHRIS wiki | 44 user-manual pages restored from 4.3.3 help exports |

The other Launchpad projects (country customizations such as ihris-kenya and ihris-manage-ghana, and side tools) are catalogued in [`src/catalogue/`](src/catalogue/); see [the inventory](docs/generated/launchpad-inventory.md).

## Layout

| path | holds |
|---|---|
| `src/` | one directory per source instance, the root catalogue, the [schemas](src/schemas/), [skills](src/skills/) and [tools](src/tools/) |
| `library/` | ingested content: toolkit, wiki |
| `docs/` | [documentation about this knowledge base](docs/index.md); `docs/generated/` is build output |
| `uploads/` | raw captures as received: the ingestion queue, not corpus |

## Numbers (release 4.3.3)

351 I2CE modules, 156 form classes and 586 fields across the four core packages in the verified `ihris-suite-4.3.3.tar.bz2`. 37 Launchpad projects catalogued.

## Rebuild and check

```sh
pip install beautifulsoup4 markdownify jsonschema
python3 src/tools/build_kg.py      # regenerate everything derived from uploads/
python3 src/tools/validate.py      # schemas, references, and folio-assistant's own zod checks
```

Tracking issue: [#1](https://github.com/litlfred/ihris/issues/1).
