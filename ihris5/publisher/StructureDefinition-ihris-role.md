# iHRIS Role - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Role**

## Resource Profile: iHRIS Role 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-role | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisRole |

 
iHRIS Profile of the Basic resource to manage roles. 

**Usages:**

* Refer to this Profile: [iHRIS Assign Role](StructureDefinition-ihris-assign-role.md)
* Examples for this Profile: [Basic/ihris-role-admin](Basic-ihris-role-admin.md), [Basic/ihris-role-open](Basic-ihris-role-open.md) and [Basic/ihris-role-self](Basic-ihris-role-self.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-role.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-role.csv), [Excel](StructureDefinition-ihris-role.xlsx), [Schematron](StructureDefinition-ihris-role.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-role",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-role",
  "version" : "0.1.0",
  "name" : "IhrisRole",
  "title" : "iHRIS Role",
  "status" : "active",
  "date" : "2026-10-09T12:31:23+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Profile of the Basic resource to manage roles.",
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
  }],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Basic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Basic",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Basic",
      "path" : "Basic"
    },
    {
      "id" : "Basic.extension",
      "path" : "Basic.extension",
      "slicing" : {
        "discriminator" : [{
          "type" : "value",
          "path" : "url"
        }],
        "ordered" : false,
        "rules" : "open"
      },
      "min" : 2
    },
    {
      "id" : "Basic.extension:name",
      "path" : "Basic.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-basic-name"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:primary",
      "path" : "Basic.extension",
      "sliceName" : "primary",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-role-primary"]
      }]
    },
    {
      "id" : "Basic.extension:primary.value[x]",
      "path" : "Basic.extension.value[x]",
      "mustSupport" : true
    },
    {
      "id" : "Basic.extension:role",
      "path" : "Basic.extension",
      "sliceName" : "role",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-assign-role"]
      }]
    },
    {
      "id" : "Basic.extension:task",
      "path" : "Basic.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Extension",
        "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-assign-task"]
      }]
    },
    {
      "id" : "Basic.code",
      "path" : "Basic.code",
      "patternCodeableConcept" : {
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
          "code" : "role"
        }]
      }
    }]
  }
}

```
