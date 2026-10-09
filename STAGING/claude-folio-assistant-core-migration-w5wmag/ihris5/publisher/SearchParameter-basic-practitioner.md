# basic-practitioner - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **basic-practitioner**

## SearchParameter: basic-practitioner 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/basic-practitioner | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on an practitioner extension on Basic resources |

 
Search by practitioner for a Basic resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "basic-practitioner",
  "url" : "http://ihris.org/fhir/SearchParameter/basic-practitioner",
  "version" : "0.1.0",
  "name" : "Search Parameter on an practitioner extension on Basic resources",
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
  "description" : "Search by practitioner for a Basic resource.",
  "code" : "practitioner",
  "base" : ["Basic"],
  "type" : "reference",
  "expression" : "Basic.extension('http://ihris.org/fhir/StructureDefinition/ihris-practitioner-reference')",
  "xpathUsage" : "normal",
  "target" : ["Practitioner"]
}

```
