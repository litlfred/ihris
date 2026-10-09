# Value Set for iHRIS Basic Resources. - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Value Set for iHRIS Basic Resources.**

## ValueSet: Value Set for iHRIS Basic Resources. 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/ihris-resource-valueset | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisResourceValueSet |

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
  "id" : "ihris-resource-valueset",
  "url" : "http://ihris.org/fhir/ValueSet/ihris-resource-valueset",
  "version" : "0.1.0",
  "name" : "IhrisResourceValueSet",
  "title" : "Value Set for iHRIS Basic Resources.",
  "status" : "active",
  "date" : "2026-10-09T12:24:25+00:00",
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
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem"
    }]
  }
}

```
