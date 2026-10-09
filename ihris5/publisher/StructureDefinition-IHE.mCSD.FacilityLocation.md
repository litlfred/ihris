# IHEmCSDFacilityLocation - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **IHEmCSDFacilityLocation**

## Resource Profile: IHEmCSDFacilityLocation 

| | |
| :--- | :--- |
| *Official URL*:http://ihe.net/fhir/StructureDefinition/IHE.mCSD.FacilityLocation | *Version*:0.1.0 |
| Draft as of 2026-10-09 | *Computable Name*:IHEmCSDFacilityLocation |

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-IHE.mCSD.FacilityLocation.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-IHE.mCSD.FacilityLocation.csv), [Excel](StructureDefinition-IHE.mCSD.FacilityLocation.xlsx), [Schematron](StructureDefinition-IHE.mCSD.FacilityLocation.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "IHE.mCSD.FacilityLocation",
  "url" : "http://ihe.net/fhir/StructureDefinition/IHE.mCSD.FacilityLocation",
  "version" : "0.1.0",
  "name" : "IHEmCSDFacilityLocation",
  "status" : "draft",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Location",
  "baseDefinition" : "http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Location",
      "path" : "Location"
    },
    {
      "id" : "Location.meta.profile",
      "path" : "Location.meta.profile",
      "min" : 2
    },
    {
      "id" : "Location.meta.profile:mCSDFacility",
      "path" : "Location.meta.profile",
      "sliceName" : "mCSDFacility",
      "min" : 1,
      "max" : "1",
      "fixedCanonical" : "http://ihe.net/fhir/StructureDefinition/IHE_mCSD_FacilityLocation"
    },
    {
      "id" : "Location.type",
      "path" : "Location.type",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "coding.system"
        }],
        "rules" : "open"
      },
      "min" : 2
    },
    {
      "id" : "Location.type:facilityType",
      "path" : "Location.type",
      "sliceName" : "facilityType",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Location.type:facilityType.coding",
      "path" : "Location.type.coding",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Location.type:facilityType.coding.system",
      "path" : "Location.type.coding.system",
      "min" : 1,
      "fixedUri" : "urn:ietf:rfc:3986"
    },
    {
      "id" : "Location.type:facilityType.coding.code",
      "path" : "Location.type.coding.code",
      "min" : 1,
      "fixedCode" : "urn:ihe:iti:mcsd:2019:facility"
    },
    {
      "id" : "Location.type:sliceType",
      "path" : "Location.type",
      "sliceName" : "sliceType",
      "min" : 1
    },
    {
      "id" : "Location.managingOrganization",
      "path" : "Location.managingOrganization",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://ihe.net/fhir/StructureDefinition/IHE_mCSD_FacilityOrganization"]
      }]
    },
    {
      "id" : "Location.managingOrganization.reference",
      "path" : "Location.managingOrganization.reference",
      "min" : 1
    }]
  }
}

```
