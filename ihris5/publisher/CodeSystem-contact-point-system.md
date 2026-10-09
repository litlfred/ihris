# ContactPointSystem - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ContactPointSystem**

## CodeSystem: ContactPointSystem 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/contact-point-system | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:ContactPointSystem |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.72 | | |

 
Telecommunications form for contact point. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [ContactPointSystem](ValueSet-contact-point-system.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "contact-point-system",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:31.763+03:00",
    "source" : "#OYYfgAEe5Uwd9zzw"
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
  "url" : "http://hl7.org/fhir/contact-point-system",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.72"
  }],
  "version" : "0.1.0",
  "name" : "ContactPointSystem",
  "title" : "ContactPointSystem",
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
  "description" : "Telecommunications form for contact point.",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/contact-point-system",
  "content" : "complete",
  "count" : 7,
  "concept" : [{
    "code" : "phone",
    "display" : "Phone",
    "definition" : "The value is a telephone number used for voice calls. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required."
  },
  {
    "code" : "fax",
    "display" : "Fax",
    "definition" : "The value is a fax machine. Use of full international numbers starting with + is recommended to enable automatic dialing support but not required."
  },
  {
    "code" : "email",
    "display" : "Email",
    "definition" : "The value is an email address."
  },
  {
    "code" : "pager",
    "display" : "Pager",
    "definition" : "The value is a pager number. These may be local pager numbers that are only usable on a particular pager system."
  },
  {
    "code" : "url",
    "display" : "URL",
    "definition" : "A contact that is not a phone, fax, pager or email address and is expressed as a URL.  This is intended for various institutional or personal contacts including web sites, blogs, Skype, Twitter, Facebook, etc. Do not use for email addresses."
  },
  {
    "code" : "sms",
    "display" : "SMS",
    "definition" : "A contact that can be used for sending an sms message (e.g. mobile phones, some landlines)."
  },
  {
    "code" : "other",
    "display" : "Other",
    "definition" : "A contact that is not a phone, fax, page or email address and is not expressible as a URL.  E.g. Internal mail address.  This SHOULD NOT be used for contacts that are expressible as a URL (e.g. Skype, Twitter, Facebook, etc.)  Extensions may be used to distinguish \"other\" contact types."
  }]
}

```
