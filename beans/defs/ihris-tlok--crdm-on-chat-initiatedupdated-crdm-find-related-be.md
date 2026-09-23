---
# ihris-tlok
title: 'CRDM: on chat-initiated/updated CRDM, find related beans and issues, categorize and summarize, ask to coordinate'
status: todo
type: task
tags:
    - upstream
    - needs-owner
created_at: 2026-09-23T07:07:42Z
updated_at: 2026-09-23T07:07:42Z
parent: ihris-um1h
---

Owner, 2026-09-23: *when CRDM is initiated/updated through human agent chat discussions existing beans need to be searched for relevance and categorized (and summarized), same for issues (e.g. github). ask user if they want to coordinate. judgement is used to determine how.*

Target: folio-assistant [`methodologies/crdm/`](https://github.com/litlfred/folio-assistant/blob/main/cat-harness/methodologies/crdm) (its skills and its processes). This is the same step as A_Relate + O_Coordinate in `processes/methodology-from-source.bpmn`, which could be extracted as a shared sub-process and called from both. Needs folio-assistant access.
