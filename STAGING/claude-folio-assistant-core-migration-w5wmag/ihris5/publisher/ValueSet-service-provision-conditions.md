# ServiceProvisionConditions - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ServiceProvisionConditions**

## ValueSet: ServiceProvisionConditions 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/service-provision-conditions | *Version*:0.1.0 | |
| * Standards status: *[Draft](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:ServiceProvisionConditions |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.3.514 | | |

 
The code(s) that detail the conditions under which the healthcare service is available/offered. 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

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
  "id" : "service-provision-conditions",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:39.998+03:00",
    "source" : "#0m2hmKlpeBEUxoSg",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablevalueset"]
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
  "url" : "http://ihris.org/fhir/ValueSet/service-provision-conditions",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.3.514"
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
  "immutable" : true,
  "compose" : {
    "include" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/service-provision-conditions",
      "version" : "4.0.1"
    }]
  }
}

```
