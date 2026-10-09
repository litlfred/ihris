# iHRIS Questionnaire - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Questionnaire**

## Resource Profile: iHRIS Questionnaire 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-questionnaire | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisQuestionnaire |

 
iHRIS Profile of the Questionnaire resource for data entry and validation. 

**Usages:**

* Examples for this Profile: [ihris-role](Questionnaire-ihris-role.md) and [ihris-task](Questionnaire-ihris-task.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-questionnaire.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-questionnaire.csv), [Excel](StructureDefinition-ihris-questionnaire.xlsx), [Schematron](StructureDefinition-ihris-questionnaire.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-questionnaire",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-questionnaire",
  "version" : "0.1.0",
  "name" : "IhrisQuestionnaire",
  "title" : "iHRIS Questionnaire",
  "status" : "active",
  "date" : "2026-10-09T11:54:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Profile of the Questionnaire resource for data entry and validation.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  },
  {
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Questionnaire",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Questionnaire",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Questionnaire",
      "path" : "Questionnaire"
    },
    {
      "id" : "Questionnaire.item.extension",
      "path" : "Questionnaire.item.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Questionnaire.item.extension:constraint",
      "path" : "Questionnaire.item.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/StructureDefinition/questionnaire-constraint"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Questionnaire.item.item",
      "path" : "Questionnaire.item.item",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Questionnaire.item.item.extension",
      "path" : "Questionnaire.item.item.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Questionnaire.item.item.extension:constraint",
      "path" : "Questionnaire.item.item.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/StructureDefinition/questionnaire-constraint"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Questionnaire.item.item.item",
      "path" : "Questionnaire.item.item.item",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Questionnaire.item.item.item.extension",
      "path" : "Questionnaire.item.item.item.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Questionnaire.item.item.item.extension:constraint",
      "path" : "Questionnaire.item.item.item.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/StructureDefinition/questionnaire-constraint"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Questionnaire.item.item.item.item",
      "path" : "Questionnaire.item.item.item.item",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Questionnaire.item.item.item.item.extension",
      "path" : "Questionnaire.item.item.item.item.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Questionnaire.item.item.item.item.extension:constraint",
      "path" : "Questionnaire.item.item.item.item.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/StructureDefinition/questionnaire-constraint"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Questionnaire.item.item.item.item.item",
      "path" : "Questionnaire.item.item.item.item.item",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Questionnaire.item.item.item.item.item.extension",
      "path" : "Questionnaire.item.item.item.item.item.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      }
    },
    {
      "id" : "Questionnaire.item.item.item.item.item.extension:constraint",
      "path" : "Questionnaire.item.item.item.item.item.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://hl7.org/fhir/StructureDefinition/questionnaire-constraint"]
      }],
      "mustSupport" : true
    }]
  }
}

```
