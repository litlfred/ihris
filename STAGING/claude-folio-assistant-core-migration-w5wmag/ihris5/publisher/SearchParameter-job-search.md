# job-search - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **job-search**

## SearchParameter: job-search 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/job-search | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:Search Parameter for a practitionerRole job |

 
Search for a practitionerRole job. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "job-search",
  "url" : "http://ihris.org/fhir/SearchParameter/job-search",
  "version" : "0.1.0",
  "name" : "Search Parameter for a practitionerRole job",
  "status" : "active",
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Search for a practitionerRole job.",
  "code" : "job",
  "base" : ["PractitionerRole"],
  "type" : "token",
  "expression" : "PractitionerRole.code",
  "xpathUsage" : "normal"
}

```
