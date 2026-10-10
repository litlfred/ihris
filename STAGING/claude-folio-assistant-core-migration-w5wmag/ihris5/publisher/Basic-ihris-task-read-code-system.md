# iHRIS Task To Read CodeSystem resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Read CodeSystem resource**

## Example Basic: iHRIS Task To Read CodeSystem resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-code-system

> **Task Attributes**
* permission: read
* resource: CodeSystem

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-read-code-system",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "read-code-system"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "read"
    },
    {
      "url" : "resource",
      "valueCode" : "CodeSystem"
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
