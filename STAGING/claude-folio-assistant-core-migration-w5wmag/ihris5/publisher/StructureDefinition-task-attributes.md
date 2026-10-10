# Task Attributes - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Task Attributes**

## Extension: Task Attributes 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/task-attributes | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:TaskAttributes |

Task attributes.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Task](StructureDefinition-ihris-task.md)
* Examples for this Extension: [Basic/ihris-task-all-permissions-to-everything](Basic-ihris-task-all-permissions-to-everything.md), [Basic/ihris-task-navigation-evaluation](Basic-ihris-task-navigation-evaluation.md), [Basic/ihris-task-navigation-leave](Basic-ihris-task-navigation-leave.md), [Basic/ihris-task-navigation-password](Basic-ihris-task-navigation-password.md)... Show 33 more, [Basic/ihris-task-navigation-profile](Basic-ihris-task-navigation-profile.md), [Basic/ihris-task-read-auditevent-resource](Basic-ihris-task-read-auditevent-resource.md), [Basic/ihris-task-read-basic-resource](Basic-ihris-task-read-basic-resource.md), [Basic/ihris-task-read-code-system](Basic-ihris-task-read-code-system.md), [Basic/ihris-task-read-document-reference](Basic-ihris-task-read-document-reference.md), [Basic/ihris-task-read-ihris-page-practitioner-role](Basic-ihris-task-read-ihris-page-practitioner-role.md), [Basic/ihris-task-read-ihris-page-practitioner](Basic-ihris-task-read-ihris-page-practitioner.md), [Basic/ihris-task-read-location-resource](Basic-ihris-task-read-location-resource.md), [Basic/ihris-task-read-organization-resource](Basic-ihris-task-read-organization-resource.md), [Basic/ihris-task-read-person-resource](Basic-ihris-task-read-person-resource.md), [Basic/ihris-task-read-practitioner-resource](Basic-ihris-task-read-practitioner-resource.md), [Basic/ihris-task-read-practitioner-role-resource](Basic-ihris-task-read-practitioner-role-resource.md), [Basic/ihris-task-read-questionnaire-leave](Basic-ihris-task-read-questionnaire-leave.md), [Basic/ihris-task-read-questionnaire-resource](Basic-ihris-task-read-questionnaire-resource.md), [Basic/ihris-task-read-questionnaire-response-resource](Basic-ihris-task-read-questionnaire-response-resource.md), [Basic/ihris-task-read-structure-definition](Basic-ihris-task-read-structure-definition.md), [Basic/ihris-task-read-value-set](Basic-ihris-task-read-value-set.md), [Basic/ihris-task-write-auditevent-resource](Basic-ihris-task-write-auditevent-resource.md), [Basic/ihris-task-write-basic-resource](Basic-ihris-task-write-basic-resource.md), [Basic/ihris-task-write-code-system](Basic-ihris-task-write-code-system.md), [Basic/ihris-task-write-document-reference](Basic-ihris-task-write-document-reference.md), [Basic/ihris-task-write-location-resource](Basic-ihris-task-write-location-resource.md), [Basic/ihris-task-write-organization-resource](Basic-ihris-task-write-organization-resource.md), [Basic/ihris-task-write-person-resource](Basic-ihris-task-write-person-resource.md), [Basic/ihris-task-write-practitioner-resource](Basic-ihris-task-write-practitioner-resource.md), [Basic/ihris-task-write-practitioner-role-resource](Basic-ihris-task-write-practitioner-role-resource.md), [Basic/ihris-task-write-questionnaire-change-password](Basic-ihris-task-write-questionnaire-change-password.md), [Basic/ihris-task-write-questionnaire-leave](Basic-ihris-task-write-questionnaire-leave.md), [Basic/ihris-task-write-questionnaire-resource](Basic-ihris-task-write-questionnaire-resource.md), [Basic/ihris-task-write-questionnaire-response-resource](Basic-ihris-task-write-questionnaire-response-resource.md), [Basic/ihris-task-write-structure-definition](Basic-ihris-task-write-structure-definition.md), [Basic/ihris-task-write-value-set](Basic-ihris-task-write-value-set.md) and [Basic/ihris-task-write-valueset-resource](Basic-ihris-task-write-valueset-resource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-task-attributes.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-task-attributes.csv), [Excel](StructureDefinition-task-attributes.xlsx), [Schematron](StructureDefinition-task-attributes.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "task-attributes",
  "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes",
  "version" : "0.1.0",
  "name" : "TaskAttributes",
  "title" : "Task Attributes",
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
  "description" : "Task attributes.",
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
      "short" : "Task Attributes",
      "definition" : "Task attributes.",
      "constraint" : [{
        "key" : "ihris-task-instance-constraint",
        "severity" : "error",
        "human" : "Only one of extension[instance].valueCode or extension[constraint].valueReference SHALL be present.",
        "expression" : "extension(url = instance).exists() xor extension(url = constraint).exists()",
        "xpath" : "exists(f:extension(url = instance)) != exists(f:extension(url = constraint))",
        "source" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
      }]
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 1
    },
    {
      "id" : "Extension.extension:permission",
      "path" : "Extension.extension",
      "sliceName" : "permission",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:permission.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:permission.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "permission"
    },
    {
      "id" : "Extension.extension:permission.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://ihris.org/fhir/ValueSet/ihris-task-permission"
      }
    },
    {
      "id" : "Extension.extension:resource",
      "path" : "Extension.extension",
      "sliceName" : "resource",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resource"
    },
    {
      "id" : "Extension.extension:resource.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://ihris.org/fhir/ValueSet/ihris-task-resource"
      }
    },
    {
      "id" : "Extension.extension:instance",
      "path" : "Extension.extension",
      "sliceName" : "instance",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:instance.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:instance.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "instance"
    },
    {
      "id" : "Extension.extension:instance.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "id"
      }]
    },
    {
      "id" : "Extension.extension:field",
      "path" : "Extension.extension",
      "sliceName" : "field",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:field.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.extension:constraint",
      "path" : "Extension.extension",
      "sliceName" : "constraint",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:constraint.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:constraint.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "constraint"
    },
    {
      "id" : "Extension.extension:constraint.value[x]",
      "path" : "Extension.extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
