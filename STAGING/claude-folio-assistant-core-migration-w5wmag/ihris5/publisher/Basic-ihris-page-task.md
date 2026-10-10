# iHRIS Tasks - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Tasks**

## Example Basic: iHRIS Tasks

Profile: [iHRIS Page](StructureDefinition-ihris-page.md)

> **iHRIS Page Display**
> **url**resource
**value**: [StructureDefinition iHRIS Task](StructureDefinition-ihris-task.md)
> **url**search
**value**: Id|Basic.id**field**: Basic.id**text**: Edit**url**: /questionnaire/ihris-task/task/FIELD**button**: true**icon**: mdi-pencil**class**: secondary
> **url**link
**field**: **text**: View Other Tasks**url**: /resource/search/task**button**: true**icon**: mdi-account-arrow-right
> **url**link
**url**: /questionnaire/ihris-task/task**icon**: mdi-account-plus**class**: accent
> **url**add

> **url**search
**value**: Name|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-basic-name').valueString
> **url**[FilterSearchParameter](filter)
**value**: Task|Basic.extension:id:contains

> **iHRIS Page Section**
* title: Task
* description: iHRIS User task details
* name: Basic
* field: Basic.extension:name.value[x]:valueString
* field: Basic.extension:attributes
* field: Basic.extension:compositeTask

**code**: iHRIS Page



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-page-task",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "resource",
      "valueReference" : {
        "reference" : "StructureDefinition/ihris-task"
      }
    },
    {
      "url" : "search",
      "valueString" : "Id|Basic.id"
    },
    {
      "extension" : [{
        "url" : "field",
        "valueString" : "Basic.id"
      },
      {
        "url" : "text",
        "valueString" : "Edit"
      },
      {
        "url" : "displayIn"
      },
      {
        "url" : "url",
        "valueUrl" : "/questionnaire/ihris-task/task/FIELD"
      },
      {
        "url" : "button",
        "valueBoolean" : true
      },
      {
        "url" : "icon",
        "valueString" : "mdi-pencil"
      },
      {
        "url" : "class",
        "valueString" : "secondary"
      }],
      "url" : "link"
    },
    {
      "extension" : [{
        "url" : "field",
        "valueString" : ""
      },
      {
        "url" : "text",
        "valueString" : "View Other Tasks"
      },
      {
        "url" : "displayIn"
      },
      {
        "url" : "url",
        "valueUrl" : "/resource/search/task"
      },
      {
        "url" : "button",
        "valueBoolean" : true
      },
      {
        "url" : "icon",
        "valueString" : "mdi-account-arrow-right"
      }],
      "url" : "link"
    },
    {
      "extension" : [{
        "url" : "url",
        "valueUrl" : "/questionnaire/ihris-task/task"
      },
      {
        "url" : "icon",
        "valueString" : "mdi-account-plus"
      },
      {
        "url" : "class",
        "valueString" : "accent"
      }],
      "url" : "add"
    },
    {
      "url" : "search",
      "valueString" : "Name|Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-basic-name').valueString"
    },
    {
      "url" : "filter",
      "valueString" : "Task|Basic.extension:id:contains"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Task"
    },
    {
      "url" : "description",
      "valueString" : "iHRIS User task details"
    },
    {
      "url" : "name",
      "valueString" : "Basic"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:name.value[x]:valueString"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:attributes"
    },
    {
      "url" : "field",
      "valueString" : "Basic.extension:compositeTask"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "page"
    }]
  }
}

```
