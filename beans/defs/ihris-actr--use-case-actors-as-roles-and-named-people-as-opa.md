---
# ihris-actr
title: Use-case actors as Roles, and named people as opaque actors
status: completed
type: task
tags:
    - library
    - licence
    - scenarios
created_at: 2026-09-23T21:00:00Z
updated_at: 2026-09-23T21:00:00Z
---

The owner's direction for the 2009 use cases (`library/ihris-use-cases`, bean `ihris-hbuc`), 2026-09-23: *"Actors can be instantiated.... actor schema instancnes could then be referenced."* It is step 6 of section 5 in folio-assistant's `cat-harness/docs/proposals/odrl-prov-actor-model.md`, from folio-assistant issue [#1180](https://github.com/litlfred/folio-assistant/issues/1180) (W3C ODRL 2.2 policies and PROV-O, merged in folio-assistant PR #1199).

## Decisions (owner, 2026-09-23)

- **Use-case actors are Roles** in the iHRIS domain, not people.
- **Staff:** one opaque Actor per distinct person.
- **Identity:** the mapping from a person to their actor lives in the data store only, and is never written into the repository.

## What was built

- `library/ihris-use-cases/scenarios/` (declared with `graphKinds: ["scenarios"]` in `ihris-use-cases.json`):
  - `roles.json`: 15 Roles, one per actor the reports describe (4 Common, 4 Manage, 6 Qualify, 1 Plan), validated with folio-assistant's own `RoleGraphSchema`. The id is `ihris-` and the A-id in lower case; title and description are the report's own, verbatim. A-ICE4 and A-PS6 ("Any User") stay two roles, and their equivalence is undecided (decided 2026-09-24: one role, bean `ihris-rluc`). A-PT9 is cited only in the Manage table of contents and has no description, so it is no role.
  - `actors/ihris-2009-staff-01.json` and `-02.json`: one opaque actor per distinct person named in "Assigned To" (12 Manage use cases) or a requirement's "Source" (12 Qualify requirements), in folio-assistant's `ActorDef` shape (validated strict: nothing but id, title, kind, description).
- `src/tools/ingest_use_cases.py` resolves each use case's primary and supporting actors to role ids (145 references; by name within the product, then Common; an unresolved name stops the build), and emits `assignedTo` / `source` as `{"actor": "ihris-2009-staff-NN"}`. It ends with a leak check over its output and a site built into a temporary directory. That check lives in the ingester because only it holds the uploads.
- QA (`src/tools/qa.py`): `use-case-roles`, `use-case-staff-refs`, `role-graph`, `staff-actors`, each with a mutation test that shows it can fail.
- Site: product pages link actors to `library/use-cases/roles.html`, and show "Assigned to: 2009 iHRIS staff member 01 (identity withheld)". The link checker now also checks #fragments outside the restored wiki.

## Deliberately not done

- The Roles carry no `lanes`. folio-assistant's `RoleDefSchema` is strict and has no such field: a role does not list its lanes (folio-assistant #1168).
- The opaque actors carry no `@type: prov:Person` and no `identities` entry. Both are in the proposal (section 2.1), but `ActorDefSchema` has no field for either yet.
- A Source value's parenthesised qualifier (after the name) is part of the withheld field and is not published.
