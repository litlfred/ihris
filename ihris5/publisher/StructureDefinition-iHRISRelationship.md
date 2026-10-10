# iHRIS Resources Relationship Profile - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Resources Relationship Profile**

## Resource Profile: iHRIS Resources Relationship Profile 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/iHRISRelationship | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisRelationship |

 
iHRIS Resources Relationship Profile 

**Usages:**

* Examples for this Profile: [Basic/ihris-es-report-mhero-send-message](Basic-ihris-es-report-mhero-send-message.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-iHRISRelationship.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-iHRISRelationship.csv), [Excel](StructureDefinition-iHRISRelationship.xlsx), [Schematron](StructureDefinition-iHRISRelationship.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "iHRISRelationship",
  "url" : "http://ihris.org/fhir/StructureDefinition/iHRISRelationship",
  "version" : "0.1.0",
  "name" : "IhrisRelationship",
  "title" : "iHRIS Resources Relationship Profile",
  "status" : "active",
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Resources Relationship Profile",
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
  "type" : "Basic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Basic",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Basic",
      "path" : "Basic"
    },
    {
      "id" : "Basic.extension",
      "path" : "Basic.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 1
    },
    {
      "id" : "Basic.extension:reportdetails",
      "path" : "Basic.extension",
      "sliceName" : "reportdetails",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISReportDetails"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:reportlink",
      "path" : "Basic.extension",
      "sliceName" : "reportlink",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISReportLink"]
      }],
      "mustSupport" : true
    }]
  }
}

```
