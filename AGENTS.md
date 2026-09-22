# AGENTS.md: ihris

What a cold agent does here, in order. The platform's rules are in
[folio-assistant's AGENTS.md](https://github.com/litlfred/folio-assistant/blob/main/AGENTS.md); this file adds what is specific to this folio and does not restate them.

## 1. Know what this is

A **folio** (content repository) on the `folio-assistant` platform, `contentType: document`. The root instance is `ihris` ([`ihris.json`](ihris.json)), and it lists ten sub-instances, each with its own `<name>.json`. Read the [README](README.md) for the map.

## 2. Rules that bind here

1. **Describe, never materialize, Launchpad source** (owner ruling, issue #1). Never commit a source tarball or a copy of a branch. Tarballs go in `uploads/<name>/`, which is git-ignored, with a `manifest.json` pinning `md5` and `sha256`.
2. **Verify before deriving.** A tarball's MD5 must match the one recorded from Launchpad (`uploads/launchpad/release-file-md5.tsv`) before anything is derived from it. `build_kg.py` re-checks the sha256 and refuses on mismatch.
3. **Generated means generated.** `src/*/catalogue`, `src/*/modules`, `src/*/data-model`, `src/ihris5/inventory`, `library/ihris-toolkit/{sections,stages,images}`, `library/ihris-wiki/osi-help-*`, `src/ihris-dak/{data-dictionary,core-data-elements}` + its csv/xlsx/json, and `docs/generated` are build output. Change `uploads/` or `src/tools/build_kg.py`, never the output.
4. **Licence decides what may be reproduced.** GPL/LGPL content may be ingested with attribution. Content with no licence (e.g. `iHRIS/ihris-documentation`) is listed by path and heading only.
5. **Core is the owner's call.** Core = i2ce, ihris-common, ihris-manage, ihris-qualify, ihris-plan, openhie-pr. Do not promote a country customization.
6. **Reuse folio-assistant's schemas first.** Catalogue nodes are `folio-catalogue-node/v1`, validated with folio-assistant's own zod. New schemas in `src/schemas/` only for what it has no field for.

## 3. Before you commit

```sh
python3 src/tools/build_kg.py && python3 src/tools/build_dak.py && python3 src/tools/validate.py   # must print OK
```

`build_dak.py` needs `pip install openpyxl pycountry==24.6.1` (pycountry pins the ISO data the ISO ConceptMaps are verified against). `validate.py` needs a folio-assistant checkout with `bun install` done (`FOLIO_ASSISTANT=<path>`, default `../litlfred/folio-assistant`). Without one it warns and skips the zod checks. That is not a pass.

## 4. Adding a knowledge asset

Use the skills in [`src/skills/`](src/skills/):

| you have | skill |
|---|---|
| a Launchpad project | `describe-launchpad-source` |
| a release tarball | `extract-i2ce-modules` |
| a toolkit page | `ingest-toolkit-stage` |
| wiki HTML / an export | `restore-wiki-from-help-export` |
| a GitHub repo | `snapshot-github-repo` |
| a changed data model, or DAK work | `derive-dak-data-dictionary` |
| a PDF or Word document | folio-assistant's `library-ingestion` skill, into `library/<slug>/` |

## 5. Network

A Claude Code cloud session reaches `launchpad.net` (project, series and milestone pages, `+rdf`, `+md5`) and GitHub (anonymous git). It does **not** reach code/bazaar/bugs/api.launchpad.net, launchpadlibrarian.net, wiki.ihris.org, toolkit.ihris.org or web.archive.org. Ask the owner to upload what those hold.

## 6. Derived knowledge assets never invent

`src/ihris-dak` is derived. Columns the source cannot answer (definitions, conditionality, indicator and decision-support linkages) stay null until a person authors them. Never fill them with plausible text. Human decisions go in `src/ihris-dak/authored/` (`ihris-dak-proposal/v1`), which no build writes. Only the owner moves a proposal's `status`.
