# leavetype-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **leavetype-search**

## SearchParameter: leavetype-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/leavetype-search | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter for a practitioner's Leave Type |

 
Search for a practitioner's Leave Type. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "leavetype-search",
  "url" : "http://ihris.org/fhir/SearchParameter/leavetype-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitioner's Leave Type",
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
  "description" : "Search for a practitioner's Leave Type.",
  "code" : "leavetype",
  "base" : ["Basic"],
  "type" : "token",
  "expression" : "Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-ethiopia-leavea').extension.where(url='leave-type')",
  "xpathUsage" : "normal"
}

```
