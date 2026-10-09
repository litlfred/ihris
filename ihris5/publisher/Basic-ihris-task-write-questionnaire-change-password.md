# iHRIS Task To Write Questionnaire ihris-password - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Write Questionnaire ihris-password**

## Example Basic: iHRIS Task To Write Questionnaire ihris-password

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: write-questionnaire

> **Task Attributes**
* permission: write
* resource: Questionnaire
* instance: ihris-change-password

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-write-questionnaire-change-password",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "write-questionnaire"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "write"
    },
    {
      "url" : "resource",
      "valueCode" : "Questionnaire"
    },
    {
      "url" : "instance",
      "valueId" : "ihris-change-password"
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
