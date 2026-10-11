# LocationStatus - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **LocationStatus**

## CodeSystem: LocationStatus 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/location-status | *Version*:0.1.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 3 | *Computable Name*:LocationStatus |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.333 | | |

 
Indicates whether the location is still in use. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [LocationStatus](ValueSet-location-status.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "location-status",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:24.960+03:00",
    "source" : "#ofZ1t0pi6T7bA09X"
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "pa"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 3
  }],
  "url" : "http://hl7.org/fhir/location-status",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.333"
  }],
  "version" : "0.1.0",
  "name" : "LocationStatus",
  "title" : "LocationStatus",
  "status" : "draft",
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
  "description" : "Indicates whether the location is still in use.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/location-status",
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "active",
    "display" : "Active",
    "definition" : "The location is operational."
  },
  {
    "code" : "suspended",
    "display" : "Suspended",
    "definition" : "The location is temporarily closed."
  },
  {
    "code" : "inactive",
    "display" : "Inactive",
    "definition" : "The location is no longer used."
  }]
}

```
