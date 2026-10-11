# LocationMode - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **LocationMode**

## CodeSystem: LocationMode 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/location-mode | *Version*:0.1.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 3 | *Computable Name*:LocationMode |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.331 | | |

 
Indicates whether a resource instance represents a specific location or a class of locations. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [LocationMode](ValueSet-location-mode.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "location-mode",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:58.239+03:00",
    "source" : "#ihvEM8PHESUikG5b"
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
  "url" : "http://hl7.org/fhir/location-mode",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.331"
  }],
  "version" : "0.1.0",
  "name" : "LocationMode",
  "title" : "LocationMode",
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
  "description" : "Indicates whether a resource instance represents a specific location or a class of locations.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/location-mode",
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "instance",
    "display" : "Instance",
    "definition" : "The Location resource represents a specific instance of a location (e.g. Operating Theatre 1A)."
  },
  {
    "code" : "kind",
    "display" : "Kind",
    "definition" : "The Location represents a class of locations (e.g. Any Operating Theatre) although this class of locations could be constrained within a specific boundary (such as organization, or parent location, address etc.)."
  }]
}

```
