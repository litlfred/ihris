# iHRIS use-case model, 2009 (`ihris-use-cases`)

The **use cases, actors and requirements** of iHRIS Common, Manage, Qualify and Plan, from four *Use Case Model - Complete Report* exports of Serlio CaseComplete (Word 97 `.doc`, 2009, document author `sturlington`). The owner uploaded them on 2026-09-23. The `.doc` files are in `uploads/ihris-use-cases/`, which is git-ignored; [`manifest.json`](../../uploads/ihris-use-cases/manifest.json) pins each one by MD5 and SHA-256.

**Licence:** the reports state none. They are **published with the owner's permission** (litlfred, 2026-09-23), in full, attributed to *IntraHealth International / the Capacity Project iHRIS team*. Two fields are withheld because they name or identify people: "Assigned To" (staff initials) and a requirement's "Source" (a named person). Each is counted in the product file's `withheld`, and neither is copied.

| product | report generated | use cases | actors | requirements | steps | extensions |
|---|---|---|---|---|---|---|
| [iHRIS Common use cases](common.md) ([json](common.json)) | 7/13/2009 3:33 PM | 21 | 4 | 19 | 163 | 37 |
| [iHRIS Manage use cases](manage.md) ([json](manage.json)) | 7/13/2009 3:28 PM | 58 | 4 | 3 | 538 | 102 |
| [iHRIS Qualify use cases](qualify.md) ([json](qualify.json)) | 3/25/2009 4:18 PM | 47 | 6 | 14 | 426 | 105 |
| [iHRIS Plan use cases](plan.md) ([json](plan.json)) | 3/25/2009 4:13 PM | 12 | 1 | 0 | 106 | 21 |

Each `<product>.json` is `ihris-use-cases/v1`. It holds the package tree, and each use case in it carries every Details field (parent, primary and supporting actors, preconditions, success guarantee, level, complexity, status, implementation status, release), its numbered main success scenario, its extensions and their steps, and its dated notes. The file also holds the actors (goals, notes, the use cases each plays a role in) and the requirements (with the use cases that reference them). Each `<product>.md` is the same content, for reading.

## Crosswalk to the iHRIS 4.3.3 data model

[`crosswalk.json`](crosswalk.json) (`ihris-use-case-crosswalk/v1`) links each use case to the forms of this repository's iHRIS 4.3.3 data model (`src/*/modules`, `src/*/data-model`), **by name matching only**. A form matches when its name (underscores read as spaces), or a display name a module declares for it, occurs word for word in the use case's title, after simple plurals are folded. Every link says `derivedBy: name-match`. Nothing is inferred from meaning: an unmatched use case keeps `matches: null` until a person links it (AGENTS.md §7). The `csd_*` forms (OpenHIE CSD, added after 2009) are left out.

- **88 matched** (108 links), **38 unmatched** (`matches: null`).
- **12 not matched: iHRIS Plan.** Plan has **no data model in this repository**: `src/ihris-plan` holds its series and releases only, and its modules need a release tarball.

## Cited but not described

The reports cite these, and describe none of them:

| id | kind | product | title (as cited) | cited by |
|---|---|---|---|---|
| UC-ICE26 | use-case | common |  | UC-ICE19 |
| A-PT9 | actor | manage | Any User | table of contents |
| UC-PS26 | use-case | qualify | Add or update a personal title | A-PS1 |
| UC-PP11 | use-case | plan | Enter pre-service training data | A-PP1, UC-PP21 |
| UC-PP13 | use-case | plan | Enter retirement assumptions | A-PP1 |
| UC-PP14 | use-case | plan | Enter attrition assumptions | A-PP1 |
| UC-PP15 | use-case | plan | Enter pre-service training assumptions | A-PP1 |
| UC-PP20 | use-case | plan | Apply interventions to a base projection model | A-PP1 |
| UC-PP22 | use-case | plan | Produce a health workforce implementation plan | A-PP1 |
| UC-PP23 | use-case | plan | Import supply data | A-PP1 |

## Rebuild

`python3 src/tools/ingest_use_cases.py` (Tool `ihris-ingest-use-cases`). It verifies the `.doc` checksums, runs `antiword -w 0`, and parses deterministically. It stops on any text it does not recognise, rather than skip it. Everything here is **generated**: change the tool, never the output.
