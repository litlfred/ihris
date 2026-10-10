# iHRIS Module - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Module**

## Resource Profile: iHRIS Module 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-module | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:IhrisModule |

 
iHRIS profile of Library resource to manage modules. 

**Usages:**

* Examples for this Profile: [ihris-example](Library-ihris-module-example.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-module.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-module.csv), [Excel](StructureDefinition-ihris-module.xlsx), [Schematron](StructureDefinition-ihris-module.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-module",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-module",
  "version" : "0.1.0",
  "name" : "IhrisModule",
  "title" : "iHRIS Module",
  "status" : "active",
  "date" : "2026-10-10T05:44:59+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS profile of Library resource to manage modules.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "w5",
    "uri" : "http://hl7.org/fhir/fivews",
    "name" : "FiveWs Pattern Mapping"
  },
  {
    "identity" : "workflow",
    "uri" : "http://hl7.org/fhir/workflow",
    "name" : "Workflow Pattern"
  },
  {
    "identity" : "objimpl",
    "uri" : "http://hl7.org/fhir/object-implementation",
    "name" : "Object Implementation Information"
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Library",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Library",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Library",
      "path" : "Library"
    },
    {
      "id" : "Library.name",
      "path" : "Library.name",
      "min" : 1
    },
    {
      "id" : "Library.title",
      "path" : "Library.title",
      "min" : 1
    },
    {
      "id" : "Library.type",
      "path" : "Library.type",
      "patternCodeableConcept" : {
        "coding" : [{
          "code" : "logic-library"
        }]
      }
    },
    {
      "id" : "Library.author",
      "path" : "Library.author",
      "min" : 1
    },
    {
      "id" : "Library.content",
      "path" : "Library.content",
      "slicing" : {
        "discriminator" : [{
          "type" : "pattern",
          "path" : "title"
        }],
        "rules" : "open"
      },
      "min" : 2,
      "max" : "2"
    },
    {
      "id" : "Library.content:Signature",
      "path" : "Library.content",
      "sliceName" : "Signature",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Library.content:Signature.contentType",
      "path" : "Library.content.contentType",
      "patternCode" : "text/x-sig"
    },
    {
      "id" : "Library.content:Signature.language",
      "path" : "Library.content.language",
      "max" : "0"
    },
    {
      "id" : "Library.content:Signature.data",
      "path" : "Library.content.data",
      "min" : 1
    },
    {
      "id" : "Library.content:Signature.url",
      "path" : "Library.content.url",
      "max" : "0"
    },
    {
      "id" : "Library.content:Signature.title",
      "path" : "Library.content.title",
      "min" : 1,
      "patternString" : "module-signature"
    },
    {
      "id" : "Library.content:Javascript",
      "path" : "Library.content",
      "sliceName" : "Javascript",
      "min" : 1,
      "max" : "1"
    },
    {
      "id" : "Library.content:Javascript.contentType",
      "path" : "Library.content.contentType",
      "patternCode" : "application/javascript"
    },
    {
      "id" : "Library.content:Javascript.language",
      "path" : "Library.content.language",
      "max" : "0"
    },
    {
      "id" : "Library.content:Javascript.data",
      "path" : "Library.content.data",
      "min" : 1
    },
    {
      "id" : "Library.content:Javascript.url",
      "path" : "Library.content.url",
      "max" : "0"
    },
    {
      "id" : "Library.content:Javascript.title",
      "path" : "Library.content.title",
      "min" : 1,
      "patternString" : "module-code"
    }]
  }
}

```
