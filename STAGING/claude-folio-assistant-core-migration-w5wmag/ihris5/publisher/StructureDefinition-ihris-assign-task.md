# iHRIS Assign Task - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Assign Task**

## Extension: iHRIS Assign Task 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-assign-task | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisAssignTask |

iHRIS Assign Task to a user or other task.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Role](StructureDefinition-ihris-role.md)
* Examples for this Extension: [Basic/ihris-role-admin](Basic-ihris-role-admin.md), [Basic/ihris-role-open](Basic-ihris-role-open.md) and [Basic/ihris-role-self](Basic-ihris-role-self.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-assign-task.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-assign-task.csv), [Excel](StructureDefinition-ihris-assign-task.xlsx), [Schematron](StructureDefinition-ihris-assign-task.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-assign-task",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task",
  "version" : "0.1.0",
  "name" : "IhrisAssignTask",
  "title" : "iHRIS Assign Task",
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
  "description" : "iHRIS Assign Task to a user or other task.",
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
    "expression" : "IhrisRole"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Assign Task",
      "definition" : "iHRIS Assign Task to a user or other task."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-task"
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
