# Code system for task permissions. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Code system for task permissions.**

## ValueSet: Code system for task permissions. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/ihris-task-resource | *Version*:0.1.0 |
| Active as of 2024-03-26 | *Computable Name*:IhrisTaskResourceValueSet |

 **References** 

* [Task Attributes](StructureDefinition-task-attributes.md)
* [iHRIS Add Task Workflow](Questionnaire-ihris-task.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "ihris-task-resource",
  "url" : "http://ihris.org/fhir/ValueSet/ihris-task-resource",
  "version" : "0.1.0",
  "name" : "IhrisTaskResourceValueSet",
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
  "compose" : {
    "include" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-task-resource"
    }]
  }
}

```
