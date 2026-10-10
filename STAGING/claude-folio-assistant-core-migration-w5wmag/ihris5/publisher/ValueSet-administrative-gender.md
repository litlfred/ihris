# AdministrativeGender - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **AdministrativeGender**

## ValueSet: AdministrativeGender 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/ValueSet/administrative-gender | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:AdministrativeGender |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.3.1 | | |

 
The gender of a person used for administrative purposes. 

 **References** 

* [Person Recorded Sex Or Gender](http://hl7.org/fhir/extensions/5.3.0/StructureDefinition-individual-recordedSexOrGender.html)
* [iHRIS Practitioner Dependent Detail](StructureDefinition-ihris-test-dependent.md)
* [iHRIS Test Questionnaire](Questionnaire-ihris-test.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "administrative-gender",
  "meta" : {
    "lastUpdated" : "2022-06-14T13:46:01.394+00:00",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablevalueset"]
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
  "url" : "http://hl7.org/fhir/ValueSet/administrative-gender",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.3.1"
  }],
  "version" : "0.1.0",
  "name" : "AdministrativeGender",
  "title" : "AdministrativeGender",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "The gender of a person used for administrative purposes.",
  "immutable" : true,
  "compose" : {
    "include" : [{
      "system" : "http://hl7.org/fhir/administrative-gender",
      "version" : "4.0.1"
    }]
  }
}

```
