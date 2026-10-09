# Contact entity type - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Contact entity type**

## CodeSystem: Contact entity type 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://terminology.hl7.org/CodeSystem/contactentity-type | *Version*:0.1.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 3 | *Computable Name*:ContactEntityType |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.1129 | | |

 
This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Contact entity type](ValueSet-contactentity-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "contactentity-type",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:12.032+03:00",
    "source" : "#1TzaqZMbfamefRi3",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablecodesystem"]
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
  "url" : "http://terminology.hl7.org/CodeSystem/contactentity-type",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.1129"
  }],
  "version" : "0.1.0",
  "name" : "ContactEntityType",
  "title" : "Contact entity type",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-10-09T12:24:25+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/contactentity-type",
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "BILL",
    "display" : "Billing",
    "definition" : "Contact details for information regarding to billing/general finance enquiries."
  },
  {
    "code" : "ADMIN",
    "display" : "Administrative",
    "definition" : "Contact details for administrative enquiries."
  },
  {
    "code" : "HR",
    "display" : "Human Resource",
    "definition" : "Contact details for issues related to Human Resources, such as staff matters, OH&S etc."
  },
  {
    "code" : "PAYOR",
    "display" : "Payor",
    "definition" : "Contact details for dealing with issues related to insurance claims/adjudication/payment."
  },
  {
    "code" : "PATINF",
    "display" : "Patient",
    "definition" : "Generic information contact for patients."
  },
  {
    "code" : "PRESS",
    "display" : "Press",
    "definition" : "Dedicated contact point for matters relating to press enquiries."
  }]
}

```
