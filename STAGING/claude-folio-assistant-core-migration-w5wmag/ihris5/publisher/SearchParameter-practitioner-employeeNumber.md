# practitioner-employeeNumber - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-employeeNumber**

## SearchParameter: practitioner-employeeNumber 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-employeeNumber | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on employee Number for practitioner |

 
Search by employee number for a practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-employeeNumber",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-employeeNumber",
  "version" : "0.1.0",
  "name" : "Search Parameter on employee Number for practitioner",
  "status" : "active",
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by employee number for a practitioner resource.",
  "code" : "employeeNumber",
  "base" : ["Practitioner"],
  "type" : "string",
  "expression" : "Practitioner.identifier.where(type.coding.code='EN').value",
  "xpathUsage" : "normal"
}

```
