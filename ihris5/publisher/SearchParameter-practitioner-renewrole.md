# practitioner-renewrole - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-renewrole**

## SearchParameter: practitioner-renewrole 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-renewrole | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on employee id for practitioner |

 
Search by employee ID for a practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-renewrole",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-renewrole",
  "version" : "0.1.0",
  "name" : "Search Parameter on  employee id for practitioner",
  "status" : "active",
  "date" : "2026-10-09T12:31:23+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by employee ID for a practitioner resource.",
  "code" : "renewrole",
  "base" : ["Practitioner"],
  "type" : "string",
  "expression" : "Practitioner.identifier.where(type.coding.code='PractitionerRole.period.start').value",
  "xpathUsage" : "normal"
}

```
