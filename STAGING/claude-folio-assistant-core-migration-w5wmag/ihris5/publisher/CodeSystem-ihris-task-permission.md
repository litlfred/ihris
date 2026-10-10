# Code system for task permissions. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Code system for task permissions.**

## CodeSystem: Code system for task permissions. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-task-permission | *Version*:0.1.0 |
| Active as of 2021-03-26 | *Computable Name*:IhrisTaskPermissionCodeSystem |

 This Code system is referenced in the content logical definition of the following value sets: 

* [Code system for task permissions.](ValueSet-ihris-task-permission.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-task-permission",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-task-permission",
  "version" : "0.1.0",
  "name" : "IhrisTaskPermissionCodeSystem",
  "title" : "Code system for task permissions.",
  "status" : "active",
  "date" : "2021-03-26T09:25:04.362Z",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "*",
    "display" : "All",
    "definition" : "Can do any task."
  },
  {
    "code" : "read",
    "display" : "Read",
    "definition" : "Can read the given resource."
  },
  {
    "code" : "write",
    "display" : "Write",
    "definition" : "Can write the given resource."
  },
  {
    "code" : "delete",
    "display" : "Delete",
    "definition" : "Can delete the given resource."
  },
  {
    "code" : "filter",
    "display" : "Filter",
    "definition" : "Search filter constraints."
  },
  {
    "code" : "special",
    "display" : "Special",
    "definition" : "Special non-resource permissions."
  }]
}

```
