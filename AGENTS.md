# AGENTS.md: ihris

What a cold agent does here, in order. The platform's rules are in
[folio-assistant-core's AGENTS.md](https://github.com/litlfred/folio-assistant-core/blob/main/AGENTS.md) and the harness's in [cat-harness's](https://github.com/litlfred/cat-harness/blob/main/AGENTS.md); this file adds what is specific to this folio and does not restate them.

## 1. Know what this is

A **folio** (content repository) that depends on **folio-assistant-core**, `contentType: document`, laid out as [who-iris](https://litlfred.github.io/who-iris/) is. `ihris.json` `needs` folio-assistant-core; [`index.config.json`](index.config.json) pins it and its closure (cat-harness, cat-harness-tools, bootstrap, bootstrap-tools) to commit SHAs, and [`index.lock.json`](index.lock.json) records what they resolved to. `bash src/tools/mount_platform.sh` mounts them at `<name>/`. They are git-ignored, never edited, and never committed. Tools find them through `src/tools/folio_platform.py` only. The root instance is `ihris` ([`ihris.json`](ihris.json)), and it lists fourteen sub-instances, each with its own `<name>.json`. Read the [README](README.md) for the map.

## 2. Rules that bind here

1. **Describe, never materialize, Launchpad source** (owner ruling, issue #1). Never commit a source tarball or a copy of a branch. Tarballs go in `uploads/<name>/`, which is git-ignored, with a `manifest.json` pinning `md5` and `sha256`.
2. **Verify before deriving.** A tarball's MD5 must match the one recorded from Launchpad (`uploads/launchpad/release-file-md5.tsv`) before anything is derived from it. `build_kg.py` re-checks the sha256 and refuses on mismatch.
3. **Generated means generated.** `src/ihris-4-on-fhir/input/fsh` (from `build_dak.py` and `gen_fsh.py`), `src/*/catalogue`, `src/*/modules`, `src/*/data-model`, `src/ihris5/inventory`, `library/ihris-toolkit/{sections,stages,images}`, `library/ihris-wiki/osi-help-*`, `library/ihris-admin-handbook/{sections,images,images.json,book.json,structure.json,manifest.jsonld}` (from `ingest_handbook.py`), `library/ihris-use-cases/{common,manage,qualify,plan}.{json,md}` + `roles.md` + `scenarios/` + `crosswalk.json` + `manifest.jsonld` (from `ingest_use_cases.py`), `library/ihris-admin-course/{course.json,course.md,manifest.jsonld,sections,modules,transcripts,images}` (from `ingest_moodle_course.py`), `src/ihris-data-dictionary/{data-dictionary,core-data-elements}` + its csv/xlsx/json, `glossary/*.glossary.json` (from `build_glossary.py`), `docs/generated`, `src/site/theme` (from `extract_theme.py`, including `intrahealth-logo.png`, IntraHealth's logo from the verified release; its `ihris-classic-dark.json` and `docs/assets/img/iHRIS_logo-on-dark.svg` from `derive_dark_theme.py`, whose input `ihris-classic-dark.grounds.json` is the owner's choice and is authored) and the site `_site/` (from `build_site.py`, never committed) are build output. Change `uploads/` or the tool in `src/tools/`, never the output.
4. **Licence decides what may be reproduced.** GPL/LGPL content may be ingested with attribution. Content with no licence (e.g. `iHRIS/ihris-documentation`) is listed by path and heading only, unless its declaration records a `licence`: either `stated` (with the licence id and where it is stated) or the owner's `permission` (who granted it, when, and the scope). Only the owner grants permission. The toolkit has one (2026-09-23, bean `ihris-kngr`), and so do the 2009 use cases and the handbook's images (bean `ihris-hbuc`). The handbook's text is GFDL-1.2, as stated in the export. The administrator course (`library/ihris-admin-course`) is CC-BY-4.0, stated by its author, the owner, on 2026-10-09, and attributed to IntraHealth International with its logo. Third parties' personal content, such as reader comments, is never published.
5. **Core is the owner's call.** Core = i2ce, ihris-common, ihris-manage, ihris-qualify, ihris-plan, openhie-pr. Do not promote a country customization.
6. **Reuse folio-assistant's schemas first.** Catalogue nodes are `folio-catalogue-node/v1`, validated with folio-assistant's own zod. New schemas in `src/schemas/` only for what it has no field for. In a declaration, ihris's own provenance key is `upstream` (core reserves `source` for `{kind: "git", repository, ref}`), and a directory's kinds are `graphTypologies`.

## 3. Before you commit

```sh
python3 src/tools/build_kg.py && python3 src/tools/build_dak.py && python3 src/tools/gen_fsh.py && python3 src/tools/validate.py   # must print OK
```

`build_dak.py` needs `pip install openpyxl pycountry==24.6.1`, `gen_fsh.py` needs SUSHI (`npm install -g fsh-sushi@3.20.1`; it writes the terminology JSON from SUSHI's build), and the site build that `validate.py` runs needs `pip install -r src/tools/requirements-site.txt` (pycountry pins the ISO data the ISO ConceptMaps are verified against). `validate.py` needs the platform layers mounted: run `bash src/tools/mount_platform.sh` first (it also runs `bun install`). Set `FOLIO_PLATFORM=<dir>` only if you mounted them somewhere else. Without them it warns and skips the zod checks. That is not a pass.

**CI runs this on every commit:** `.github/workflows/ci.yml` runs on every push to any branch and on every pull request. In CI (`CI` set), a skipped check is an error, not a warning.

**Every schema and node type has QA** (`src/tools/qa.py`, skill `qa-coverage`): each one has checks beyond shape, such as references resolving, counts matching and files existing. A schema or node type with no QA check fails as `qa-missing`, because missing QA is a QA failure in itself. When you add a schema, add its QA check, and prove the check can fail.

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
| a PDF or Word document | folio-assistant's `library-ingestion` skill, into `library/<slug>/` (Tool `ihris-ingest-pdf`) |
| a MediaWiki book export (mwlib PDF) | `ingest-wiki-book-export` (Tool `ihris-ingest-handbook`) |
| a use-case model report (CaseComplete .doc) | `ingest-use-case-model` (Tool `ihris-ingest-use-cases`) |
| a Moodle course backup (moodle.xml + course_files/) | `ingest-moodle-course` (Tool `ihris-ingest-moodle-course`): the content under the declaration's licence, structure only without one |
| a paper or standard whose **method** is to be used | `adopt-methodology-from-source` (process `processes/methodology-from-source.bpmn`) |
| a UI to design (pages, visualisers) | `wireframe-design-review` (methodology `wiregen`): web **and** mobile, with adjudication |
| the site to (re)build or restyle | `build-ihris-site`: iHRIS theme measured from the release CSS, pages from the data, published on the `gh-pages` branch by `.github/workflows/pages.yml`, at litlfred.github.io/ihris/ |
| terms to define, or external SKOS concepts to link (the glossary) | `build-skos-glossary` (Tool `ihris-build-glossary`): folio-assistant core's `folio-glossary/v1`, reference first; matches only from verified ConceptMaps |
| FHIR work on the iHRIS 4 data model | `ihris-4-on-fhir` (documented; SUSHI later) |
| a KG subgraph to draw as one diagram (forms, a declaration schema) | `kg-subgraph-layout` (Tool `ihris-kg-layout`): the i2ce Form Documentor's Graphviz convention over a projection, laid out in the browser by Graphviz in WebAssembly with draggable nodes |
| the iHRIS 5 IG to build or re-pin | `build-ihris5-ig` (Tool `ihris-build-ihris5-ig`): fhir-harness, from the source `src/ihris5/ihris5.json` pins; published only on `gh-pages` at `/ihris5/` by `.github/workflows/ihris5-ig.yml` |

## 5. Processes and tools

`processes/*.bpmn` are generated from `processes/specs/*.json` by `src/tools/gen_bpmn.py`, and `validate.py` fails when one is stale. Judgement points call folio-assistant's processes (`Process_Adjudication`, `Process_OptionsAnalysis`, `Process_Ingestion`) instead of copying them. **Every skill and tool used gets a Tool node** in `src/tools/*.tool.json`.

## 6. Network

A Claude Code cloud session reaches `launchpad.net` (project, series and milestone pages, `+rdf`, `+md5`) and GitHub (anonymous git). It does **not** reach code/bazaar/bugs/api.launchpad.net, launchpadlibrarian.net, wiki.ihris.org, toolkit.ihris.org or web.archive.org. Ask the owner to upload what those hold.

## 7. Derived knowledge assets never invent

`src/ihris-data-dictionary` is derived. Columns the source cannot answer (definitions, conditionality, indicator and decision-support linkages) stay null until a person authors them. Never fill them with plausible text. Human decisions go in `src/ihris-data-dictionary/authored/` (`ihris-dak-proposal/v1`), which no build writes. Only the owner moves a proposal's `status`.

## 8. FHIR: independent, and gated by design

iHRIS is **independent**: it is not a SMART DAK and is not related to smart-base (owner ruling, 2026-09-23). Do not add smart-base dependencies or smart-base types anywhere. FHIR work is built on **fhir-harness**, the bare FHIR IG pipeline with no WHO in it (owner, 2026-10-09), mounted by `index.config.json`: `src/ihris-4-on-fhir/` (new derived content) and `src/ihris5/` (the iHRIS 5 IG, built from its pinned source and published only on `gh-pages`) both `need` it.

The design is [`docs/design/fhir-strategy.md`](docs/design/fhir-strategy.md), approved 2026-09-23 (bean `ihris-dmgf`). Its rules:
- Python generates FSH, and sushi is the build. Sushi must run clean before any commit that contains FSH.
- The build depends on R4 core only. The canonical is `https://litlfred.github.io/ihris/dak`.
- **Done (owner, 2026-10-09: "all"):** F1 the SUSHI skeleton, F2 terminology as FSH with the D8 switch (the terminology JSON is SUSHI's build), F3 the 51 logical models. Skill `ihris-4-on-fhir`, Tool `ihris-gen-fsh` (with `ihris-sushi`).
- **Next:** F4, the mapping to iHRIS 5 (bean `ihris-7gl8`). **Still waiting:** any IG Publisher or HTML render of this IG, on folio-assistant's lightweight IG render pipeline (bean `ihris-bwls`).

Work items are beans in `beans/defs/` (`.beans.yml`, prefix `ihris-`); the epic is `ihris-g768`.
