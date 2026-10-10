# gofr-search-isbroadcast - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **gofr-search-isbroadcast**

## SearchParameter: gofr-search-isbroadcast 

| | |
| :--- | :--- |
| *Official URL*:http://gofr.org/fhir/SearchParameter/gofr-search-isbroadcast | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:search parameter for broadcasted messages |

 
search parameter for broadcasted messages 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "gofr-search-isbroadcast",
  "url" : "http://gofr.org/fhir/SearchParameter/gofr-search-isbroadcast",
  "version" : "0.1.0",
  "name" : "search parameter for broadcasted messages",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "search parameter for broadcasted messages",
  "code" : "isbroadcast",
  "base" : ["CommunicationRequest"],
  "type" : "token",
  "expression" : "CommunicationRequest.extension('http://mhero.org/fhir/StructureDefinition/mhero-comm-req-broadcast-starts').exists()"
}

```
