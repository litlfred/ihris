# iHRIS Task - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task**

## Resource Profile: iHRIS Task 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-task | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisTask |

 
iHRIS Profile of the Basic resource to manage tasks. 

**Usages:**

* Refer to this Profile: [Composite Task](StructureDefinition-composite-task.md) and [iHRIS Assign Task](StructureDefinition-ihris-assign-task.md)
* Examples for this Profile: [Basic/ihris-task-all-permissions-to-everything](Basic-ihris-task-all-permissions-to-everything.md), [Basic/ihris-task-navigation-evaluation](Basic-ihris-task-navigation-evaluation.md), [Basic/ihris-task-navigation-leave](Basic-ihris-task-navigation-leave.md), [Basic/ihris-task-navigation-password](Basic-ihris-task-navigation-password.md)... Show 33 more, [Basic/ihris-task-navigation-profile](Basic-ihris-task-navigation-profile.md), [Basic/ihris-task-read-auditevent-resource](Basic-ihris-task-read-auditevent-resource.md), [Basic/ihris-task-read-basic-resource](Basic-ihris-task-read-basic-resource.md), [Basic/ihris-task-read-code-system](Basic-ihris-task-read-code-system.md), [Basic/ihris-task-read-document-reference](Basic-ihris-task-read-document-reference.md), [Basic/ihris-task-read-ihris-page-practitioner-role](Basic-ihris-task-read-ihris-page-practitioner-role.md), [Basic/ihris-task-read-ihris-page-practitioner](Basic-ihris-task-read-ihris-page-practitioner.md), [Basic/ihris-task-read-location-resource](Basic-ihris-task-read-location-resource.md), [Basic/ihris-task-read-organization-resource](Basic-ihris-task-read-organization-resource.md), [Basic/ihris-task-read-person-resource](Basic-ihris-task-read-person-resource.md), [Basic/ihris-task-read-practitioner-resource](Basic-ihris-task-read-practitioner-resource.md), [Basic/ihris-task-read-practitioner-role-resource](Basic-ihris-task-read-practitioner-role-resource.md), [Basic/ihris-task-read-questionnaire-leave](Basic-ihris-task-read-questionnaire-leave.md), [Basic/ihris-task-read-questionnaire-resource](Basic-ihris-task-read-questionnaire-resource.md), [Basic/ihris-task-read-questionnaire-response-resource](Basic-ihris-task-read-questionnaire-response-resource.md), [Basic/ihris-task-read-structure-definition](Basic-ihris-task-read-structure-definition.md), [Basic/ihris-task-read-value-set](Basic-ihris-task-read-value-set.md), [Basic/ihris-task-write-auditevent-resource](Basic-ihris-task-write-auditevent-resource.md), [Basic/ihris-task-write-basic-resource](Basic-ihris-task-write-basic-resource.md), [Basic/ihris-task-write-code-system](Basic-ihris-task-write-code-system.md), [Basic/ihris-task-write-document-reference](Basic-ihris-task-write-document-reference.md), [Basic/ihris-task-write-location-resource](Basic-ihris-task-write-location-resource.md), [Basic/ihris-task-write-organization-resource](Basic-ihris-task-write-organization-resource.md), [Basic/ihris-task-write-person-resource](Basic-ihris-task-write-person-resource.md), [Basic/ihris-task-write-practitioner-resource](Basic-ihris-task-write-practitioner-resource.md), [Basic/ihris-task-write-practitioner-role-resource](Basic-ihris-task-write-practitioner-role-resource.md), [Basic/ihris-task-write-questionnaire-change-password](Basic-ihris-task-write-questionnaire-change-password.md), [Basic/ihris-task-write-questionnaire-leave](Basic-ihris-task-write-questionnaire-leave.md), [Basic/ihris-task-write-questionnaire-resource](Basic-ihris-task-write-questionnaire-resource.md), [Basic/ihris-task-write-questionnaire-response-resource](Basic-ihris-task-write-questionnaire-response-resource.md), [Basic/ihris-task-write-structure-definition](Basic-ihris-task-write-structure-definition.md), [Basic/ihris-task-write-value-set](Basic-ihris-task-write-value-set.md) and [Basic/ihris-task-write-valueset-resource](Basic-ihris-task-write-valueset-resource.md)
* Search Parameters using this Profile: [Search Parameter on related location constraint resources for role](SearchParameter-basic-location-constraint.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-task.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-task.csv), [Excel](StructureDefinition-ihris-task.xlsx), [Schematron](StructureDefinition-ihris-task.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-task",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-task",
  "version" : "0.1.0",
  "name" : "IhrisTask",
  "title" : "iHRIS Task",
  "status" : "active",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Profile of the Basic resource to manage tasks.",
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
      "id" : "Basic.extension:name",
      "path" : "Basic.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-basic-name"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:attributes",
      "path" : "Basic.extension",
      "sliceName" : "attributes",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/task-attributes"]
      }]
    },
    {
      "id" : "Basic.extension:attributes.extension:permission",
      "path" : "Basic.extension.extension",
      "sliceName" : "permission",
      "label" : "Permission"
    },
    {
      "id" : "Basic.extension:attributes.extension:permission.value[x]",
      "path" : "Basic.extension.extension.value[x]",
      "label" : "Permission",
      "min" : 1,
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:attributes.extension:resource",
      "path" : "Basic.extension.extension",
      "sliceName" : "resource",
      "label" : "Resource"
    },
    {
      "id" : "Basic.extension:attributes.extension:resource.value[x]",
      "path" : "Basic.extension.extension.value[x]",
      "label" : "Resource",
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:attributes.extension:instance",
      "path" : "Basic.extension.extension",
      "sliceName" : "instance",
      "label" : "Instance"
    },
    {
      "id" : "Basic.extension:attributes.extension:instance.value[x]",
      "path" : "Basic.extension.extension.value[x]",
      "label" : "Instance",
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:attributes.extension:field",
      "path" : "Basic.extension.extension",
      "sliceName" : "field",
      "label" : "Field"
    },
    {
      "id" : "Basic.extension:attributes.extension:field.value[x]",
      "path" : "Basic.extension.extension.value[x]",
      "label" : "Field",
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:attributes.extension:constraint",
      "path" : "Basic.extension.extension",
      "sliceName" : "constraint",
      "label" : "Constraint"
    },
    {
      "id" : "Basic.extension:attributes.extension:constraint.value[x]",
      "path" : "Basic.extension.extension.value[x]",
      "label" : "Constraint",
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:compositeTask",
      "path" : "Basic.extension",
      "sliceName" : "compositeTask",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/composite-task"]
      }]
    },
    {
      "id" : "Basic.extension:compositeTask.value[x]",
      "path" : "Basic.extension.value[x]",
      "label" : "Composite Task"
    },
    {
      "id" : "Basic.code",
      "path" : "Basic.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
          "code" : "task"
        }]
      }
    }]
  }
}

```
