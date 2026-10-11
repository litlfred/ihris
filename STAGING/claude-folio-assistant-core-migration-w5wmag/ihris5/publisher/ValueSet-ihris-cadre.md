# iHRIS Cadre - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Cadre**

## ValueSet: iHRIS Cadre 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/ihris-cadre | *Version*:0.1.0 |
| Active as of 2020-09-25 | *Computable Name*:IhrisCadre |

 
Sample iHRIS ValueSet for: IhrisCadre 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

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
  "id" : "ihris-cadre",
  "url" : "http://ihris.org/fhir/ValueSet/ihris-cadre",
  "version" : "0.1.0",
  "name" : "IhrisCadre",
  "title" : "iHRIS Cadre",
  "status" : "active",
  "experimental" : false,
  "date" : "2020-09-25T21:03:12.952Z",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Sample iHRIS ValueSet for: IhrisCadre",
  "compose" : {
    "include" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-cadre"
    }]
  }
}

```
