# iHRIS health workforce DAK: draft data dictionary (`ihris-dak`)

A **data dictionary** for health workforce information, laid out in the column order of WHO's DAK L2 guide. iHRIS is independent: it is not a SMART Guidelines DAK and does not depend on smart-base (owner ruling, 2026-09-23). It is derived mechanically from the iHRIS 4.3.3 data model (`src/*/data-model/4.3.3/`), which itself comes from the checksum-verified release.

| | |
|---|---|
| data elements | 242 (101 required, 141 optional) |
| logical models | 49, one per iHRIS record form (Person, Demographic, Education, Position, License, Leave, …) |
| value sets | 47: 41 used as input options, plus 6 reached only through other lists' properties (e.g. degree → education type, salary grade → currency). 12 ship default codes, 24 ship sample data only, 11 are defined by each deployment |
| wiki evidence | 156 elements are mentioned in a restored user-manual page |

## Files

- [`data-dictionary.xlsx`](data-dictionary.xlsx) / [`.csv`](data-dictionary.csv): the dictionary in the **WHO column order** of the *Form data mapping guide* (Digital transformation handbook for primary health care, 9789240093362, pp. 86-90), plus a *Value sets* sheet.
- [`data-dictionary/`](data-dictionary/): one `ihris-dak-data-dictionary/v1` sheet per logical model, with full provenance (class, field, I2CE type, defining modules).
- [`value-sets.json`](value-sets.json): which iHRIS list backs each value set, and which elements use it.
- [`excluded.json`](excluded.json): what was left out and why (system, interoperability and list classes; password and remap fields).
- Overview: [docs/generated/dak-data-dictionary.md](../../docs/generated/dak-data-dictionary.md).

## Terminology (`terminology/`)

FHIR R4 JSON is generated from the records iHRIS ships in `formsData` (`src/*/data-lists/4.3.3/`). It is validated with `fhir.resources` (R4):

| resource | what it holds |
|---|---|
| `CodeSystem-<list>.json` (12) | **default** records, which install with their module. `content: complete` *as shipped*; deployments add their own. Codes are the iHRIS record ids |
| `CodeSystem-<list>-example-<module>.json` (28) | **sample** records from `SampleData-*` modules. `content: example`, and **no ValueSet includes them** |
| `ValueSet-<list>.json` (47) | includes the default CodeSystem. It has no `compose` when iHRIS ships no default records |

The lists that ship real codes are `benefit_recurrence` (4), `competency_evaluation` (3), `country` (246), `currency` (162), `exam_result` (3), `exam_try` (3), `gender` (2), `language_proficiency` (5), `leave_status` (3), `registration_type` (2), `training_course_evaluation` (4), `training_course_exam_type` (3).

Why sample data is kept apart: `SampleData-country` reuses real ISO codes for demo records. Its `TF` is the made-up "Taifafeki", while ISO `TF` is French Southern Territories. The Manage and Qualify sample lists also disagree under the same id: `id_type` 2 is "…Number" in one and "…Card" in the other.

Other lists that a record points to are linked as Coding properties to the CodeSystem that actually holds the code (e.g. a district's `region`). I2CE CURRENCY values (`currency|<id>=<amount>`) become a decimal amount plus a currency Coding.

## Occupations: ISCO-08 and ISCO-88

iHRIS ships **both ISCO classifications as default data**: ISCO-08 with 10 / 43 / 130 / 436 major, sub-major, minor and unit groups (the full structure), and ISCO-88.

| file | what it is | basis |
|---|---|---|
| `ValueSet-isco_08_{major,sub_major,minor,unit}.json` | the ISCO-08 groups iHRIS ships, as codes of the ILO ISCO-08 system (`http://www.ilo.org/public/english/bureau/stat/isco/isco08/`, the ILO's own system URL) | iHRIS record ids *are* ISCO-08 codes |
| `CodeSystem-isco_88_*.json` | ISCO-88 as shipped (no FHIR canonical for ISCO-88 exists to cite) | shipped default data |
| `ConceptMap-job-to-isco-88-unit.json` | sample jobs → ISCO-88 unit group: 48 mapped, 3 unmatched | the job code's four-digit prefix, kept only where it is a shipped ISCO-88 unit group |
| `ConceptMap-classification-to-isco-88-minor.json` | sample classifications → ISCO-88 minor group: 5 mapped, 1 unmatched | the record's own `code` field |
| `ConceptMap-cadre-to-isco-88-minor.json` | sample cadres → ISCO-88 minor groups: 3 mapped, 1 unmatched | through the cadre's sample jobs; `inexact`, citing the jobs |

Why the maps target **ISCO-88** and not ISCO-08: iHRIS's own sample data is keyed on ISCO-88. For example, job `2221-1D` Medical Doctor sits under ISCO-88 unit 2221, and classification code `223` is ISCO-88 "Nursing and midwifery professionals". Going from ISCO-88 to ISCO-08 is many-to-many and needs the ILO correspondence table. That step is **blocked**, not guessed; see `authored/isco-08.json`, item P2.

## Countries and currencies: ISO 3166-1 and ISO 4217

iHRIS's shipped country ids *are* ISO 3166-1 alpha-2 codes, and its currency ids *are* ISO 4217 codes. So the DAK ValueSets `country` and `currency` **bind to the standards** (`urn:iso:std:iso:3166`, `urn:iso:std:iso:4217`, all current codes). The shipped lists stay as local CodeSystems, because that is what deployments store, and are mapped to the standards:

| ConceptMap | equal | not current | current codes iHRIS lacks | older names |
|---|---|---|---|---|
| `country-to-iso-3166` | 245 | 1 (`AN`, withdrawn 2010, now ISO 3166-3 `ANHH`) | 4 (`BQ`, `CW`, `SS`, `SX`) | 11 |
| `currency-to-iso-4217` | 143 | 19 (e.g. `ZMK`, `GHC`, `MRO`, `EEK`, `LTL`) | 38 (e.g. `ZMW`, `GHS`, `MRU`, `SSP`) | 15 |

Verified against the Debian *iso-codes* data packaged by `pycountry` (the version is recorded in `iso-report.json`). A withdrawn code is `unmatched`: its successor is **not** inferred, because that is a redenomination fact the source does not state. Decisions are in [`authored/iso.json`](authored/iso.json):
- **B1:** the ISO binding. Accepted by the owner.
- **P1 (proposed):** deployments update the 2009-era lists.

## Authored overlay (`authored/`)

The only part of this instance that a person writes and the build never touches. Each file is an `ihris-dak-proposal/v1`: proposals with a rationale, evidence and a status that only the owner changes.

- [`authored/iso.json`](authored/iso.json): B1 (accepted) ISO binding; P1 (proposed) update the outdated lists.
- [`authored/isco-08.json`](authored/isco-08.json):
  - **P1 (accepted by the owner, 2026-09-22):** each deployment maps its cadre and job codes to ISCO-08 unit groups.
  - **P2 (blocked):** ISCO-88 → ISCO-08, pending the ILO correspondence table.
  - **O1 (to verify):** smart-base's ISCO08 CodeSystem holds 182 of 619 groups while declaring `content: complete`, and has a `913` that iHRIS lacks. An upstream issue is drafted in [docs/upstream/smart-base-isco08-codesystem.md](../../docs/upstream/smart-base-isco08-codesystem.md) (not filed).

## How fields were mapped

| iHRIS (I2CE) | DAK data type |
|---|---|
| STRING_LINE / MLINE / TEXT | String |
| DATE_YMD (DATE_Y, DATE_YM, DATE_MD partial) | Date |
| DATE_HMS / DATE_TIME | Time / DateTime |
| YESNO, BOOL | Boolean |
| INT, PERCENT_INT / FLOAT, CURRENCY | Quantity (Integer / Decimal) |
| INT_GENERATE, REFERENCE | ID |
| MAP, ENUM, ASSOC_MAP | List - select one |
| MAP_MULT, ASSOC_LIST | List - select all that apply |
| DOCUMENT, IMAGE | Attachment |

- **Optionality:** `required` → R, otherwise O. C (conditional) is never inferred.
- **Input options:** a MAP field's `meta/form`. Where that is absent, I2CE's default applies: the list form named after the field.
- **Scope:**
  - Record forms become logical models.
  - Lists (the class chain reaches `I2CE_List` or `I2CE_SimpleList`) become value sets.
  - I2CE infrastructure, user and alert state, and RapidPro/DHIS/SVS plumbing are excluded as `system`.
  - The CSD (OpenHIE) classes are kept aside as `interoperability`, for mapping later.

## What a person still has to do

The builder **never invents** these columns: they are `null` until authored.

1. **Descriptions and definitions** (all 242): `descriptionStatus: "to-author"`. Start from the `evidence` wiki pages.
2. **Activity IDs**, once the business processes (L2 BPMN) exist. The toolkit stages and the wiki user manual are the source for them.
3. **Conditionality (C)**, **reasons for requiring**, **indicator linkages** (e.g. WHO National Health Workforce Accounts) and **decision-support linkages**.
4. **Codes for the 24 sample-only and 11 deployment-defined lists**: these are national decisions (cadres, districts, facilities, …). Candidate standards to bind: ISO 3166 (already the iHRIS default for country), ISCO-08 for cadre and occupation.
5. **Canonical**: `https://litlfred.github.io/ihris/dak` is provisional.

Because the dictionary is regenerated, authored columns should go in an overlay keyed by data element ID (planned: `src/ihris-dak/authored/`). They should not be edited into the generated sheets.

Regenerate: `python3 src/tools/build_dak.py && python3 src/tools/validate.py`.
