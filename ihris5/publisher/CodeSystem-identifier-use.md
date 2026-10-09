# IdentifierUse - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **IdentifierUse**

## CodeSystem: IdentifierUse 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/identifier-use | *Version*:0.1.0 | |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 5 | *Computable Name*:IdentifierUse |
| *Other Identifiers:*OID:2.16.840.1.113883.4.642.4.58 | | |

 
Identifies the purpose for this identifier, if known . 

 This Code system is referenced in the content logical definition of the following value sets: 

* [IdentifierUse](ValueSet-identifier-use.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "identifier-use",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:14:40.194+03:00",
    "source" : "#MwLVKPjy1CijmhDQ"
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
  "url" : "http://hl7.org/fhir/identifier-use",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:2.16.840.1.113883.4.642.4.58"
  }],
  "version" : "0.1.0",
  "name" : "IdentifierUse",
  "title" : "IdentifierUse",
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
  "description" : "Identifies the purpose for this identifier, if known .",
  "caseSensitive" : true,
  "valueSet" : "http://hl7.org/fhir/ValueSet/identifier-use",
  "content" : "complete",
  "count" : 5,
  "concept" : [{
    "code" : "usual",
    "display" : "Usual",
    "definition" : "The identifier recommended for display and use in real-world interactions."
  },
  {
    "code" : "official",
    "display" : "Official",
    "definition" : "The identifier considered to be most trusted for the identification of this item. Sometimes also known as \"primary\" and \"main\". The determination of \"official\" is subjective and implementation guides often provide additional guidelines for use."
  },
  {
    "code" : "temp",
    "display" : "Temp",
    "definition" : "A temporary identifier."
  },
  {
    "code" : "secondary",
    "display" : "Secondary",
    "definition" : "An identifier that was assigned in secondary use - it serves to identify the object in a relative context, but cannot be consistently assigned to the same object again in a different context."
  },
  {
    "code" : "old",
    "display" : "Old",
    "definition" : "The identifier id no longer considered valid, but may be relevant for search purposes.  E.g. Changes to identifier schemes, account merges, etc."
  }]
}

```
