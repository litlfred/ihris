# iHRIS health workforce DAK: draft data dictionary (`ihris-dak`)

A **WHO SMART Guidelines DAK (L2) data dictionary** for health workforce information. It is derived mechanically from the iHRIS 4.3.3 data model (`src/*/data-model/4.3.3/`), which itself comes from the checksum-verified release.

| | |
|---|---|
| data elements | 242 (101 required, 141 optional) |
| logical models | 49, one per iHRIS record form (Person, Demographic, Education, Position, License, Leave, …) |
| value sets | 41, one per iHRIS list used as input options (country, cadre, degree, gender, …) |
| wiki evidence | 156 elements are mentioned in a restored user-manual page |

## Files

- [`data-dictionary.xlsx`](data-dictionary.xlsx) / [`.csv`](data-dictionary.csv): the dictionary in the **WHO column order** of the *Form data mapping guide* (Digital transformation handbook for primary health care, 9789240093362, pp. 86-90), plus a *Value sets* sheet.
- [`data-dictionary/`](data-dictionary/): one `ihris-dak-data-dictionary/v1` sheet per logical model, with full provenance (class, field, I2CE type, defining modules).
- [`core-data-elements/`](core-data-elements/): smart-base `CoreDataElement` instances (`logicalmodel` / `valueset`). They validate against smart-base's own JSON Schema.
- [`value-sets.json`](value-sets.json): which iHRIS list backs each value set, and which elements use it.
- [`excluded.json`](excluded.json): what was left out and why (system, interoperability and list classes; password and remap fields).
- Overview: [docs/generated/dak-data-dictionary.md](../../docs/generated/dak-data-dictionary.md).

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
4. **Value-set codes**: iHRIS ships standard lists (country, currency, ISCO-08, …) in its `formsData`. Extracting them into CodeSystems is the next step.
5. **Canonical**: `https://litlfred.github.io/ihris/dak` is provisional.

Because the dictionary is regenerated, authored columns should go in an overlay keyed by data element ID (planned: `src/ihris-dak/authored/`). They should not be edited into the generated sheets.

Regenerate: `python3 src/tools/build_dak.py && python3 src/tools/validate.py`.
