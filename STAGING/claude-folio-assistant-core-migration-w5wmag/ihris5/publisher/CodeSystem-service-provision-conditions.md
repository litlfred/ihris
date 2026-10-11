# ServiceProvisionConditions - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ServiceProvisionConditions**

## CodeSystem: ServiceProvisionConditions 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://terminology.hl7.org/CodeSystem/service-provision-conditions | *Version*:0.1.0 | |
| * Standards status: *[Draft](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:ServiceProvisionConditions |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.1143 | | |

 
The code(s) that detail the conditions under which the healthcare service is available/offered. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ServiceProvisionConditions](ValueSet-service-provision-conditions.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "service-provision-conditions",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:13.131+03:00",
    "source" : "#GRPiOoNOzlP2WMgQ"
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
  "url" : "http://terminology.hl7.org/CodeSystem/service-provision-conditions",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.1143"
  }],
  "version" : "0.1.0",
  "name" : "ServiceProvisionConditions",
  "title" : "ServiceProvisionConditions",
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
  "description" : "The code(s) that detail the conditions under which the healthcare service is available/offered.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/service-provision-conditions",
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "free",
    "display" : "Free",
    "definition" : "This service is available for no patient cost."
  },
  {
    "code" : "disc",
    "display" : "Discounts Available",
    "definition" : "There are discounts available on this service for qualifying patients."
  },
  {
    "code" : "cost",
    "display" : "Fees apply",
    "definition" : "Fees apply for this service."
  }]
}

```
