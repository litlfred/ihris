# Round 1: the iHRIS 4 data model on just-the-docs

Process: [`wireframe-design-review`](../../../../processes/wireframe-design-review.bpmn) (methodology `wiregen`).

| step | state |
|---|---|
| intent | [`intent.md`](intent.md) |
| candidates | [`a.html`](a.html) (catalogue first), [`b.html`](b.html) (graph and detail). Each has a web and a mobile layout. C (record-centric) is considered and deferred; the reason is in `intent.md`. |
| mechanical checks | `checks/report.json`: all `pass` at web 1280×800 and mobile 390×844 (renders, no-overflow, no-placeholder). Screenshots are in `checks/`. |
| blind review | agent entries: [`reviews/agent-1.json`](reviews/agent-1.json) (non-author, blind). A: pass on intent-fit, web and mobile; warn on accessibility and alternatives. B: pass on web and alternatives; warn on intent-fit, mobile and accessibility. Two factual issues, both minor: `I2CE_Form` should be marked as a base or external class, and the 156 records vs 153 classes difference is not explained. **The human review is recorded:** [`reviews/human-1.json`](reviews/human-1.json). B's mobile layout passes (the list on phones is accepted). A and B both get warnings on accessibility (A: a tile that is not a real link and a search that is not an input; B: the graph has no text twin and the search is not an input). |
| adjudication | [`adjudication.json`](adjudication.json). One disagreement, B's mobile usability (agent-1 warn, human-1 pass). It is settled as pass with a dispensation: the hybrid uses A's field cards. |
| choice | [`decision.json`](decision.json). The owner chose the **hybrid A + B**. A and B are kept as rejected-as-drawn, with the reason each lost. The intent is revised: [round 2](round-2/). |

## Round 2: the hybrid

| step | state |
|---|---|
| intent | [`round-2/intent.md`](round-2/intent.md): A's structure plus B's neighbourhood, and the five fixes round 1 carried forward |
| candidate | [`round-2/h.html`](round-2/h.html) (catalogue with neighbourhood) |
| mechanical checks | `round-2/checks/report.json`: all `pass` at web and mobile |
| blind review | [`round-2/reviews/agent-2.json`](round-2/reviews/agent-2.json) (non-author, blind). Intent-fit, web and alternatives pass. Mobile warns: the opened menu is not drawn. Accessibility warns on five smaller points (cards strip table semantics, a label with no role, no skip link, decorative glyphs are not hidden, the graph's name is its legend). Carry-forward fixes 1–4 pass; fix 5 warns because the 156/153 note is hidden on phones. Every fact matches the data, but the counts include an extraction artefact, `formClass`, filed as bean `ihris-73by`. |
| acceptance | open: the owner accepts H, or sends it round again |

`authors.json` records who made each candidate. Reviewers should not open it.
