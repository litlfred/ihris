# Code System for iHRIS Basic Resources. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Code System for iHRIS Basic Resources.**

## CodeSystem: Code System for iHRIS Basic Resources. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisResourceCodeSystem |

 This Code system is referenced in the content logical definition of the following value sets: 

* [Value Set for iHRIS Basic Resources.](ValueSet-ihris-resource-valueset.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-resource-codesystem",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
  "version" : "0.1.0",
  "name" : "IhrisResourceCodeSystem",
  "title" : "Code System for iHRIS Basic Resources.",
  "status" : "active",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "content" : "complete",
  "count" : 9,
  "concept" : [{
    "code" : "role",
    "display" : "iHRIS Role",
    "definition" : "User roles that are available to be assigned to users."
  },
  {
    "code" : "task",
    "display" : "iHRIS Task",
    "definition" : "Role tasks that are available to be assigned to roles"
  },
  {
    "code" : "page",
    "display" : "iHRIS Page",
    "definition" : "Page definitions for viewing and editing resources."
  },
  {
    "code" : "practitioner-link",
    "display" : "iHRIS Practitioner Link",
    "definition" : "Basic resource for customization that links to a Practitioner."
  },
  {
    "code" : "training-link",
    "display" : "iHRIS Training Link",
    "definition" : "Basic resource for customization that links to a Qualify training."
  },
  {
    "code" : "visualization",
    "display" : "iHRIS Data Visualization",
    "definition" : "iHRIS Data Visualization"
  },
  {
    "code" : "dashboard",
    "display" : "iHRIS Dashboard",
    "definition" : "iHRIS Dashboard"
  },
  {
    "code" : "resourcedata",
    "display" : "Resource Data",
    "definition" : "Resource Data"
  },
  {
    "code" : "standard-list",
    "display" : "Standard List",
    "definition" : "Standard List"
  }]
}

```
