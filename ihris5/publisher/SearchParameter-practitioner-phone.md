# practitioner-phone - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitioner-phone**

## SearchParameter: practitioner-phone 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitioner-phone | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:Search Parameter on a name extension on Basic resources |

 
Search by phone for a Practitioner resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitioner-phone",
  "url" : "http://ihris.org/fhir/SearchParameter/practitioner-phone",
  "version" : "0.1.0",
  "name" : "Search Parameter on a name extension on Basic resources",
  "status" : "active",
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search by phone for a Practitioner resource.",
  "code" : "phonenumber",
  "base" : ["Practitioner"],
  "type" : "string",
  "expression" : "Practitioner.telecom.where(system='phone').value",
  "xpathUsage" : "normal",
  "target" : ["Practitioner"]
}

```
