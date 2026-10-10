# iHRIS 5 IG defects, drafted for iHRIS/iHRIS

These were found while building the three iHRIS 5 Implementation Guides with fhir-harness (skill `build-ihris5-ig`) and mapping
the iHRIS 4 logical models to them (F4, bean `ihris-7gl8`). The source is
[iHRIS/iHRIS@fa66e9b](https://github.com/iHRIS/iHRIS/tree/fa66e9b375e38525236d28459ec5e5eb3875e2b2), which is `master`
on 2026-10-09. The compiler is SUSHI 3.20.1 against `hl7.fhir.r4.core#4.0.1`.

Each section below is one issue, ready to file. **Not filed yet:** on 2026-10-09 GitHub refused to create issues on iHRIS/iHRIS for this account (`403 Resource not accessible by integration`). The five defects were re-checked on `master` and none is covered by an existing issue (all 41 open and closed issues read). Someone with issue rights on iHRIS/iHRIS files them, or the account gets access. This folio works around defects 1 and 2 in workspace copies only (`src/ihris5/ig-build-patches.json`:
`role-primary-context`, `qualify-include-location`, `qualify-residence-jurisdiction`; owner, 2026-10-09: "do the #2
qualify local fix"). Delete each patch when the pin moves past its fix.

---

## 1. `IhrisRolePrimary` sets `^context[1]` with no `context[0]`, so the IG Publisher cannot read the extension

**Where:** `ig/input/fsh/IhrisRole.fsh`, Extension `IhrisRolePrimary` (`ihris-role-primary`). The two backend IGs reach it
through their `input/fsh/core` symlink.

```fsh
Extension:      IhrisRolePrimary
Id:             ihris-role-primary
...
* ^context[1].type = #element
* ^context[1].expression = "IhrisRole"
```

**What happens:**
- SUSHI warns `The array 'context' in ihris-role-primary is missing values at the following indices: 0` and writes
  `"context": [null, {"type": "element", "expression": "IhrisRole"}]`.
- The IG Publisher (2.3.4) then stops with `Not a JSON Object: null` while it loads the StructureDefinition, so none of
  the three IGs can be published.

**Fix:** the extension has exactly one context, so index 0 is what was meant:

```fsh
* ^context[0].type = #element
* ^context[0].expression = "IhrisRole"
```

---

## 2. `qualify-ig` references `IhrisFacility`, which only the manage IG defines, and `IhrisJurisdiction`, which nothing defines

**Where:**
- `ihris-backend/ihris-backend-site/qualify-ig/input/fsh/IhrisDeployment.fsh` line 25:
  `* extension[healthFacility].valueReference only Reference(IhrisFacility)`
- `ihris-backend/ihris-backend-site/qualify-ig/input/fsh/IhrisPractitioner.fsh` line 138:
  `* valueReference only Reference(IhrisJurisdiction)`

`IhrisFacility` is defined in `ihris-backend/ihris-backend-site/ig/input/fsh/IhrisLocation.fsh` (line 92), which is in the
manage IG and not in `qualify-ig` or `ig/`. **`IhrisJurisdiction` is not defined anywhere in the repository**: that file
has `IhrisCountry`, `IhrisRegion` and `IhrisDistrict` (and the `IhrisJurisdictionType` terminology), but no
`IhrisJurisdiction`.

**What happens:** `sushi build` in `qualify-ig` fails with 2 errors:

```
error No definition for the type "IhrisFacility" could be found.   (IhrisDeployment.fsh:25)
error No definition for the type "IhrisJurisdiction" could be found. (IhrisPractitioner.fsh:138)
```

Both constraints are dropped from the output.

**Fix:**
- `IhrisFacility`: move `IhrisLocation.fsh` into `ig/input/fsh`, so both backend IGs get it through `core`, or add it to
  `qualify-ig` as well.
- `IhrisJurisdiction`: either define an `IhrisJurisdiction` profile, or point line 138 at the existing ones, for example
  `Reference(IhrisCountry or IhrisRegion or IhrisDistrict)`, whichever the extension means.

(Correction, 2026-10-09: an earlier version of this draft said both profiles are in `IhrisLocation.fsh`. Only
`IhrisFacility` is; found by the filing session's re-check.)

---

## 3. The three IGs share one canonical and one package id, but define different content at the same URLs

**Where:** the `sushi-config.yaml` of `ig/`, `ihris-backend/ihris-backend-site/ig` and
`ihris-backend/ihris-backend-site/qualify-ig` all declare `canonical: http://ihris.org/fhir`, `id: ihris` and
`version: 0.1.0`.

**What happens:** the manage and qualify IGs both define these StructureDefinitions at the same canonical URL with
different content:
- `ihris-practitioner`, with 38 differential elements in manage and 37 in qualify
- `ihris-practitioner-dependents`
- `ihris-practitioner-marital-status`
- `ihris-practitioner-residence`
- `ihris-discipline`
- `ihris-basic-discipline`
- `ihris-user-location`

So a validator or server that loads both packages, or a mapping that targets `http://ihris.org/fhir/StructureDefinition/ihris-practitioner`, cannot tell which definition is meant. Both packages also claim the same package id and version, `ihris#0.1.0`.

**Fix:** give each IG its own package id, and either its own canonical (for example `http://ihris.org/fhir/manage` and
`http://ihris.org/fhir/qualify`) or distinct ids for the profiles that differ. Shared definitions belong in `ig/` (the
core package), with the backend IGs depending on it instead of copying it through the symlink.

---

## 4. Duplicate FSH names make references by name ambiguous

**Where:** all three IGs. SUSHI warns:

> Detected FSH entity definitions with duplicate names … IhrisRole, IhrisTask, IhrisJurisdictionType (manage),
> LocationStatus, LocationMode, ContactPointSystem, ContactPointUse, AddressUse, AddressType, LocationType, DaysOfWeek,
> IdentifierUse, IdentifierType, OrganizationType, ContactEntityType, ServiceCategory, ServiceType,
> ServiceProvisionConditions, NameUse, AdministrativeGender, Currencies, IhrisCadre, IhrisClassification, IhrisJob,
> IhrisSalaryGrade.

For example, `IhrisRole` is a Profile (`ig/input/fsh/IhrisRole.fsh:1`) and an Instance (`IhrisRole.fsh:645`), and `IhrisJob` is
both a ValueSet and a CodeSystem (`Terminologies.fsh:5959` and `:5973`).

**What happens:** `Reference(IhrisRole)` or `from IhrisJob` resolves by SUSHI's precedence rules, not by intent. Those
rules are stable today, but the result is fragile.

**Fix:** name the entities uniquely (for example `IhrisJobVS` and `IhrisJobCS`) and keep the published names with
`* ^name = "IhrisJob"` caret rules, as SUSHI suggests.

---

## 5. `Iso3166-1-2` is not a computable name

**Where:** `ig/input/fsh/Terminologies.fsh` line 6772, `ValueSet: Iso3166-1-2`.

**What happens:** SUSHI warns that the name is not suitable for code generation. A FHIR `name` must start with an
upper-case letter followed by letters, digits and `_`, so the hyphens break it.

**Fix:** `ValueSet: Iso3166Part1Alpha2` (any valid name), keeping `Id: iso3166-1-2` so the canonical URL does not change.
