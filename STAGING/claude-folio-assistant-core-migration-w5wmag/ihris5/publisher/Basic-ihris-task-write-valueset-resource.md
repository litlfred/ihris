# iHRIS Task To Write Valueset Resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Write Valueset Resource**

## Example Basic: iHRIS Task To Write Valueset Resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-value-set

> **Task Attributes**
* permission: write
* resource: ValueSet

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-read-value-set.md)

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-write-valueset-resource",
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
      "valueCode" : "write"
    },
    {
      "url" : "resource",
      "valueCode" : "ValueSet"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-value-set"
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
