# IdentifierType - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **IdentifierType**

## ValueSet: IdentifierType 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ValueSet/identifier-type | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:IdentifierType |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.3.45 | | |

 
A coded type for an identifier that can be used to determine which identifier to use for a specific purpose. 

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
  "id" : "identifier-type",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:15:53.644+03:00",
    "source" : "#dUQ1w25GGaF7BmRG",
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablevalueset"]
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/valueset-warning",
    "valueMarkdown" : "Types are for general categories of identifiers. See [the identifier registry](identifier-registry.html) for a list of common identifier systems"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-wg",
    "valueCode" : "vocab"
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
  "url" : "http://ihris.org/fhir/ValueSet/identifier-type",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.3.45"
  }],
  "version" : "0.1.0",
  "name" : "IdentifierType",
  "title" : "IdentifierType",
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
  "description" : "A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.",
  "compose" : {
    "include" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v2-0203",
      "version" : "5.0.0",
      "concept" : [{
        "code" : "DL"
      },
      {
        "code" : "PPN"
      },
      {
        "code" : "BRN"
      },
      {
        "code" : "MR"
      },
      {
        "code" : "MCN"
      },
      {
        "code" : "EN"
      },
      {
        "code" : "TAX"
      },
      {
        "code" : "NIIP"
      },
      {
        "code" : "PRN"
      },
      {
        "code" : "MD"
      },
      {
        "code" : "DR"
      },
      {
        "code" : "ACSN"
      },
      {
        "code" : "UDI"
      },
      {
        "code" : "SNO"
      },
      {
        "code" : "SB"
      },
      {
        "code" : "PLAC"
      },
      {
        "code" : "FILL"
      },
      {
        "code" : "JHN"
      }]
    }]
  }
}

```
