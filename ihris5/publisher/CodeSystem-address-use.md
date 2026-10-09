# AddressUse - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **AddressUse**

## CodeSystem: AddressUse 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/address-use | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:AddressUse |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.68 | | |

 
The use of an address. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [AddressUse](ValueSet-address-use.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "address-use",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:19.131+03:00",
    "source" : "#p6zFoi9Jny2q0yPE"
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
  "url" : "http://hl7.org/fhir/address-use",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.68"
  }],
  "version" : "0.1.0",
  "name" : "AddressUse",
  "title" : "AddressUse",
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
  "description" : "The use of an address.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/address-use",
  "content" : "complete",
  "count" : 5,
  "concept" : [{
    "code" : "home",
    "display" : "Home",
    "definition" : "A communication address at a home."
  },
  {
    "code" : "work",
    "display" : "Work",
    "definition" : "An office address. First choice for business related contacts during business hours."
  },
  {
    "code" : "temp",
    "display" : "Temporary",
    "definition" : "A temporary address. The period can provide more detailed information."
  },
  {
    "code" : "old",
    "display" : "Old / Incorrect",
    "definition" : "This address is no longer in use (or was never correct but retained for records)."
  },
  {
    "code" : "billing",
    "display" : "Billing",
    "definition" : "An address to be used to send bills, invoices, receipts etc."
  }]
}

```
