---
# ihris-rluc
title: 'Use-case roles: merge ''Any User''; derive useCases from primary actors'
status: completed
type: task
tags:
    - library
    - scenarios
created_at: 2026-09-24T00:00:00Z
updated_at: 2026-09-24T00:00:00Z
---

The owner's answers, 2026-09-24, to the open questions of PR [#17](https://github.com/litlfred/ihris/pull/17) (bean `ihris-actr`), tracked in issue [#20](https://github.com/litlfred/ihris/issues/20):

1. *"Any User" in A-ICE4 and A-PS6 is the same role.* Merge them into one role, citing both sources.
2. *Fill each role's `useCases` from the actors' goals in the 2009 reports.* Link each role to the use cases the reports list it as primary actor on, derived from the source only.

## What was built

- `src/tools/ingest_use_cases.py`:
  - `SAME_ROLE` joins A-PS6 (Qualify) to A-ICE4 (Common): one role, `ihris-a-ice4`, whose `_sources` cites both actors and their reports. The tool stops if the two reports differ in title or description, so no merged text is ever written. Every role now carries `_sources`. 15 roles become 14.
  - The links: folio-assistant's `RoleDefSchema` is strict and has no `useCases` (a story points at its role, folio-assistant #1168, merged just after #17). So each (role, use case) pair whose use case names the role in "Primary Actors" is a user story in `scenarios/stories.json` (`UserStorySchema`), with id `<role id>-<use-case id>` and `want` the use case's title, verbatim. That makes 145 stories. The tool stops if an actor's own list ("Use cases that this actor plays a role in") disagrees for a use case the reports describe.
- `validate-folio.ts` now reads the role graph with folio-assistant's `readRoleGraph`, which treats `_` keys as documentation, and `stories.json` with `readUserStories` and `danglingStoryRoles`.
- QA (`src/tools/qa.py`): `role-graph` is rewritten to check that no id appears twice, that no title appears twice within a product, that every described actor is cited by exactly its role, and that the owner's merge cites both. Only owner-listed merges are allowed. The new checks are `role-use-cases` (each story resolves to a declared role and a described use case, title verbatim) and `role-use-cases-primary` (each link is backed by Primary Actors, and none is missing). Each check was mutation-tested.
- Site: the roles page lists both actors of the merged role, and "Primary actor on" is read from `stories.json`.

## Left with no link, from the source

- A-PS5 Decision Maker: no use case names it as primary actor.
- Use cases that an actor lists but the reports never describe (dangling): UC-PS26 (A-PS1), UC-PP11, 13, 14, 15, 20, 22 and 23 (A-PP1). They get no story, because a link must resolve to a real use case.
