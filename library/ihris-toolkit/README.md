# iHRIS Implementation Toolkit (`ihris-toolkit`)

This instance ingests the six stage pages of [toolkit.ihris.org](https://toolkit.ihris.org/), captured by the repository owner on 2026-09-22 (`uploads/toolkit/`).

| | |
|---|---|
| stages | 6: 0 Assess, 1 Plan, 2 Deploy, 3 Pilot, 4 Scale-up, 5 Sustain |
| domains | Governance, Project Management, Software & Systems, Data Sharing & Interoperability, Data Quality & Standards, Training & Support, Data Use & Reporting, Deliverable, Ongoing |
| tools linked | 83 (47 hosted on the toolkit, 36 external) |

- [`sections/`](sections/): readable Markdown, one per stage
- [`stages/`](stages/): the structured `ihris-toolkit-stage/v1` record for each stage
- [`structure.json`](structure.json): the stage × domain matrix; [`tools-index.json`](tools-index.json) lists every tool

**Still referenced, not held:** the 47 tool documents hosted on the toolkit (worksheets, templates, presentations, PDFs). toolkit.ihris.org is egress-blocked from the session that built this. Each one is `"materialization": "referenced"` in `tools-index.json`. Upload any of them to `uploads/toolkit/` to have them ingested.
