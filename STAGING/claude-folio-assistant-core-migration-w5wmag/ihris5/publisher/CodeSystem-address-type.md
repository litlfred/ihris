# AddressType - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **AddressType**

## CodeSystem: AddressType 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/address-type | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:AddressType |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.70 | | |

 
The type of an address (physical / postal). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [AddressType](ValueSet-address-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "address-type",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:38.526+03:00",
    "source" : "#wbAXcC4IHcxqM3qA"
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
  "url" : "http://hl7.org/fhir/address-type",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.70"
  }],
  "version" : "0.1.0",
  "name" : "AddressType",
  "title" : "AddressType",
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
  "description" : "The type of an address (physical / postal).",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/address-type",
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "postal",
    "display" : "Postal",
    "definition" : "Mailing addresses - PO Boxes and care-of addresses."
  },
  {
    "code" : "physical",
    "display" : "Physical",
    "definition" : "A physical address that can be visited."
  },
  {
    "code" : "both",
    "display" : "Postal & Physical",
    "definition" : "An address that is both physical and postal."
  }]
}

```
