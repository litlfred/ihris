# iHRIS Task With All Permissions To Everything - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task With All Permissions To Everything**

## Example Basic: iHRIS Task With All Permissions To Everything

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: all-permissions-to-everything

> **Task Attributes**
* permission: *
* resource: *

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-all-permissions-to-everything",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "all-permissions-to-everything"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "*"
    },
    {
      "url" : "resource",
      "valueCode" : "*"
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
