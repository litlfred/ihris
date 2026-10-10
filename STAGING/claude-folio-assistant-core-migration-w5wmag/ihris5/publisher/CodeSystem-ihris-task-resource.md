# Code system for task permissions. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Code system for task permissions.**

## CodeSystem: Code system for task permissions. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/CodeSystem/ihris-task-resource | *Version*:0.1.0 |
| Active as of 2024-03-26 | *Computable Name*:IhrisTaskResourceCodeSystem |

 This Code system is referenced in the content logical definition of the following value sets: 

* [Code system for task permissions.](ValueSet-ihris-task-resource.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "ihris-task-resource",
  "url" : "http://ihris.org/fhir/CodeSystem/ihris-task-resource",
  "version" : "0.1.0",
  "name" : "IhrisTaskResourceCodeSystem",
  "title" : "Code system for task permissions.",
  "status" : "active",
  "date" : "2024-03-26T09:25:04.362Z",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "content" : "complete",
  "count" : 18,
  "concept" : [{
    "code" : "*",
    "display" : "All"
  },
  {
    "code" : "Practitioner",
    "display" : "Practitioner"
  },
  {
    "code" : "StructureDefinition",
    "display" : "StructureDefinition"
  },
  {
    "code" : "ValueSet",
    "display" : "ValueSet"
  },
  {
    "code" : "CodeSystem",
    "display" : "CodeSystem"
  },
  {
    "code" : "Basic",
    "display" : "Basic"
  },
  {
    "code" : "DocumentReference",
    "display" : "DocumentReference"
  },
  {
    "code" : "Organization",
    "display" : "Organization"
  },
  {
    "code" : "Questionnaire",
    "display" : "Questionnaire"
  },
  {
    "code" : "QuestionnaireResponse",
    "display" : "QuestionnaireResponse"
  },
  {
    "code" : "PractitionerRole",
    "display" : "PractitionerRole"
  },
  {
    "code" : "Location",
    "display" : "Location"
  },
  {
    "code" : "Person",
    "display" : "Person"
  },
  {
    "code" : "Parameters",
    "display" : "Parameters"
  },
  {
    "code" : "AuditEvent",
    "display" : "AuditEvent"
  },
  {
    "code" : "navigation",
    "display" : "Page Navigation"
  },
  {
    "code" : "section",
    "display" : "Page Section"
  },
  {
    "code" : "special",
    "display" : "Special"
  }]
}

```
