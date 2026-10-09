# iHRIS Report - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Report**

## Resource Profile: iHRIS Report 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-report | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisReport |

 
iHRIS Profile of the Basic resource to manage reports. 

**Usages:**

* This Profile is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-report.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-report.csv), [Excel](StructureDefinition-ihris-report.xlsx), [Schematron](StructureDefinition-ihris-report.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-report",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-report",
  "version" : "0.1.0",
  "name" : "IhrisReport",
  "title" : "iHRIS Report",
  "status" : "active",
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Profile of the Basic resource to manage reports.",
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
      "id" : "Basic.extension:reportDetails",
      "path" : "Basic.extension",
      "sliceName" : "reportDetails",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/iHRISReportDetails"]
      }],
      "mustSupport" : true
    }]
  }
}

```
