# iHRIS Task To Navigate to Profile - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Navigate to Profile**

## Example Basic: iHRIS Task To Navigate to Profile

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: navigation-profile

> **Task Attributes**
* permission: special
* resource: navigation
* instance: profile

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-navigation-profile",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "navigation-profile"
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
      "valueId" : "profile"
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
