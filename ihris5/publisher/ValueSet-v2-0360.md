# hl7VS-degreeLicenseCertificate - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **hl7VS-degreeLicenseCertificate**

## ValueSet: hl7VS-degreeLicenseCertificate 

| | |
| :--- | :--- |
| *Official URL*:http://terminology.hl7.org/ValueSet/v2-0360 | *Version*:0.1.0 |
| Active as of 2019-12-01 | *Computable Name*:Hl7VSDegreeLicenseCertificate |
| *Other Identifiers:*OID:2.16.840.1.113883.21.236 | |
| **Copyright/Legal**: Copyright HL7. Licensed under creative commons public domain | |

 
Concepts specifying an educational degree (e.g., MD). Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging. Used in Version 2 messaging; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7. 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

No Expansion for this valueset (Unsupported Code System Version)

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
  "id" : "v2-0360",
  "url" : "http://terminology.hl7.org/ValueSet/v2-0360",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.21.236"
  }],
  "version" : "0.1.0",
  "name" : "Hl7VSDegreeLicenseCertificate",
  "title" : "hl7VS-degreeLicenseCertificate",
  "status" : "active",
  "experimental" : false,
  "date" : "2019-12-01",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Concepts specifying an educational degree (e.g., MD).  Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging.  Used in Version 2 messaging; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7.",
  "copyright" : "Copyright HL7. Licensed under creative commons public domain",
  "compose" : {
    "include" : [{
      "system" : "http://terminology.hl7.org/CodeSystem/v2-0360",
      "version" : "2.1.0"
    }]
  }
}

```
