# practitioner-birthdate - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-birthdate**

## SearchParameter: practitioner-birthdate 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-birthdate | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on birthdate resources for practioner |

 
Search by birthdate for a Practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-birthdate",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-birthdate",
  "version" : "0.1.0",
  "name" : "Search Parameter on birthdate resources for practioner",
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
  "description" : "Search by birthdate for a Practitioner resource.",
  "code" : "birthDate",
  "base" : ["Practitioner"],
  "type" : "date",
  "expression" : "Practitioner.birthDate",
  "xpathUsage" : "normal"
}

```
