# DaysOfWeek - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **DaysOfWeek**

## CodeSystem: DaysOfWeek 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/days-of-week | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:DaysOfWeek |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.513 | | |

 
The days of the week. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [DaysOfWeek](ValueSet-days-of-week.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "days-of-week",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:04.757+03:00",
    "source" : "#05cbULabyly6Sdiw"
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "pa"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "normative"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-normative-version",
    "valueCode" : "4.0.0"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 5
  }],
  "url" : "http://hl7.org/fhir/days-of-week",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.513"
  }],
  "version" : "0.1.0",
  "name" : "DaysOfWeek",
  "title" : "DaysOfWeek",
  "status" : "active",
  "experimental" : false,
  "date" : "2019-11-01T09:29:23+11:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "The days of the week.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/days-of-week",
  "content" : "complete",
  "count" : 7,
  "concept" : [{
    "code" : "mon",
    "display" : "Monday",
    "definition" : "Monday."
  },
  {
    "code" : "tue",
    "display" : "Tuesday",
    "definition" : "Tuesday."
  },
  {
    "code" : "wed",
    "display" : "Wednesday",
    "definition" : "Wednesday."
  },
  {
    "code" : "thu",
    "display" : "Thursday",
    "definition" : "Thursday."
  },
  {
    "code" : "fri",
    "display" : "Friday",
    "definition" : "Friday."
  },
  {
    "code" : "sat",
    "display" : "Saturday",
    "definition" : "Saturday."
  },
  {
    "code" : "sun",
    "display" : "Sunday",
    "definition" : "Sunday."
  }]
}

```
