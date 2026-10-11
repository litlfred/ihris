# iHRIS Add Task Workflow - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Add Task Workflow**

## Questionnaire: iHRIS Add Task Workflow 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/Questionnaire/ihris-task | *Version*:0.1.0 |
| Active as of 2022-02-20 | *Computable Name*:ihris-task |

 
iHRIS workflow to record a Role 

 
Workflow page for user role tasks information. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "ihris-task",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-questionnaire"]
  },
  "url" : "http://ihris.org/fhir/Questionnaire/ihris-task",
  "version" : "0.1.0",
  "name" : "ihris-task",
  "title" : "iHRIS Add Task Workflow",
  "status" : "active",
  "date" : "2022-02-20",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS workflow to record a Role",
  "purpose" : "Workflow page for user role tasks information.",
  "item" : [{
    "linkId" : "Basic",
    "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task",
    "text" : "Add Task",
    "type" : "group",
    "item" : [{
      "linkId" : "Basic.extension[0]",
      "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes",
      "text" : "Task Attributes",
      "type" : "group",
      "item" : [{
        "linkId" : "Basic.extension[0].extension[0]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes.extension:permission.value[x]:valueCode",
        "text" : "Permission",
        "type" : "choice",
        "required" : true,
        "repeats" : false,
        "answerValueSet" : "http://ihris.org/fhir/ValueSet/ihris-task-permission"
      },
      {
        "linkId" : "Basic.extension[0].extension[1]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes.extension:resource.value[x]:valueCode",
        "text" : "Resource",
        "type" : "choice",
        "required" : true,
        "repeats" : false,
        "answerValueSet" : "http://ihris.org/fhir/ValueSet/ihris-task-resource"
      },
      {
        "linkId" : "Basic.extension[0].extension[2]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes.extension:instance.value[x]:valueId",
        "text" : "Instance",
        "type" : "string",
        "required" : false,
        "repeats" : false
      },
      {
        "linkId" : "Basic.extension[0].extension[3]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes.extension:constraint.value[x]:valueString",
        "text" : "Constraint",
        "type" : "string",
        "required" : false,
        "repeats" : false
      },
      {
        "linkId" : "Basic.extension[0].extension[4]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:attributes.extension:field.value[x]:valueString",
        "text" : "Field",
        "type" : "string",
        "required" : false,
        "repeats" : false
      }]
    },
    {
      "linkId" : "CompositeTasks",
      "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:compositeTask",
      "text" : "Composite/Linked Tasks",
      "type" : "group",
      "item" : [{
        "linkId" : "linkedtasks",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-task#Basic.extension:compositeTask.value[x]:valueReference",
        "text" : "Composite/Linked Tasks",
        "type" : "reference",
        "required" : false,
        "repeats" : true
      }]
    }]
  }]
}

```
