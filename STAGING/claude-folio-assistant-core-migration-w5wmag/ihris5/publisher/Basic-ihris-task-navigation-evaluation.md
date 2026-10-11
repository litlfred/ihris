# iHRIS Task To Navigate to evaluation - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Navigate to evaluation**

## Example Basic: iHRIS Task To Navigate to evaluation

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: navigation-evaluation

> **Task Attributes**
* permission: special
* resource: navigation
* instance: evaluation

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-navigation-evaluation",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "navigation-evaluation"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "special"
    },
    {
      "url" : "resource",
      "valueCode" : "navigation"
    },
    {
      "url" : "instance",
      "valueId" : "evaluation"
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
