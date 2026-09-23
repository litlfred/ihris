# Round 1: the iHRIS 4 data model on just-the-docs

Process: [`wireframe-design-review`](../../../../processes/wireframe-design-review.bpmn) (methodology `wiregen`).

| step | state |
|---|---|
| intent | [`intent.md`](intent.md) |
| candidates | [`a.html`](a.html) (catalogue first), [`b.html`](b.html) (graph and detail). Each has a web and a mobile layout. C (record-centric) is considered and deferred; the reason is in `intent.md`. |
| mechanical checks | `checks/report.json`: all `pass` at web 1280×800 and mobile 390×844 (renders, no-overflow, no-placeholder). Screenshots are in `checks/`. |
| blind review | agent entries: [`reviews/agent-1.json`](reviews/agent-1.json) (non-author, blind). A: pass on intent-fit, web and mobile; warn on accessibility and alternatives. B: pass on web and alternatives; warn on intent-fit, mobile and accessibility. Two factual issues, both minor: `I2CE_Form` should be marked as a base or external class, and the 156 records vs 153 classes difference is not explained. **The human review is open.** |
| adjudication / choice | **open.** The owner decides. |

`authors.json` records who made each candidate. Reviewers should not open it.
