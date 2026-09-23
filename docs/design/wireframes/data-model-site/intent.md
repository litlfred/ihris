# Design intent: the iHRIS 4 data model on just-the-docs

**Who:** an iHRIS implementer, analyst or data manager. They know HR data, not I2CE internals. They may be on a laptop or on a phone.

**What they need to do:**
1. Find a record type (for example *Person*, *Position* or *Education*) by package, by name, or by searching.
2. See its fields: label, type, required or not, and the list a coded field draws from.
3. See how it relates to other types: what it extends, what extends it, and which lists it references.
4. Trace every fact back to the module and release that define it.

**What it must show:** real iHRIS 4.3.3 content. There are 156 form-class records (153 distinct classes) in 4 packages: i2ce 12, ihris-common 93, ihris-manage 26 and ihris-qualify 25. Each has its fields and its `extends` and `references` edges.

**Where:** folio-assistant's just-the-docs pipeline, with a **harness visualiser** declared on the data-model subgraph. The visualiser becomes a tile on the navbar and board (`harness-tiles`). The whole site must stay readable linearly, which is the just-the-docs accessibility floor from folio-assistant `6lb8`.

**Both layouts:** web (1280 wide) and mobile (390 wide) are required for every candidate.

## Candidates

- **A: catalogue first.** Just-the-docs pages per package and class. The visualiser is a separate tile page.
- **B: graph and detail.** The visualiser is on the class page: a neighbourhood graph beside the detail. On mobile it becomes a relationships list.

**Considered and deferred: C, record-centric.** The person record as HR staff see it, with child records as tabs. It is deferred because the parent/child form links are **not yet extracted** from the modules (`build_kg.py` does not read child forms). Drawing it now would invent relations. It can come back once that extraction exists.
