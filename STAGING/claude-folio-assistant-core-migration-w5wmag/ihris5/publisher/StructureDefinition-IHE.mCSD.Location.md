# IHEmCSDLocation - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **IHEmCSDLocation**

## Resource Profile: IHEmCSDLocation 

| | |
| :--- | :--- |
| *Official URL*:http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location | *Version*:0.1.0 |
| Draft as of 2026-10-09 | *Computable Name*:IHEmCSDLocation |

**Usages:**

* Derived from this Profile: [IHEmCSDFacilityLocation](StructureDefinition-IHE.mCSD.FacilityLocation.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-IHE.mCSD.Location.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-IHE.mCSD.Location.csv), [Excel](StructureDefinition-IHE.mCSD.Location.xlsx), [Schematron](StructureDefinition-IHE.mCSD.Location.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "IHE.mCSD.Location",
  "url" : "http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
  "version" : "0.1.0",
  "name" : "IHEmCSDLocation",
  "status" : "draft",
  "date" : "2026-10-09T12:24:25+00:00",
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
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Location",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Location",
      "path" : "Location"
    },
    {
      "id" : "Location.meta.profile",
      "path" : "Location.meta.profile",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "mCSD"
        }],
        "rules" : "open"
      },
      "min" : 1
    },
    {
      "id" : "Location.meta.profile:mCSD",
      "path" : "Location.meta.profile",
      "sliceName" : "mCSD",
      "min" : 1,
      "max" : "1",
      "fixedCanonical" : "http://ihe.net/fhir/StructureDefinition/IHE_mCSD_Location"
    },
    {
      "id" : "Location.meta.profile:sliceProfile",
      "path" : "Location.meta.profile",
      "sliceName" : "sliceProfile"
    },
    {
      "id" : "Location.status",
      "path" : "Location.status",
      "min" : 1
    },
    {
      "id" : "Location.name",
      "path" : "Location.name",
      "min" : 1
    },
    {
      "id" : "Location.type",
      "path" : "Location.type",
      "min" : 1
    },
    {
      "id" : "Location.physicalType",
      "path" : "Location.physicalType",
      "min" : 1
    }]
  }
}

```
