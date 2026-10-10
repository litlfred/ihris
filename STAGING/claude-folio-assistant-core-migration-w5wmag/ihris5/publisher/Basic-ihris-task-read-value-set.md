# iHRIS Task To Read Valueset Resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Read Valueset Resource**

## Example Basic: iHRIS Task To Read Valueset Resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-value-set

> **Task Attributes**
* permission: read
* resource: ValueSet

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-read-value-set",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "read-value-set"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "read"
    },
    {
      "url" : "resource",
      "valueCode" : "ValueSet"
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
