# How this knowledge base is built

## Sources, and how each is held

| source | reached via | held here as | state |
|---|---|---|---|
| Launchpad project, series and milestone pages | `launchpad.net` | `folio-catalogue-node/v1` + `ihris-source-record/v1` | referenced |
| Launchpad release files | Launchpad `+md5` pages | file entries with MD5 on release records | referenced (a verified copy of `ihris-suite-4.3.3` exists but is not committed) |
| I2CE module XML (4.3.3) | the verified suite tarball | `ihris-i2ce-module/v1`, `ihris-form-class/v1` | derived descriptions, each pinned by path + sha256 |
| wiki user-manual pages | exports inside the 4.3.3 help modules | Markdown sections in `library/ihris-wiki/` | ingested (GPL-3.0) |
| toolkit stage pages | pages saved by the owner | `ihris-toolkit-stage/v1` + Markdown in `library/ihris-toolkit/` | ingested |
| iHRIS 5 and its docs | GitHub, anonymous git | catalogue nodes pinned by commit + path inventories | referenced |

## Schemas

Reused from folio-assistant: `folio-catalogue/v1`, `folio-catalogue-node/v1` (with `folio-materialization/v1`), the library `manifest.jsonld` / section `.jsonld` shape, and the Tool definition.

Added here, in [`src/schemas/`](../src/schemas/):

| schema | why it is needed |
|---|---|
| `ihris-source-record/v1` | the catalogue node is strict and has no field for an `lp:` branch, a commit, an MD5, release notes or a licence. This is its companion via `metadataRef`, the same pattern as who-iris's Dublin Core records |
| `ihris-i2ce-module/v1` | an I2CE module's requirement/enable/conflict graph, forms and pages |
| `ihris-form-class/v1` | the data model: form classes with fields merged across the modules that contribute them |
| `ihris-toolkit-stage/v1` | the toolkit's stage × domain → objective → tool structure |

## The iHRIS data model as a DAK-style asset

`src/*/data-model/4.3.3/` is, in WHO SMART Guidelines terms, a **core data element** set read from the source: each field has a type (`STRING_LINE`, `MAP`, `DATE_YMD`, …), a label, whether it is required, and for `MAP` fields the list it draws from (e.g. `iHRIS_Person.nationality → country`). Module `requirement` edges give the dependency graph, and the toolkit stages supply the implementation process. These are the inputs for building derived knowledge assets (L2 DAK components, FHIR mappings to the iHRIS 5 IG).
