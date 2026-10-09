# gofr-search-isflowstart - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **gofr-search-isflowstart**

## SearchParameter: gofr-search-isflowstart 

| | |
| :--- | :--- |
| *Official URL*:http://gofr.org/fhir/SearchParameter/gofr-search-isflowstart | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:search parameter for flow starts |

 
search parameter for flow starts 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "gofr-search-isflowstart",
  "url" : "http://gofr.org/fhir/SearchParameter/gofr-search-isflowstart",
  "version" : "0.1.0",
  "name" : "search parameter for flow starts",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-10-09T11:54:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "search parameter for flow starts",
  "code" : "isflowstart",
  "base" : ["CommunicationRequest"],
  "type" : "token",
  "expression" : "CommunicationRequest.extension('http://mhero.org/fhir/StructureDefinition/mhero-comm-req-flow-starts').exists()"
}

```
