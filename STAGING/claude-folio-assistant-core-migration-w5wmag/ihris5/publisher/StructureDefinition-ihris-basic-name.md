# iHRIS Basic Name - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Basic Name**

## Extension: iHRIS Basic Name 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-basic-name | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisBasicName |

iHRIS name field for basic resources.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Dashboard](StructureDefinition-ihris-dashboard.md), [iHRIS Data Visualizer](StructureDefinition-ihris-data-visualization.md), [iHRIS Role](StructureDefinition-ihris-role.md) and [iHRIS Task](StructureDefinition-ihris-task.md)
* Examples for this Extension: [Basic/ihris-role-admin](Basic-ihris-role-admin.md), [Basic/ihris-role-open](Basic-ihris-role-open.md), [Basic/ihris-role-self](Basic-ihris-role-self.md), [Basic/ihris-task-all-permissions-to-everything](Basic-ihris-task-all-permissions-to-everything.md)... Show 36 more, [Basic/ihris-task-navigation-evaluation](Basic-ihris-task-navigation-evaluation.md), [Basic/ihris-task-navigation-leave](Basic-ihris-task-navigation-leave.md), [Basic/ihris-task-navigation-password](Basic-ihris-task-navigation-password.md), [Basic/ihris-task-navigation-profile](Basic-ihris-task-navigation-profile.md), [Basic/ihris-task-read-auditevent-resource](Basic-ihris-task-read-auditevent-resource.md), [Basic/ihris-task-read-basic-resource](Basic-ihris-task-read-basic-resource.md), [Basic/ihris-task-read-code-system](Basic-ihris-task-read-code-system.md), [Basic/ihris-task-read-document-reference](Basic-ihris-task-read-document-reference.md), [Basic/ihris-task-read-ihris-page-practitioner-role](Basic-ihris-task-read-ihris-page-practitioner-role.md), [Basic/ihris-task-read-ihris-page-practitioner](Basic-ihris-task-read-ihris-page-practitioner.md), [Basic/ihris-task-read-location-resource](Basic-ihris-task-read-location-resource.md), [Basic/ihris-task-read-organization-resource](Basic-ihris-task-read-organization-resource.md), [Basic/ihris-task-read-person-resource](Basic-ihris-task-read-person-resource.md), [Basic/ihris-task-read-practitioner-resource](Basic-ihris-task-read-practitioner-resource.md), [Basic/ihris-task-read-practitioner-role-resource](Basic-ihris-task-read-practitioner-role-resource.md), [Basic/ihris-task-read-questionnaire-leave](Basic-ihris-task-read-questionnaire-leave.md), [Basic/ihris-task-read-questionnaire-resource](Basic-ihris-task-read-questionnaire-resource.md), [Basic/ihris-task-read-questionnaire-response-resource](Basic-ihris-task-read-questionnaire-response-resource.md), [Basic/ihris-task-read-structure-definition](Basic-ihris-task-read-structure-definition.md), [Basic/ihris-task-read-value-set](Basic-ihris-task-read-value-set.md), [Basic/ihris-task-write-auditevent-resource](Basic-ihris-task-write-auditevent-resource.md), [Basic/ihris-task-write-basic-resource](Basic-ihris-task-write-basic-resource.md), [Basic/ihris-task-write-code-system](Basic-ihris-task-write-code-system.md), [Basic/ihris-task-write-document-reference](Basic-ihris-task-write-document-reference.md), [Basic/ihris-task-write-location-resource](Basic-ihris-task-write-location-resource.md), [Basic/ihris-task-write-organization-resource](Basic-ihris-task-write-organization-resource.md), [Basic/ihris-task-write-person-resource](Basic-ihris-task-write-person-resource.md), [Basic/ihris-task-write-practitioner-resource](Basic-ihris-task-write-practitioner-resource.md), [Basic/ihris-task-write-practitioner-role-resource](Basic-ihris-task-write-practitioner-role-resource.md), [Basic/ihris-task-write-questionnaire-change-password](Basic-ihris-task-write-questionnaire-change-password.md), [Basic/ihris-task-write-questionnaire-leave](Basic-ihris-task-write-questionnaire-leave.md), [Basic/ihris-task-write-questionnaire-resource](Basic-ihris-task-write-questionnaire-resource.md), [Basic/ihris-task-write-questionnaire-response-resource](Basic-ihris-task-write-questionnaire-response-resource.md), [Basic/ihris-task-write-structure-definition](Basic-ihris-task-write-structure-definition.md), [Basic/ihris-task-write-value-set](Basic-ihris-task-write-value-set.md) and [Basic/ihris-task-write-valueset-resource](Basic-ihris-task-write-valueset-resource.md)
* Search Parameters using this Extension: [Search Parameter on a name extension on Basic resources](SearchParameter-basic-name.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-basic-name.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-basic-name.csv), [Excel](StructureDefinition-ihris-basic-name.xlsx), [Schematron](StructureDefinition-ihris-basic-name.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-basic-name",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
  "version" : "0.1.0",
  "name" : "IhrisBasicName",
  "title" : "iHRIS Basic Name",
  "status" : "active",
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS name field for basic resources.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "Basic"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Basic Name",
      "definition" : "iHRIS name field for basic resources."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "label" : "Name",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    }]
  }
}

```
