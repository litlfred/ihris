# practitionerrole-related-location - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **practitionerrole-related-location**

## SearchParameter: practitionerrole-related-location 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/SearchParameter/practitionerrole-related-location | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:Search Parameter on related location resources for security |

 
Search by related location for a PractitionerRole resource. 



## Resource Content

```json
{
  "resourceType" : "SearchParameter",
  "id" : "practitionerrole-related-location",
  "url" : "http://ihris.org/fhir/SearchParameter/practitionerrole-related-location",
  "version" : "0.1.0",
  "name" : "Search Parameter on related location resources for security",
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
  "description" : "Search by related location for a PractitionerRole resource.",
  "code" : "related-location",
  "base" : ["PractitionerRole"],
  "type" : "string",
  "expression" : "PractitionerRole.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location') | PractitionerRole.extension('http://ihris.org/fhir/StructureDefinition/ihris-related-group').extension('location').empty()",
  "xpathUsage" : "normal"
}

```
