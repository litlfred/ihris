# iHRIS 4 on FHIR (`ihris-4-on-fhir`)

**New derived content** (owner, 2026-09-23): the iHRIS 4.3.3 data model expressed in FHIR, derived from `src/ihris-data-dictionary` (the data dictionary and terminology).

**Built on [fhir-harness](https://github.com/litlfred/fhir-harness)**, the bare FHIR IG pipeline with no WHO in it (owner, 2026-10-09). It replaced the smart-base harness and IG this subgraph depended on from 2026-09-23, so nothing in this folio depends on smart-base. The IG depends on `hl7.fhir.r4.core#4.0.1` only (D5).

| status | item |
|---|---|
| done | F1: SUSHI 3.20.1 pinned, `sushi-config.yaml` (R4 core only); F2: terminology as FSH, the JSON is SUSHI's build (D8); F3: 51 logical models (`input/fsh/logical-models/`). Tool `ihris-gen-fsh`, with `ihris-sushi` |
| in progress | F4 (bean `ihris-7gl8`): the logical models mapped to the three iHRIS 5 IGs by Tool `ihris-map-ihris5` (`src/tools/map_ihris5.py`). Evidence only: name and label equality, no synonyms and no judgement. It writes [`mapping/crosswalk.json`](mapping/crosswalk.json), the two-way gap report [`mapping/gaps.md`](mapping/gaps.md), and one StructureMap per mapped model and IG in `input/fsh/maps/`. What the evidence does not decide waits on the owner in `src/ihris-data-dictionary/authored/ihris5-mapping.json` |
| blocked on the lightweight IG render pipeline | F5: render and publication (`ihris-bwls`) |

### F4: how the mapping is made

1. **Index.** The three iHRIS 5 IGs (`ig/`, `ihris-backend/ihris-backend-site/ig`, `qualify-ig`), as pinned in `src/ihris5/ihris5.json` and mounted at `ihris5-source/`, are compiled with SUSHI in `.build/ihris5-sd/`. What compiles is indexed in [`mapping/ihris5-index.json`](mapping/ihris5-index.json): names, element paths, labels, types and bindings, with each compiled file's sha256. No FSH is copied. SUSHI's errors are kept there as upstream defects.
2. **Match.** A model matches a profile when one of its names equals the profile's (or its top-level complex extension's) name, id or title, or when most of its elements have a label-equal element in that profile. An element matches when its I2CE label equals the element's label, its extension's value label or title, or a Questionnaire item's text on it. One type-compatible candidate is `exact`; several, or one of the wrong type, is `ambiguous`; and none is `none`.
3. **Decide.** Each ambiguous match becomes a proposal, listing only the candidates the matcher found (or the bean's own examples, cited as such). When the owner accepts one, with `selected`, it drives the next run (`accepted`). A rejected proposal's candidates are not matched again.
4. **Generate.** StructureMaps carry only the exact and accepted element rules. Their source is the logical model's canonical, and their target is the iHRIS 5 profile's canonical, as a URL only. iHRIS 5 is not an IG dependency (D5).

Design: [`docs/design/fhir-strategy.md`](../../docs/design/fhir-strategy.md).
