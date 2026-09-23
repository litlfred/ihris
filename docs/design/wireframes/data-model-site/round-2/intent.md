# Design intent, round 2: the hybrid

The same **who**, **what** and **where** as [round 1](../intent.md). The owner chose the hybrid in round 1 ([`../decision.json`](../decision.json)).

**The candidate:** A's page structure (a package sidebar, then per class a heading, a field table and its source), with B's neighbourhood graph as a section **after** the fields. On phones the graph becomes B's relationships list, and fields become A's labelled cards.

**It must also fix everything round 1 carried forward:**
1. The nav, the visualiser tile and the search are real `<a>` and `<input>` elements.
2. The graph has a text twin: a table of the same edges, and every class in it is a link.
3. The class `h1` comes first in reading order.
4. `I2CE_Form` is marked as a base class. It has no page of its own.
5. The 156 package records vs 153 distinct classes difference is explained where the counts appear.

**One candidate, on purpose.** Round 2 refines a choice the owner already made; it is not a fresh comparison. The review still covers both viewports, and the "alternatives" criterion points back to round 1.
