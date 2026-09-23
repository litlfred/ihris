---
# ihris-91d2
title: 'folio-assistant: define a schema for pdf-structure/v1'
status: todo
type: task
tags:
    - upstream
created_at: 2026-09-23T13:26:39Z
updated_at: 2026-09-23T13:26:39Z
---

folio-assistant's library-ingestion (`pdf-structure.py`) writes `structure.json` tagged `_schema: pdf-structure/v1`, but defines no schema for that tag anywhere (checked 2026-09-23 on origin/main: no zod schema and no JSON Schema). ihris validates the keys it reads with a local stand-in, `src/schemas/pdf-structure.schema.json`. When folio-assistant defines the schema, bind to it and delete the stand-in (AGENTS.md §2.6: reuse folio-assistant's schemas first).
