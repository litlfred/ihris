# iHRIS Task To Read Questionnaire resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Read Questionnaire resource**

## Example Basic: iHRIS Task To Read Questionnaire resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-questionnaire-resource

> **Task Attributes**
* permission: read
* resource: Questionnaire

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-read-questionnaire-resource",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "read-questionnaire-resource"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "read"
    },
    {
      "url" : "resource",
      "valueCode" : "Questionnaire"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "task"
    }]
  }
}

```
