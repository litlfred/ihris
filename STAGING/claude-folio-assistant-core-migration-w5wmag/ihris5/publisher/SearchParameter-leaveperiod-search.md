# leaveperiod-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **leaveperiod-search**

## SearchParameter: leaveperiod-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/leaveperiod-search | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter for a practitioner's Leave Period |

 
Search for a practitioner's Leave Period 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "leaveperiod-search",
  "url" : "http://ihris.org/fhir/SearchParameter/leaveperiod-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitioner's Leave Period",
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
  "description" : "Search for a practitioner's Leave Period",
  "code" : "leaveperiod",
  "base" : ["Basic"],
  "type" : "date",
  "expression" : "Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-ethiopia-leave').extension.where(url='period')",
  "xpathUsage" : "normal"
}

```
