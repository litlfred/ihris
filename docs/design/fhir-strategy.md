# Design strategy: how the iHRIS DAK becomes FHIR

> **Status: approved by the owner, 2026-09-23 (gate `ihris-dmgf` completed).** Decisions are in §0. **iHRIS is independent: it is not a SMART DAK and is not related to smart-base.** Sections 3 onward keep the original options for the record; where §0 differs, §0 wins. The rules in force are in [AGENTS.md §8](../../AGENTS.md).

## 0. Owner decisions so far

| # | decision | by, on |
|---|---|---|
| — | **iHRIS is independent.** It is not a SMART DAK, and not related to smart-base. | owner, 2026-09-23 |
| D1 | **A, amended**: the FHIR content lives in this repository and is **independent** (no smart-base). iHRIS 5 is mapped to, not edited. | owner, 2026-09-23 |
| D2 | **b**: Python generates FSH, and sushi is the build (it must run clean). | owner, 2026-09-23 |
| D4 | **1**: canonical `https://litlfred.github.io/ihris/dak`. | owner, 2026-09-23 |
| D6 target | **All three iHRIS 5 IGs**: `ig/`, `ihris-backend-site/ig` and `ihris-backend-site/qualify-ig`. | owner, 2026-09-23 |
| D3 | **ii**: logical models wait for smart-base's DAK model (folio-assistant `cz17`). | owner, 2026-09-23 |
| D5 | **R4 core only**: `hl7.fhir.r4.core#4.0.1`, with no smart-base dependency. | owner, 2026-09-23 |
| D6 format | **γ**: StructureMaps, as executable transforms. | owner, 2026-09-23 |
| D7 | Sushi and validation only, with no IG Publisher and no HTML in this phase. | owner, 2026-09-23 |
| D8 | Keep the terminology JSON until the sushi output is equal in content, then switch in one commit. | owner, 2026-09-23 |

### Later rulings (owner, 2026-09-23, after the gate)

| # | ruling |
|---|---|
| subgraph | The FHIR content is **new derived content in its own subgraph, `src/ihris-4-on-fhir`**, and *that* subgraph depends on the **smart-base harness and IG**. The rest of iHRIS stays independent. This supersedes D5 ("R4 core only") **for this subgraph**, and it is consistent with D3 (wait for `cz17`). |
| timing | **SUSHI later.** Document the skills, processes and tools now: skill `ihris-4-on-fhir`, `processes/ihris-4-on-fhir.bpmn`, Tool `ihris-sushi`. |
| rename | `ihris-dak` is to be renamed. The new name is not yet chosen. |
| focus | Now: modelling the iHRIS 4 data model on just-the-docs, with a harness visualiser. |

### Consequences

1. **The smart-base CoreDataElements were removed** (the 121 files, and their generation and validation), because of the independence ruling.
2. **D6 γ depends on D3.** A StructureMap needs a source StructureDefinition, and that source is the iHRIS 4 logical models, which D3 defers until folio-assistant `cz17`. Now that iHRIS is independent of smart-base, whether logical models should still wait for `cz17` is **open for the owner** (bean `ihris-ct58`).
3. **Unpaused by the gate:** F1 (the SUSHI skeleton, bean `ihris-dipr`) and F2 (terminology as FSH, then the D8 switch, bean `ihris-ej94`). Logical models, the iHRIS 5 mapping and publication stay blocked.

## 1. Where we are (measured, 2026-09-23)

| what | state |
|---|---|
| L2 data dictionary | `src/ihris-dak/data-dictionary`: 242 data elements in 49 logical models (one per I2CE form class), in WHO column order. It is not FHIR. |
| Terminology | `src/ihris-dak/terminology`: 44 CodeSystems, 57 ValueSets and 5 ConceptMaps. These are FHIR R4 **JSON** written directly by `build_dak.py`, with no FSH and no sushi. `validate_fhir.py` checks their structure (`fhir.resources` 6.5). |
| CoreDataElements | Removed 2026-09-23 (independence ruling). |
| Canonical | `https://litlfred.github.io/ihris/dak`, confirmed by the owner 2026-09-23 (D4, bean `ihris-gj3u` completed). |
| iHRIS 5 IG | `iHRIS/iHRIS@fa66e9b` `ig/`: canonical `http://ihris.org/fhir`, version 0.1.0, FHIR 4.0.1. Its only dependency is `hl7.fhir.r4.core`, and it does **not** depend on smart-base. It uses a custom template (`input/ihrisigtemplate`), and its `sushi-config.yaml` was migrated from a SUSHI 0.x `package.json`. It has 436 FSH definitions in `ig/input/fsh`, plus two more IGs under `ihris-backend-site/` (`ig` 174, `qualify-ig` 74). The repository is LGPL-3.0; the IG declares CC0-1.0. |
| smart-base | *Not a dependency (owner ruling).* Kept here for context: it publishes `SGLogicalModel`, `SGValueSet`, `SGCodeSystem`, `SGConceptMap` and the `DAK` logical model (folio-assistant `smart-base/fhir-artifact-index`, v0.3.0). The DAK *metadata* model (`dak.json`) is still pending upstream (folio-assistant bean `cz17`). |

## 2. Principles that do not change

These are already rules, and every option below respects them.

1. **Derived never invents** (AGENTS.md §7). A FHIR element carries what the source states. Definitions, conditionality and linkages stay empty until a person authors them in `authored/`.
2. **Generated means generated.** FHIR output is build output. People change the inputs or the generator, never the output.
3. **Sushi runs clean before any commit that contains FSH** (owner preference).
4. **Describe, do not materialize,** third-party sources. The iHRIS 5 FSH is read and cited by commit and path. It is not copied in.
5. **Only the owner** moves a proposal's `status`, or completes a gate bean.

## 3. Decisions for the owner

### D1. What this repository produces

| option | meaning |
|---|---|
| **A (recommended)** | This repository produces an **iHRIS DAK**: a DAK-style FHIR IG built on smart-base, holding the L2 content (logical models, terminology, CoreDataElements) derived from iHRIS 4.3.3. iHRIS 5 is a separate implementation that the DAK is **mapped to** (D6). This repository does not edit iHRIS 5. |
| B | Contribute the DAK content into `iHRIS/iHRIS`'s IG. |
| C | Both: build here, then upstream selected parts. |

*Why A:* it keeps the provenance chain (verified tarball → generator → FHIR) in one repository. It also needs no write access to, or agreement from, iHRIS/IntraHealth. C remains possible later, and A does not block it.

### D2. Source format and build

| option | meaning |
|---|---|
| a | Keep generating FHIR JSON from Python, as today. |
| **b (recommended)** | Python **generates FSH** into a generated directory (for example `src/ihris-dak/fsh/`). **Sushi is the build**, and `validate.py` fails unless sushi reports 0 errors. The authored overlay stays as JSON proposals, which the generator renders into FSH. |
| c | Hand-author the FSH. |

*Why b:* it matches how the smart-* DAKs and iHRIS 5 are built. It also makes sushi the conformance check your rule asks for, and FSH diffs are reviewable. Option c would break "derived never invents", because 242 hand-typed elements would drift from the source.

*Prerequisite:* a pinned SUSHI version, run with Node in the session. Whether it installs here is not yet measured.

### D3. Logical model format

| option | meaning |
|---|---|
| **i (recommended)** | Make one `StructureDefinition` (kind `logical`) per form class (49), conforming to smart-base's `SGLogicalModel`. Elements come from the data dictionary, types come from the existing I2CE→DAK type map, and coded elements bind to our ValueSets. |
| ii | Wait until smart-base's DAK model (cz17) is final. |

*Why i:* cz17 is about `dak.json`, the DAK's *metadata*. It is not about the per-DAK logical models, which smart-* IGs already publish as `SGLogicalModel`. So D3 does not need to wait. Writing `dak.json` does, and it should wait until cz17 settles.

*Not verified yet:* the exact constraints `SGLogicalModel` places on a logical model. This needs a smart-base checkout, which is not in this session's scope.

### D4. Canonical URL

| option | meaning |
|---|---|
| **1 (recommended, for now)** | `https://litlfred.github.io/ihris/dak`, a namespace you control. |
| 2 | Under `http://ihris.org/fhir/…`. This is IntraHealth's namespace and needs their agreement. |
| 3 | A WHO `smart.who.int` canonical. Not ours to claim. |

*Decide before any FSH exists.* Every CodeSystem, ValueSet and ConceptMap URL depends on the canonical, so changing it later means reissuing every artefact.

### D5. Dependencies

The recommendation is:
- `hl7.fhir.r4.core#4.0.1`, the same FHIR version as iHRIS 5, so the mapping in D6 is version-aligned.
- `smart.who.int.base`, pinned to one version.
- ISCO and ISO referenced by their external system URLs, as today.

*Caveat:* smart-base's `ISCO08` CodeSystem holds 182 of 619 groups while declaring `content: complete` (draft upstream issue, bean `ihris-xbqd`). Until that is fixed, we keep our own ISCO-08 ValueSets and do not bind to `ISCO08ValueSet`.

### D6. How the iHRIS 5 mapping is expressed (bean `ihris-7gl8`)

| option | meaning |
|---|---|
| **α (recommended)** | Use `StructureDefinition.mapping` on each logical model (identity `ihris5`, uri `http://ihris.org/fhir`) and per-element `mapping.map` entries naming the iHRIS 5 profile path or extension. Also produce a generated two-way gap report. Every non-obvious match starts as an `authored/` proposal. |
| β | ConceptMaps. |
| γ | StructureMaps (executable transforms). |

*Why α:* ConceptMap maps **codes**, not elements. StructureMap is an executable migration, which is a larger commitment that should come after the map is agreed. `mapping` is FHIR's own place for "this element corresponds to that element".

*Input needed:* the iHRIS 5 FSH content, read by commit (LGPL). Only names are inventoried now.

### D7. Pipeline scope for this phase

The recommendation is **sushi + validation only**: no IG Publisher and no HTML. Publication follows the platform's layering (folio-assistant `nsbb`: a bare IG pipeline as the base, with DAK/SMART as overlays) and its phased transition (`kn0t`), once those are approved. Caching compiled output (`gpdo`) is out of scope here.

### D8. Retiring the current terminology JSON

The recommendation is to keep the JSON until the sushi build of the same content is **equal in content**: same codes, displays, `content` flags, compose rules and ConceptMap rows, compared by a script. Then switch in one commit. Nothing is dropped silently.

## 4. Proposed phases (only after `ihris-dmgf` is completed)

| phase | does | exit criterion (measured) |
|---|---|---|
| F0 | Owner reviews this document | `ihris-dmgf` completed, with D1 to D8 answered |
| F1 | Pin SUSHI; create an empty IG skeleton (`sushi-config.yaml`, dependencies) | sushi: 0 errors, 0 warnings; `validate.py` runs it |
| F2 | Terminology as generated FSH | content-equal to today's JSON (D8); JSON path retired |
| F3 | 49 logical models as generated FSH (`SGLogicalModel`) | sushi clean; every data element present, and no field filled that the source leaves null |
| F4 | iHRIS 5 mapping (D6) | every logical model has a `mapping`; gap report generated; uncertain matches are proposals |
| F5 | Publication (bean `ihris-bwls`) | blocked until folio-assistant's new lightweight IG render pipeline is done (`jut3`, `kn0t`, `nsbb`) |

Each phase is its own bean, blocked by the one before.

## 5. Risks and unknowns

- **Tooling:** SUSHI availability and version in the session has not been measured.
- **`SGLogicalModel` constraints** are unverified (D3).
- **Canonical churn** (D4) is the costliest decision to reverse.
- **iHRIS 5 is itself 0.1.0 and CI-build status.** A mapping to it should be pinned to one commit and re-run when that commit changes.
- **Three iHRIS 5 IGs**, not one (`ig`, `ihris-backend-site/ig`, `qualify-ig`). Which of them the mapping targets is part of D6.

## 6. Related work

- **This folio:** epic `ihris-g768`, gate `ihris-dmgf`, and the paused beans `ihris-7gl8`, `ihris-ct58`, `ihris-ej94`, `ihris-gj3u`.
- **folio-assistant:** `cz17` (the DAK model), `nsbb` (IG layering), `kn0t` (phased transition), `gpdo` (compiled-artefact caching), `cpmo` (smart-base crosswalks), `qrnz` (second-IG generalisation).
