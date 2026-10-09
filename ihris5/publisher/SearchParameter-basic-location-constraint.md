# basic-location-constraint - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **basic-location-constraint**

## SearchParameter: basic-location-constraint 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/basic-location-constraint | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related location constraint resources for role |

 
Search by related location for a Basic resource Role. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "basic-location-constraint",
  "url" : "http://ihris.org/fhir/SearchParameter/basic-location-constraint",
  "version" : "0.1.0",
  "name" : "Search Parameter on related location constraint resources for role",
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
  "description" : "Search by related location for a Basic resource Role.",
  "code" : "locationconstraint",
  "base" : ["Basic"],
  "type" : "string",
  "expression" : "Basic.extension('http://ihris.org/fhir/StructureDefinition/ihris-task').extension('constraint')",
  "xpathUsage" : "normal"
}

```
