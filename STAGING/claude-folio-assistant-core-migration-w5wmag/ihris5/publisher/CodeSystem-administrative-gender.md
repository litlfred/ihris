# AdministrativeGender - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **AdministrativeGender**

## CodeSystem: AdministrativeGender 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/administrative-gender | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:AdministrativeGender |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.1.2 | | |

 
The gender of a person used for administrative purposes. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [AdministrativeGender](ValueSet-administrative-gender.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "administrative-gender",
  "meta" : {
    "lastUpdated" : "2022-06-14T13:46:01.394+00:00"
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
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 5
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-normative-version",
    "valueCode" : "4.0.0"
  }],
  "url" : "http://hl7.org/fhir/administrative-gender",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.1.2"
  }],
  "version" : "0.1.0",
  "name" : "AdministrativeGender",
  "title" : "AdministrativeGender",
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
  "description" : "The gender of a person used for administrative purposes.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/administrative-gender",
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "male",
    "display" : "Male",
    "definition" : "Male."
  },
  {
    "code" : "female",
    "display" : "Female",
    "definition" : "Female."
  },
  {
    "code" : "other",
    "display" : "Other",
    "definition" : "Other."
  },
  {
    "code" : "unknown",
    "display" : "Unknown",
    "definition" : "Unknown."
  }]
}

```
