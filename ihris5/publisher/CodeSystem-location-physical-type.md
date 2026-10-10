# Location type - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Location type**

## CodeSystem: Location type 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://terminology.hl7.org/CodeSystem/location-physical-type | *Version*:0.1.0 | |
| * Standards status: *[Draft](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:LocationType |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.1108 | | |

 
This example value set defines a set of codes that can be used to indicate the physical form of the Location. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Location type](ValueSet-location-physical-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "location-physical-type",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:20.522+03:00",
    "source" : "#gVSzyaw7vrYD2zWC",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablecodesystem"]
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "pa"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "draft"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 1
  }],
  "url" : "http://terminology.hl7.org/CodeSystem/location-physical-type",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.1108"
  }],
  "version" : "0.1.0",
  "name" : "LocationType",
  "title" : "Location type",
  "status" : "draft",
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
  "description" : "This example value set defines a set of codes that can be used to indicate the physical form of the Location.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/location-physical-type",
  "content" : "complete",
  "count" : 14,
  "concept" : [{
    "code" : "si",
    "display" : "Site",
    "definition" : "A collection of buildings or other locations such as a site or a campus."
  },
  {
    "code" : "bu",
    "display" : "Building",
    "definition" : "Any Building or structure. This may contain rooms, corridors, wings, etc. It might not have walls, or a roof, but is considered a defined/allocated space."
  },
  {
    "code" : "wi",
    "display" : "Wing",
    "definition" : "A Wing within a Building, this often contains levels, rooms and corridors."
  },
  {
    "code" : "wa",
    "display" : "Ward",
    "definition" : "A Ward is a section of a medical facility that may contain rooms and other types of location."
  },
  {
    "code" : "lvl",
    "display" : "Level",
    "definition" : "A Level in a multi-level Building/Structure."
  },
  {
    "code" : "co",
    "display" : "Corridor",
    "definition" : "Any corridor within a Building, that may connect rooms."
  },
  {
    "code" : "ro",
    "display" : "Room",
    "definition" : "A space that is allocated as a room, it may have walls/roof etc., but does not require these."
  },
  {
    "code" : "bd",
    "display" : "Bed",
    "definition" : "A space that is allocated for sleeping/laying on. This is not the physical bed/trolley that may be moved about, but the space it may occupy."
  },
  {
    "code" : "ve",
    "display" : "Vehicle",
    "definition" : "A means of transportation."
  },
  {
    "code" : "ho",
    "display" : "House",
    "definition" : "A residential dwelling. Usually used to reference a location that a person/patient may reside."
  },
  {
    "code" : "ca",
    "display" : "Cabinet",
    "definition" : "A container that can store goods, equipment, medications or other items."
  },
  {
    "code" : "rd",
    "display" : "Road",
    "definition" : "A defined path to travel between 2 points that has a known name."
  },
  {
    "code" : "area",
    "display" : "Area",
    "definition" : "A defined physical boundary of something, such as a flood risk zone, region, postcode"
  },
  {
    "code" : "jdn",
    "display" : "Jurisdiction",
    "definition" : "A wide scope that covers a conceptual domain, such as a Nation (Country wide community or Federal Government - e.g. Ministry of Health),  Province or State (community or Government), Business (throughout the enterprise), Nation with a business scope of an agency (e.g. CDC, FDA etc.) or a Business segment (UK Pharmacy), not just an physical boundary"
  }]
}

```
