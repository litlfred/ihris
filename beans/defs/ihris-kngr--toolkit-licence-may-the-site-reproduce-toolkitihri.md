---
# ihris-kngr
title: 'Toolkit licence: may the site reproduce toolkit.ihris.org text?'
status: completed
type: task
tags:
created_at: 2026-09-23T13:37:09Z
updated_at: 2026-09-23T13:37:09Z
---

No licence is recorded for toolkit.ihris.org. None is stated in the captured pages under `uploads/toolkit/*.html`, and none is recorded in `library/ihris-toolkit`. So the site shows the toolkit's structure only: stages, taglines, domains and tool titles, each linking back (AGENTS.md §2.4).

The owner decides whether the ingested text (the stage intros, objectives, challenges and technical terms in `library/ihris-toolkit/stages/*.json` and `sections/*.md`) may be published. If yes, record the licence and basis in `library/ihris-toolkit/ihris-toolkit.json`, and `site_instances.toolkit_pages` can render the text.

## Decision (2026-09-23)

- **The owner's answer:** asked whether they, or IntraHealth through them, grant permission, the owner answered "I have permission". That is recorded as `licence.status: permission` in `library/ihris-toolkit/ihris-toolkit.json`, with who granted it, when, the basis, the scope and the exclusions. It is validated by `ihris-instance-extension/v1`.
- **The site:** `site_instances.toolkit_pages` publishes the stage introductions, objectives with their tools, challenges, technical terms and graphics, with attribution. It publishes the text only while that record exists.
- **Reader comments:** comments from the original site, with their authors' names, are excluded, because they are third-party personal content. The build output was checked to contain no comment author's name.
- AGENTS.md §2.4 now says how a recorded licence or permission lifts headings-only.
