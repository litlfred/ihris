---
# ihris-hbuc
title: Ingest the 2010 Administrator Handbook (wiki export) and the 2009 use-case model
status: completed
type: task
tags:
    - library
    - licence
created_at: 2026-09-23T19:30:00Z
updated_at: 2026-09-23T19:30:00Z
---

Two sources the owner uploaded on 2026-09-23, each ingested as its own library instance.

## Sources

- **`library/ihris-admin-handbook`**: `ihris_admin_handbook_sep_17_2010.pdf` (md5 `25186f0c5398b7f68364d33d78706613`), uploaded by the owner to litlfred/folio-assistant main (commit b8549160). It is a 534-page mwlib/PediaPress export of 79 iHRIS wiki articles (open.intrahealth.org), generated 2010-09-17, titled "iHRIS Administator Handbook" (sic).
- **`library/ihris-use-cases`**: four Serlio CaseComplete reports, `iHRIS{Common,Manage,Qualify,Plan}UseCases.doc` (2009, author sturlington): 21 Common, 58 Manage, 47 Qualify and 12 Plan use cases.

Both are pinned by md5 and sha256 in `uploads/<slug>/manifest.json`, and the files themselves are git-ignored (`*.pdf`, `*.doc`).

## The owner's licence decisions (chat, 2026-09-23)

- **Handbook text:** GFDL-1.2, as the export's last page states (`licence.status: stated`, `id: GFDL-1.2`). Attribution goes to the iHRIS wiki and IntraHealth contributors; every article carries its wiki revision (`oldid`) and contributors from the export's "Article Sources and Contributors" appendix.
- **Handbook images:** the image-credits appendix says "License: unknown" for all 11. The owner decided to ingest them too, under their **permission** (`licence.images`, `status: permission`, granted by litlfred, 2026-09-23). Each image keeps its credit line.
- **Use cases:** no licence is stated. The owner answered "I have permission" (`licence.status: permission`, granted by litlfred, 2026-09-23). The scope is the full text: use cases, steps, extensions, notes, actors and requirements. Attribution goes to IntraHealth International / the Capacity Project iHRIS team.

## What was withheld

- The handbook has 4 redactions: 3 e-mail addresses and 1 phone number (organisational contact details in "README File for iHRIS" and a module example). Placeholder addresses in example configuration are kept.
- In the use cases, the "Assigned To" field (staff initials, 12 use cases) and requirement "Source" (a named person, 12 Qualify requirements) are counted but not copied. **Owner:** say if either may be published.
- The handbook holds no talk or user pages, so there are no reader comments.

## How it is built

- `src/tools/ingest_handbook.py` (Tool `ihris-ingest-handbook`) runs folio-assistant's `pdf-structure` and `pdf-images` rungs, then writes one Markdown section per article and `book.json` (`ihris-wiki-book/v1`).
- `src/tools/ingest_use_cases.py` (Tool `ihris-ingest-use-cases`) runs antiword and a deterministic parser. It writes `ihris-use-cases/v1` per product, Markdown, and `crosswalk.json` (`ihris-use-case-crosswalk/v1`). The crosswalk links use cases to iHRIS 4.3.3 forms by name matching only; unmatched use cases stay null. iHRIS Plan has no data model in this repository.
- Dangling references (cited, never described) are recorded: UC-ICE26, UC-PS26, UC-PP11/13/14/15/20/22/23, and actor A-PT9 (listed in the Manage table of contents only).

## Relation to ihris-wiki

The handbook is a 2010 snapshot of the same wiki that `library/ihris-wiki` restores from the 4.3.3 help exports (the user manual). They share one page by title, "IHRIS Manage Form Fields - 4.0". Otherwise the handbook holds the administrator and developer articles that `ihris-wiki`'s README lists as "still to restore". It stays its own entry because its licence (GFDL-1.2), date and provenance differ. Restoring those pages into `ihris-wiki` (skill `restore-wiki-from-help-export`) can take the handbook as a source.

## QA

New schemas `ihris-wiki-book/v1`, `ihris-use-cases/v1` and `ihris-use-case-crosswalk/v1` are added, and folio-assistant's `folio-document-images/v1` is reused (zod in `validate-folio.ts`). Each has a check in `src/tools/qa.py`: `wiki-book`, `use-cases`, `use-case-crosswalk` and `document-images`.

Each check was mutation-tested (2026-09-23) and reported the break:
- an extension off a missing step;
- a drifted use-case count;
- an invented form link;
- a section sha256 mismatch;
- a dropped image credit;
- an image page mismatch;
- an unredacted e-mail address added to a section.

Both ingest tools are deterministic: a re-run reproduces every output byte for byte.
