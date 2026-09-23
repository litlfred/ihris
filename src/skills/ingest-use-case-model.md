---
name: ingest-use-case-model
description: >
  Parse a use-case model report (Serlio CaseComplete "Use Case Model - Complete
  Report", Word .doc) into structured ihris-use-cases/v1 records, readable
  Markdown, and a name-matched crosswalk to the iHRIS data model. Use when
  someone shares iHRIS use-case documents.
---

# Ingest a use-case model report

CaseComplete's complete report, extracted with `antiword -w 0`, has a fixed shape:

- **Packages** are numbered headings outside any table (`1. iHRIS Manage - Core Functional`, then `  1. Data Administration` indented two spaces, then three for the next level down). Each has a description, a Notes table and a Related Documents table.
- **Actors** (`|A-PT1 HR Manager|`) carry a description, a Goals table, Notes, and "Use cases that this actor plays a role in:".
- **Use cases** (`|UC-PT23 Create a position|P5|`) carry a description, a two-column **Details** table (Parent, Primary/Supporting Actors, Preconditions, Success Guarantee, Level, Complexity, Use Case Status, Implementation Status, Assigned To, Release), a **Flow of Events** table (Main Success Scenario rows, then Extensions `3.a` with numbered steps), Notes and Referenced Requirements.
- **Requirements** (`|REQ-ICE13 Authorization|P10|`) carry a description, sometimes Details, and "Use cases that reference this requirement".
- Tables have a fixed width, and a long row wraps. A row continues the one above when its first word would not have fit there.

## Steps

1. Put the `.doc` files in `uploads/<slug>/` with a `manifest.json` pinning md5 and sha256 (git-ignored). Record the licence decision. A report that states no licence needs the owner's permission before its text is published.
2. Run `python3 src/tools/ingest_use_cases.py` (Tool `ihris-ingest-use-cases`). It stops on any line it does not understand, rather than skip it. Fix the parser, never the output.
3. Check the counts against the report's own table of contents, and check `dangling` (ids the report cites but never describes).
4. Run AGENTS.md §3.

## Rules

- The crosswalk is **name matching only**, and says so on every link (`derivedBy: name-match`). An unmatched use case keeps `matches: null`. Never fill it with a plausible form (AGENTS.md §7).
- Fields that identify people (Assigned To initials, a requirement's named Source) are withheld and counted, unless the owner says otherwise.
