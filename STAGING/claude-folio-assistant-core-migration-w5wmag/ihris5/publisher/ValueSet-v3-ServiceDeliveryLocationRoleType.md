# V3 Value SetServiceDeliveryLocationRoleType - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **V3 Value SetServiceDeliveryLocationRoleType**

## ValueSet: V3 Value SetServiceDeliveryLocationRoleType 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType | *Version*:0.1.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 3 | *Computable Name*:V3_ServiceDeliveryLocationRoleType |
| *Other Identifiers:*OID:2.16.840.1.113883.1.11.17660 | | |

 
A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered. 

 **References** 

* [Location](http://hl7.org/fhir/R4/location.html)
* [ServiceRequest](http://hl7.org/fhir/R4/servicerequest.html)

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
  "id" : "v3-ServiceDeliveryLocationRoleType",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:16:12.009+03:00",
    "source" : "#MRfemLMQj06Qpx2q",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablevalueset"]
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 3
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "pa"
  }],
  "url" : "http://terminology.hl7.org/ValueSet/v3-ServiceDeliveryLocationRoleType",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.1.11.17660"
  }],
  "version" : "0.1.0",
  "name" : "V3_ServiceDeliveryLocationRoleType",
  "title" : "V3 Value SetServiceDeliveryLocationRoleType",
  "status" : "active",
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
  "description" : " A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered.",
  "immutable" : false,
  "compose" : {
    "include" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "version" : "4.0.0",
      "filter" : [{
        "property" : "concept",
        "op" : "is-a",
        "value" : "_ServiceDeliveryLocationRoleType"
      }]
    }],
    "exclude" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v3-RoleCode",
      "concept" : [{
        "code" : "_ServiceDeliveryLocationRoleType"
      }]
    }]
  }
}

```
