# active-user - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **active-user**

## SearchParameter: active-user 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/active-user | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on active person resources for security |

 
Search by active status for a Person resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "active-user",
  "url" : "http://ihris.org/fhir/SearchParameter/active-user",
  "version" : "0.1.0",
  "name" : "Search Parameter on active person resources for security",
  "status" : "active",
  "date" : "2026-10-09T11:54:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by active status for a Person resource.",
  "code" : "active",
  "base" : ["Person"],
  "type" : "token",
  "expression" : "Person.active",
  "xpathUsage" : "normal"
}

```
