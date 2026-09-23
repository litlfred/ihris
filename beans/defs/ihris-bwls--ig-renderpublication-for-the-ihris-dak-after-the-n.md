---
# ihris-bwls
title: 'IG render/publication for the iHRIS DAK: after the new lightweight IG render pipeline is done'
status: draft
type: task
tags:
    - fhir
    - paused
    - blocked-upstream
created_at: 2026-09-23T06:23:42Z
updated_at: 2026-09-23T06:23:42Z
parent: ihris-g768
blocked_by:
    - ihris-dmgf
---

Owner, 2026-09-23: *"bean up for IG publisher also needs first new lightweight IG render pipeline is done"*.

Rendering or publishing the iHRIS DAK IG (HTML, gh-pages) waits for **two** things:

1. the design gate `ihris-dmgf` (D7: sushi + validation only in this phase), and
2. **folio-assistant's new lightweight IG render pipeline being done**, which is upstream. The relevant platform beans are:
   - [jut3](https://github.com/litlfred/folio-assistant/blob/main/beans/defs/folio-assistant-jut3--smart-via-just-the-docs-stop-mounting-ig-publisher.md): smart-* via just-the-docs; render `input/pages` from post-processed JSON-LD instead of mounting IG Publisher HTML
   - [kn0t](https://github.com/litlfred/folio-assistant/blob/main/beans/defs/folio-assistant-kn0t--phased-transition-ig-publisher-reduced-to-ast-qa-i.md): IG Publisher reduced to AST + QA, in five phases
   - [nsbb](https://github.com/litlfred/folio-assistant/blob/main/beans/defs/folio-assistant-nsbb--ig-pipeline-layering-a-bare-fhir-ig-pipeline-is-th.md): a bare FHIR IG pipeline as the base, with DAK/SMART as overlays

Until both are done, do not run the IG Publisher or generate HTML for this folio. This bean is phase F5 of `docs/design/fhir-strategy.md`.
