# ContactPoint - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **ContactPoint**

## Data Type Profile: ContactPoint 

| | |
| :--- | :--- |
| *Official URL*:http://hl7.org/fhir/StructureDefinition/ContactPoint | *Version*:0.1.0 |
| * Standards status: *[Normative](http://hl7.org/fhir/R4/versions.html#std-process) | *Computable Name*:ContactPoint |

 
Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc. 

 
Need to track phone, fax, mobile, sms numbers, email addresses, twitter tags, etc. 

**Usages:**

* This DataType is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ContactPoint.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ContactPoint.csv), [Excel](StructureDefinition-ContactPoint.xlsx), [Schematron](StructureDefinition-ContactPoint.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ContactPoint",
  "meta" : {
    "versionId" : "1",
    "lastUpdated" : "2022-02-15T08:18:57.172+03:00",
    "source" : "#rMQE1iMv80qInhAV"
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "normative"
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-normative-version",
    "valueCode" : "4.0.0"
  }],
  "url" : "http://hl7.org/fhir/StructureDefinition/ContactPoint",
  "version" : "0.1.0",
  "name" : "ContactPoint",
  "status" : "active",
  "date" : "2018-12-27T10:06:46-05:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.",
  "purpose" : "Need to track phone, fax, mobile, sms numbers, email addresses, twitter tags, etc.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "servd",
    "uri" : "http://www.omg.org/spec/ServD/1.0/",
    "name" : "ServD"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "type" : "ContactPoint",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Element",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "ContactPoint",
      "extension" : [{
        "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
        "valueCode" : "normative"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-normative-version",
        "valueCode" : "4.0.0"
      }],
      "path" : "ContactPoint",
      "short" : "Details of a Technology mediated contact point (phone, fax, email, etc.)",
      "definition" : "Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.",
      "min" : 0,
      "max" : "*",
      "constraint" : [{
        "key" : "cpt-2",
        "severity" : "error",
        "human" : "A system is required if a value is provided.",
        "expression" : "value.empty() or system.exists()",
        "xpath" : "not(exists(f:value)) or exists(f:system)"
      }],
      "mapping" : [{
        "identity" : "v2",
        "map" : "XTN"
      },
      {
        "identity" : "rim",
        "map" : "TEL"
      },
      {
        "identity" : "servd",
        "map" : "ContactPoint"
      }]
    },
    {
      "id" : "ContactPoint.system",
      "path" : "ContactPoint.system",
      "short" : "phone | fax | email | pager | url | sms | other",
      "definition" : "Telecommunications form for contact point - what communications system is required to make use of the contact.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "condition" : ["cpt-2"],
      "isSummary" : true,
      "binding" : {
        "extension" : [{
          "url" : "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
          "valueString" : "ContactPointSystem"
        }],
        "strength" : "required",
        "description" : "Telecommunications form for contact point.",
        "valueSet" : "http://hl7.org/fhir/ValueSet/contact-point-system|4.0.0"
      },
      "mapping" : [{
        "identity" : "v2",
        "map" : "XTN.3"
      },
      {
        "identity" : "rim",
        "map" : "./scheme"
      },
      {
        "identity" : "servd",
        "map" : "./ContactPointType"
      }]
    },
    {
      "id" : "ContactPoint.value",
      "path" : "ContactPoint.value",
      "short" : "The actual contact point details",
      "definition" : "The actual contact point details, in a form that is meaningful to the designated communication system (i.e. phone number or email address).",
      "comment" : "Additional text data such as phone extension numbers, or notes about use of the contact are sometimes included in the value.",
      "requirements" : "Need to support legacy numbers that are not in a tightly controlled format.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }],
      "isSummary" : true,
      "mapping" : [{
        "identity" : "v2",
        "map" : "XTN.1 (or XTN.12)"
      },
      {
        "identity" : "rim",
        "map" : "./url"
      },
      {
        "identity" : "servd",
        "map" : "./Value"
      }]
    },
    {
      "id" : "ContactPoint.use",
      "path" : "ContactPoint.use",
      "short" : "home | work | temp | old | mobile - purpose of this contact point",
      "definition" : "Identifies the purpose for the contact point.",
      "comment" : "Applications can assume that a contact is current unless it explicitly says that it is temporary or old.",
      "requirements" : "Need to track the way a person uses this contact, so a user can choose which is appropriate for their purpose.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "isModifier" : true,
      "isModifierReason" : "This is labeled as \"Is Modifier\" because applications should not mistake a temporary or old contact etc.for a current/permanent one",
      "isSummary" : true,
      "binding" : {
        "extension" : [{
          "url" : "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
          "valueString" : "ContactPointUse"
        }],
        "strength" : "required",
        "description" : "Use of contact point.",
        "valueSet" : "http://hl7.org/fhir/ValueSet/contact-point-use|4.0.0"
      },
      "mapping" : [{
        "identity" : "v2",
        "map" : "XTN.2 - but often indicated by field"
      },
      {
        "identity" : "rim",
        "map" : "unique(./use)"
      },
      {
        "identity" : "servd",
        "map" : "./ContactPointPurpose"
      }]
    },
    {
      "id" : "ContactPoint.rank",
      "path" : "ContactPoint.rank",
      "short" : "Specify preferred order of use (1 = highest)",
      "definition" : "Specifies a preferred order in which to use a set of contacts. ContactPoints with lower rank values are more preferred than those with higher rank values.",
      "comment" : "Note that rank does not necessarily follow the order in which the contacts are represented in the instance.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "positiveInt"
      }],
      "isSummary" : true,
      "mapping" : [{
        "identity" : "v2",
        "map" : "n/a"
      },
      {
        "identity" : "rim",
        "map" : "n/a"
      }]
    },
    {
      "id" : "ContactPoint.period",
      "path" : "ContactPoint.period",
      "short" : "Time period when the contact point was/is in use",
      "definition" : "Time period when the contact point was/is in use.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "Period"
      }],
      "isSummary" : true,
      "mapping" : [{
        "identity" : "v2",
        "map" : "N/A"
      },
      {
        "identity" : "rim",
        "map" : "./usablePeriod[type=\"IVL<TS>\"]"
      },
      {
        "identity" : "servd",
        "map" : "./StartDate and ./EndDate"
      }]
    }]
  }
}

```
