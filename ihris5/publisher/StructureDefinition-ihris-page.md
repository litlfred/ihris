# iHRIS Page - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Page**

## Resource Profile: iHRIS Page 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-page | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisPage |

 
iHRIS Profile of the Basic resource to manage pages. 

**Usages:**

* Examples for this Profile: [Basic/ihris-page-auditevent](Basic-ihris-page-auditevent.md), [Basic/ihris-page-role](Basic-ihris-page-role.md), [Basic/ihris-page-task](Basic-ihris-page-task.md), [Basic/ihris-page-test-codesystem](Basic-ihris-page-test-codesystem.md) and [Basic/ihris-page-test-practitioner](Basic-ihris-page-test-practitioner.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-page.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-page.csv), [Excel](StructureDefinition-ihris-page.xlsx), [Schematron](StructureDefinition-ihris-page.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-page",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page",
  "version" : "0.1.0",
  "name" : "IhrisPage",
  "title" : "iHRIS Page",
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
  "description" : "iHRIS Profile of the Basic resource to manage pages.",
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
      "id" : "Basic.extension:display",
      "path" : "Basic.extension",
      "sliceName" : "display",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page-display"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:section",
      "path" : "Basic.extension",
      "sliceName" : "section",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page-section"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:task",
      "path" : "Basic.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page-task"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.code",
      "path" : "Basic.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
          "code" : "page"
        }]
      }
    }]
  }
}

```
