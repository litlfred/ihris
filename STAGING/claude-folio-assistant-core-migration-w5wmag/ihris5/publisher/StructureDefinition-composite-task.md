# Composite Task - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Composite Task**

## Extension: Composite Task 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/composite-task | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:CompositeTask |

Tasks Inheritance

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Task](StructureDefinition-ihris-task.md)
* Examples for this Extension: [Basic/ihris-task-read-ihris-page-practitioner-role](Basic-ihris-task-read-ihris-page-practitioner-role.md), [Basic/ihris-task-read-ihris-page-practitioner](Basic-ihris-task-read-ihris-page-practitioner.md), [Basic/ihris-task-read-questionnaire-leave](Basic-ihris-task-read-questionnaire-leave.md), [Basic/ihris-task-write-auditevent-resource](Basic-ihris-task-write-auditevent-resource.md)... Show 14 more, [Basic/ihris-task-write-basic-resource](Basic-ihris-task-write-basic-resource.md), [Basic/ihris-task-write-code-system](Basic-ihris-task-write-code-system.md), [Basic/ihris-task-write-document-reference](Basic-ihris-task-write-document-reference.md), [Basic/ihris-task-write-location-resource](Basic-ihris-task-write-location-resource.md), [Basic/ihris-task-write-organization-resource](Basic-ihris-task-write-organization-resource.md), [Basic/ihris-task-write-person-resource](Basic-ihris-task-write-person-resource.md), [Basic/ihris-task-write-practitioner-resource](Basic-ihris-task-write-practitioner-resource.md), [Basic/ihris-task-write-practitioner-role-resource](Basic-ihris-task-write-practitioner-role-resource.md), [Basic/ihris-task-write-questionnaire-leave](Basic-ihris-task-write-questionnaire-leave.md), [Basic/ihris-task-write-questionnaire-resource](Basic-ihris-task-write-questionnaire-resource.md), [Basic/ihris-task-write-questionnaire-response-resource](Basic-ihris-task-write-questionnaire-response-resource.md), [Basic/ihris-task-write-structure-definition](Basic-ihris-task-write-structure-definition.md), [Basic/ihris-task-write-value-set](Basic-ihris-task-write-value-set.md) and [Basic/ihris-task-write-valueset-resource](Basic-ihris-task-write-valueset-resource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-composite-task.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-composite-task.csv), [Excel](StructureDefinition-composite-task.xlsx), [Schematron](StructureDefinition-composite-task.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "composite-task",
  "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
  "version" : "0.1.0",
  "name" : "CompositeTask",
  "title" : "Composite Task",
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
  "description" : "Tasks Inheritance",
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
    "expression" : "IhrisTask"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "Composite Task",
      "definition" : "Tasks Inheritance"
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/composite-task"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "label" : "Task",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.value[x].reference",
      "path" : "Extension.value[x].reference",
      "label" : "Task"
    }]
  }
}

```
