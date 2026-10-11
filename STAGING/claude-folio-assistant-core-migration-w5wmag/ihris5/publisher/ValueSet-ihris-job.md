# iHRIS Job - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Job**

## ValueSet: iHRIS Job 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/ihris-job | *Version*:0.1.0 |
| Active as of 2022-01-18 | *Computable Name*:IhrisJob |

 
Sample iHRIS ValueSet for: IhrisJob 

 **References** 

* [iHRIS Test Practitioner Role](StructureDefinition-ihris-test-practitioner-role.md)
* [iHRIS Test Questionnaire](Questionnaire-ihris-test.md)

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
  "id" : "ihris-job",
  "url" : "http://ihris.org/fhir/ValueSet/ihris-job",
  "version" : "0.1.0",
  "name" : "IhrisJob",
  "title" : "iHRIS Job",
  "status" : "active",
  "experimental" : false,
  "date" : "2022-01-18T20:48:33.646Z",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Sample iHRIS ValueSet for: IhrisJob",
  "compose" : {
    "include" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-job"
    }]
  }
}

```
