# basic-name - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **basic-name**

## SearchParameter: basic-name 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/basic-name | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on a name extension on Basic resources |

 
Search by name for a Basic resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "basic-name",
  "url" : "http://ihris.org/fhir/SearchParameter/basic-name",
  "version" : "0.1.0",
  "name" : "Search Parameter on a name extension on Basic resources",
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
  "description" : "Search by name for a Basic resource.",
  "code" : "name",
  "base" : ["Basic"],
  "type" : "string",
  "expression" : "Basic.extension('http://ihris.org/fhir/StructureDefinition/ihris-basic-name')",
  "xpathUsage" : "normal"
}

```
