---
# ihris-glsk
title: 'SKOS glossary: toolkit terms, use-case glossaries and code lists, on a glossary/ page and in search'
status: in-progress
type: feature
tags:
    - glossary
    - skos
    - site
created_at: 2026-09-23T23:00:00Z
updated_at: 2026-09-23T23:00:00Z
---

The owner, 2026-09-23: *"everything extracted to glosasay / skos? accesible in ihris page/search?"*, then *"it should be part of general pracice w/ glossary/ page"*, *"put glossary into folio-assistant-core"* and *"can glossary be refefences to external skos schema?"*. Yes: reference first, define second. folio-assistant issue [#1217](https://github.com/litlfred/folio-assistant/issues/1217) put the glossary into core, and PR [#1218](https://github.com/litlfred/folio-assistant/pull/1218) adds core's `glossary` graph kind, the `folio-glossary/v1` schema with `toSkos` (`folio-assistant-core/schemas/glossary.ts`), and the skill `glossary-terms`. This bean adopts them here.

**Waits on #1218.** ihris CI clones folio-assistant `main`, and `validate-folio.ts` stops on a checkout without `folio-assistant-core/schemas/glossary.ts`. So this branch's CI stays red until #1218 merges, and the pull request opens after that. Complete this bean in that pull request's last commit.

## What was built

- `glossary/`, declared in `ihris.json` (`graphKinds: ["glossary"]`, read-only, generated): 35 schemes, 1725 terms. Term IRIs are in the instance namespace, `https://litlfred.github.io/ihris/ihris/ns#glossary/<scheme>/<term>`.
  - `toolkit-technical-terms`: 33 terms, authored, verbatim from the stage pages, with the toolkit's attribution and the owner's permission (bean `ihris-kngr`).
  - `use-cases-2009`: no terms. Each report's document summary says "Use cases, actor goal list, glossary and packages", but none of the four reports holds a glossary section. `ingest_use_cases.py` now records that (`glossary` in `ihris-use-cases/v1`) and stops if a report's text ever names one. None was invented.
  - 33 `code-list-<form>` schemes: 1692 terms from the iHRIS 4.3.3 default records. 541 ISCO-88 groups are authored with the definition the release ships (`description`), and 1151 are candidates. Sample records are left out.
  - `exactMatch`: 245 countries to the EU Publications Office country table and 143 currencies to its currency table. They come only from the verified ConceptMaps `country-to-iso-3166` and `currency-to-iso-4217` (equal only); and 619 ISCO-08 codes (10 major, 43 sub-major, 130 minor, 436 unit) to ESCO by ValueSet identity (owner, 2026-09-24).
  - `remoteGraphs` in `ihris.json`: ESCO ISCO-08 and the two EU authority tables, `graphKinds: ["glossary"]`. The IRIs are built by each publisher's pattern and were not dereferenced (the session cannot reach those hosts).
- `src/tools/build_glossary.py` (Tool `ihris-build-glossary`, skill `build-skos-glossary`): deterministic, and `--check` runs in `validate.py`. Its `to_skos` mirrors core's `toSkos`, because the Pages workflow has no bun. `validate-folio.ts` validates each scheme with core's `GlossarySchema`, and fails unless core's `toSkos()` equals the published SKOS JSON-LD, key order included.
- Site: `glossary/` has A–Z navigation, a filter with a live count, badges for the states, definitions, matches and sources, a Sources section with SKOS JSON-LD per scheme and the external schemes, and a schema.org `DefinedTermSet`. `data-model/search.html` now searches glossary terms too, at the same URL. There is a nav item and a landing card, and toolkit stage pages anchor each term. Targets are 44px, and the site was checked at 390px and 1280px.
- QA (`qa.py`, `folio-glossary/v1`), each check with a mutation test that showed it fails:
  - `glossary-schemes`
  - `glossary-ids`
  - `glossary-matches` (recomputed from the ConceptMaps)
  - `glossary-counts`
  - `glossary-verbatim` (against the source JSON and the captured toolkit HTML)
  - `glossary-page`

## Open: the owner's call

- **ISCO-08 to ESCO: decided.** No ConceptMap records a mapping from iHRIS's `isco_08_*` lists to ISCO-08; `build_dak.py` binds them to the ILO system as a ValueSet. The owner accepted that binding as identity on 2026-09-24 (*"Accept ValueSet identity"*), so every ISCO-08 code has `exactMatch` to ESCO, the scheme descriptions name the basis, and `glossary-matches` recomputes it from the ValueSets. ISCO-88 definitions stay verbatim (*"Keep verbatim"*). Conventions (instance namespace; one ConceptScheme per code list) follow folio-assistant and are written in the skill.
- **The instance namespace** `https://litlfred.github.io/ihris/ihris/ns#` applies core's `instanceNs` rule (`<publication root><instance>/ns#`) to this repository's own site. Confirm it, or name another (compare bean `ihris-gj3u`, the DAK canonical).
- **ISCO-88 definitions** are the ILO's text as iHRIS 4.3.3 ships it, and some carry the release's own concatenation errors. They are published verbatim as `authored` under the release's GPL.
