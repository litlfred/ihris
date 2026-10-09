# Round 1: a dark scheme for the iHRIS site (bean ihris-u3fg)

Process: [`wireframe-design-review`](../../../../processes/wireframe-design-review.bpmn) (methodology `wiregen`).

| step | state |
|---|---|
| intent | [`intent.md`](intent.md): why the grounds are a person's choice and every other colour is derived |
| candidates | A, Manage blue at night ([`a.grounds.json`](a.grounds.json): [`a.html`](a.html), [`a-home.html`](a-home.html)); B, neutral charcoal ([`b.grounds.json`](b.grounds.json): [`b.html`](b.html), [`b-home.html`](b-home.html)). Each is a real built page in the candidate palette (`derive_dark_theme.py --page`), web and mobile. |
| mechanical checks | `checks/report.json`: all `pass` at web 1280×800 and mobile 390×844. Screenshots are in `checks/`. |
| blind review | [`reviews/agent-1.json`](reviews/agent-1.json) (non-author, blind) and the owner's answers, [`reviews/human-1.json`](reviews/human-1.json). |
| choice | [`decision.json`](decision.json): the owner chose **A, with the logo inverted to white**. B is kept with the reason it lost. |
| post-review patch | [`post-review-patch.json`](post-review-patch.json): agent-1's two below-target colours fixed in the derivation (exact ratios; the diagram ink derived against the base-class box too). The checks were re-run. |
| acceptance | **accepted** by the owner, 2026-10-09: [`acceptance.json`](acceptance.json). The site's grounds are [`src/site/theme/ihris-classic-dark.grounds.json`](../../../../src/site/theme/ihris-classic-dark.grounds.json). |

`authors.json` records who made each candidate. Reviewers should not open it.
