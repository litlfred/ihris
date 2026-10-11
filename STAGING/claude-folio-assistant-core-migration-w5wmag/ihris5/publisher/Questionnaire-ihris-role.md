# iHRIS AddRole Workflow - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS AddRole Workflow**

## Questionnaire: iHRIS AddRole Workflow 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/Questionnaire/ihris-role | *Version*:0.1.0 |
| Active as of 2022-02-20 | *Computable Name*:ihris-role |

 
iHRIS workflow to record a Role 

 
Workflow page for recording a user role information. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "ihris-role",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-questionnaire"]
  },
  "url" : "http://ihris.org/fhir/Questionnaire/ihris-role",
  "version" : "0.1.0",
  "name" : "ihris-role",
  "title" : "iHRIS AddRole Workflow",
  "status" : "active",
  "date" : "2022-02-20",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS workflow to record a Role",
  "purpose" : "Workflow page for recording a user role information.",
  "item" : [{
    "linkId" : "Basic",
    "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role",
    "text" : "Add Role",
    "type" : "group",
    "item" : [{
      "linkId" : "Basic.id",
      "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role#Basic.id",
      "text" : "Role Details",
      "type" : "group",
      "item" : [{
        "linkId" : "Basic.extension[0]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role#Basic.extension:name.value[x]:valueString",
        "text" : "Role Name",
        "type" : "string",
        "required" : false,
        "repeats" : false
      },
      {
        "linkId" : "Basic.extension[1]#preload",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role#Basic.extension:task.value[x]:valueReference",
        "text" : "Tasks",
        "type" : "reference",
        "required" : false,
        "repeats" : true
      },
      {
        "linkId" : "Basic.extension[2]#preload",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role#Basic.extension:role.value[x]:valueReference",
        "text" : "Roles",
        "type" : "reference",
        "required" : false,
        "repeats" : true
      },
      {
        "linkId" : "Basic.extension[3]",
        "definition" : "http://ihris.org/fhir/StructureDefinition/ihris-role#Basic.extension:primary.value[x]:valueBoolean",
        "text" : "Is Role Primary",
        "type" : "boolean",
        "required" : true,
        "repeats" : false
      }]
    }]
  }]
}

```
