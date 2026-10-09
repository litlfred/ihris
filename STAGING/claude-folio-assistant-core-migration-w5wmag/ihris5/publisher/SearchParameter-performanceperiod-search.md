# performanceperiod-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **performanceperiod-search**

## SearchParameter: performanceperiod-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/performanceperiod-search | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter for a practitioner's Performance Period |

 
Search for a practitioner's Performance Period 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "performanceperiod-search",
  "url" : "http://ihris.org/fhir/SearchParameter/performanceperiod-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitioner's Performance Period",
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
  "description" : "Search for a practitioner's Performance Period",
  "code" : "performanceperiod",
  "base" : ["Basic"],
  "type" : "date",
  "expression" : "Basic.extension.where(url='http://ihris.org/fhir/StructureDefinition/ihris-performance').extension.where(url='period')",
  "xpathUsage" : "normal"
}

```
