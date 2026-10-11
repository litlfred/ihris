# iHRIS Task To Navigate to Leave - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Navigate to Leave**

## Example Basic: iHRIS Task To Navigate to Leave

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: navigation-leave

> **Task Attributes**
* permission: special
* resource: navigation
* instance: leaveRequest

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-navigation-leave",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "navigation-leave"
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
      "valueId" : "leaveRequest"
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
