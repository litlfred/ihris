# Design intent, round 3: H refined

The same **who**, **what** and **where** as [round 1](../intent.md), and the same design as [round 2's H](../round-2/h.html). The owner chose to fix H's round-2 warnings ([`../round-2/reviews/agent-2.json`](../round-2/reviews/agent-2.json)) before accepting it.

**Candidate H2** ([`h2.html`](h2.html)) and its phone-menu-open state ([`h2-menu.html`](h2-menu.html)) must fix:

1. **Mobile:** draw the opened menu. It shows the package tree, the count note and the visualiser tile, with touch targets at least 44px tall.
2. **Count note on phones:** the 156 / 153 explanation can be reached on a phone (it is in the opened menu).
3. **Skip link:** a "Skip to content" link past the sidebar.
4. **Decorative glyphs:** arrows, the graph icon and the menu icon are `aria-hidden`.
5. **Relationships:** the phone relationships list is a real region (`<section aria-label>`), not a `div` with a label that does nothing.
6. **Fields as cards:** the field table keeps explicit table roles, so screen readers still read it as a table when it becomes cards.
7. **Graph name:** the SVG's accessible name describes its edges; the legend becomes its description.
8. **Info:** the sidebar excerpt shows it is cut at both ends ("68 above", "21 below"), and each list link names its class (`iHRIS_Country`, and so on).

Counts are unchanged by the `ihris-73by` fix: 93 in ihris-common, 156 records, 153 classes.
