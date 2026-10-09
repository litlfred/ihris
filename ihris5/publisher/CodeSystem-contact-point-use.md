# ContactPointUse - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ContactPointUse**

## CodeSystem: ContactPointUse 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/contact-point-use | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:ContactPointUse |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.74 | | |

 
Use of contact point. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ContactPointUse](ValueSet-contact-point-use.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "contact-point-use",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:11.176+03:00",
    "source" : "#jXMHyNVcUayicVHs"
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "fhir"
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
  "url" : "http://hl7.org/fhir/contact-point-use",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.74"
  }],
  "version" : "0.1.0",
  "name" : "ContactPointUse",
  "title" : "ContactPointUse",
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
  "description" : "Use of contact point.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/contact-point-use",
  "content" : "complete",
  "count" : 5,
  "concept" : [{
    "code" : "home",
    "display" : "Home",
    "definition" : "A communication contact point at a home; attempted contacts for business purposes might intrude privacy and chances are one will contact family or other household members instead of the person one wishes to call. Typically used with urgent cases, or if no other contacts are available."
  },
  {
    "code" : "work",
    "display" : "Work",
    "definition" : "An office contact point. First choice for business related contacts during business hours."
  },
  {
    "code" : "temp",
    "display" : "Temp",
    "definition" : "A temporary contact point. The period can provide more detailed information."
  },
  {
    "code" : "old",
    "display" : "Old",
    "definition" : "This contact point is no longer in use (or was never correct, but retained for records)."
  },
  {
    "code" : "mobile",
    "display" : "Mobile",
    "definition" : "A telecommunication device that moves and stays with its owner. May have characteristics of all other use codes, suitable for urgent matters, not the first choice for routine business."
  }]
}

```
