# iHRIS Role Primary - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Role Primary**

## Extension: iHRIS Role Primary 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-role-primary | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisRolePrimary |

iHRIS flag for roles to indicate a primary role for assignment to users.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Role](StructureDefinition-ihris-role.md)
* Examples for this Extension: [Basic/ihris-role-admin](Basic-ihris-role-admin.md), [Basic/ihris-role-open](Basic-ihris-role-open.md) and [Basic/ihris-role-self](Basic-ihris-role-self.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-role-primary.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-role-primary.csv), [Excel](StructureDefinition-ihris-role-primary.xlsx), [Schematron](StructureDefinition-ihris-role-primary.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-role-primary",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-role-primary",
  "version" : "0.1.0",
  "name" : "IhrisRolePrimary",
  "title" : "iHRIS Role Primary",
  "status" : "active",
  "date" : "2026-10-09T12:24:25+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS flag for roles to indicate a primary role for assignment to users.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "IhrisRole"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Role Primary",
      "definition" : "iHRIS flag for roles to indicate a primary role for assignment to users."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-role-primary"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "boolean"
      }]
    }]
  }
}

```
