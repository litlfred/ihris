---
# ihris-91d2
title: 'folio-assistant: define a schema for pdf-structure/v1'
status: completed
type: task
tags:
    - upstream
created_at: 2026-09-23T13:26:39Z
updated_at: 2026-09-23T13:26:39Z
---

folio-assistant's library-ingestion (`pdf-structure.py`) writes `structure.json` tagged `_schema: pdf-structure/v1`, but defines no schema for that tag anywhere (checked 2026-09-23 on origin/main: no zod schema and no JSON Schema). ihris validates the keys it reads with a local stand-in, `src/schemas/pdf-structure.schema.json`. When folio-assistant defines the schema, bind to it and delete the stand-in (AGENTS.md §2.6: reuse folio-assistant's schemas first).

## Outcome (2026-09-23)

- folio-assistant now defines `pdf-structure/v1`: `cat-harness/schemas/pdf-structure.ts`, issue litlfred/folio-assistant#1112, PR litlfred/folio-assistant#1113. `check-l1-complete` checks it.
- ihris validates `library/*/structure.json` with it in `validate-folio.ts`. The local stand-in `src/schemas/pdf-structure.schema.json` and its binding are deleted.
- The new schema caught a defect in ihris's own file: a non-standard `sections_text` key, and no `source.mtime`. Both are fixed in 131188d.
- Measured upstream and recorded there, not fixed: the text origin has two spellings (folio-assistant-hn0l).
