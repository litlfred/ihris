# iHRIS Assign Role - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Assign Role**

## Extension: iHRIS Assign Role 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-assign-role | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisAssignRole |

iHRIS Assign Role to a user or other role.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Role](StructureDefinition-ihris-role.md)
* Examples for this Extension: [Basic/ihris-role-admin](Basic-ihris-role-admin.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-assign-role.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-assign-role.csv), [Excel](StructureDefinition-ihris-assign-role.xlsx), [Schematron](StructureDefinition-ihris-assign-role.sch) 

#### Terminology Bindings

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-assign-role",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-role",
  "version" : "0.1.0",
  "name" : "IhrisAssignRole",
  "title" : "iHRIS Assign Role",
  "status" : "active",
  "date" : "2026-10-09T11:48:54+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Assign Role to a user or other role.",
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
    "expression" : "Person"
  },
  {
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
      "short" : "iHRIS Assign Role",
      "definition" : "iHRIS Assign Role to a user or other role."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-assign-role"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "label" : "Role",
      "min" : 1,
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://ihris.org/fhir/StructureDefinition/ihris-role"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.value[x].reference",
      "path" : "Extension.value[x].reference",
      "label" : "Role"
    }]
  }
}

```
