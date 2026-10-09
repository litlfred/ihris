# iHRIS Task To Write Organization resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Write Organization resource**

## Example Basic: iHRIS Task To Write Organization resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: write-organization-resource

> **Task Attributes**
* permission: write
* resource: Organization

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-read-organization-resource.md)

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-write-organization-resource",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "write-organization-resource"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "write"
    },
    {
      "url" : "resource",
      "valueCode" : "Organization"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-organization-resource"
    }
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "task"
    }]
  }
}

```
