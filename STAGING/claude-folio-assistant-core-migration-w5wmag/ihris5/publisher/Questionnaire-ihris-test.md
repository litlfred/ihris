# iHRIS Test Questionnaire - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Test Questionnaire**

## Questionnaire: iHRIS Test Questionnaire 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/Questionnaire/ihris-test | *Version*:0.1.0 |
| Active as of 2020-06-24 | *Computable Name*:ihris-test |

 
iHRIS Test initial data entry questionnaire. 

 
Data entry page for test. 



## Resource Content

```json
{
  "resourceType" : "Questionnaire",
  "id" : "ihris-test",
  "url" : "http://ihris.org/fhir/Questionnaire/ihris-test",
  "version" : "0.1.0",
  "name" : "ihris-test",
  "title" : "iHRIS Test Questionnaire",
  "status" : "active",
  "date" : "2020-06-24",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Test initial data entry questionnaire.",
  "purpose" : "Data entry page for test.",
  "item" : [{
    "linkId" : "Practitioner",
    "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner",
    "text" : "Health Worker|Primary demographic details",
    "type" : "group",
    "item" : [{
      "linkId" : "Practitioner.name[0]",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.name",
      "text" : "Name",
      "type" : "group",
      "item" : [{
        "linkId" : "Practitioner.name[0].use",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.name.use",
        "text" : "Name Usage",
        "type" : "choice",
        "required" : true,
        "repeats" : false,
        "readOnly" : true,
        "answerOption" : [{
          "valueCoding" : {
            "system" : "http://hl7.org/fhir/name-use",
            "code" : "official"
          },
          "initialSelected" : true
        }]
      },
      {
        "linkId" : "Practitioner.name[0].family",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.name.family",
        "text" : "Family Name",
        "type" : "string",
        "required" : true,
        "repeats" : false
      },
      {
        "linkId" : "Practitioner.name[0].given[0]",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.name.given",
        "text" : "Given Name(s)",
        "type" : "string",
        "required" : true,
        "repeats" : true
      }]
    },
    {
      "linkId" : "Practitioner.birthDate",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.birthDate",
      "text" : "Date of Birth",
      "type" : "date",
      "required" : false,
      "repeats" : false
    },
    {
      "linkId" : "Practitioner.gender",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.gender",
      "text" : "Gender",
      "type" : "choice",
      "required" : false,
      "repeats" : false,
      "answerValueSet" : "http://hl7.org/fhir/ValueSet/administrative-gender"
    }]
  },
  {
    "linkId" : "__Practitioner:contact",
    "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner",
    "text" : "Contact Details|Address, email, phone numbers",
    "type" : "group",
    "item" : [{
      "linkId" : "Practitioner.telecom[0].use",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.use",
      "text" : "Telecom Use",
      "type" : "choice",
      "required" : true,
      "repeats" : false,
      "readOnly" : true,
      "answerOption" : [{
        "valueCoding" : {
          "system" : "http://hl7.org/fhir/contact-point-use",
          "code" : "mobile"
        },
        "initialSelected" : true
      }]
    },
    {
      "linkId" : "Practitioner.telecom[0].system",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.system",
      "text" : "Telecom System",
      "type" : "choice",
      "required" : true,
      "repeats" : false,
      "readOnly" : true,
      "answerOption" : [{
        "valueCoding" : {
          "system" : "http://hl7.org/fhir/contact-point-system",
          "code" : "phone"
        },
        "initialSelected" : true
      }]
    },
    {
      "linkId" : "Practitioner.telecom[0].value",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.value",
      "text" : "Mobile Phone",
      "type" : "string",
      "required" : false,
      "repeats" : false
    },
    {
      "linkId" : "Practitioner.telecom[1].use",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.use",
      "text" : "Telecom Use",
      "type" : "choice",
      "required" : true,
      "repeats" : false,
      "readOnly" : true,
      "answerOption" : [{
        "valueCoding" : {
          "system" : "http://hl7.org/fhir/contact-point-use",
          "code" : "work"
        },
        "initialSelected" : true
      }]
    },
    {
      "linkId" : "Practitioner.telecom[1].system",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.system",
      "text" : "Telecom System",
      "type" : "choice",
      "required" : true,
      "repeats" : false,
      "readOnly" : true,
      "answerOption" : [{
        "valueCoding" : {
          "system" : "http://hl7.org/fhir/contact-point-system",
          "code" : "email"
        },
        "initialSelected" : true
      }]
    },
    {
      "linkId" : "Practitioner.telecom[1].value",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.telecom.value",
      "text" : "Work Email",
      "type" : "string",
      "required" : false,
      "repeats" : false
    }]
  },
  {
    "linkId" : "PractitionerRole",
    "definition" : "http://hl7.org/fhir/StructureDefinition/PractitionerRole",
    "text" : "Position|Position the person holds",
    "type" : "group",
    "item" : [{
      "linkId" : "PractitionerRole.code",
      "definition" : "http://hl7.org/fhir/StructureDefinition/PractitionerRole#PractitionerRole.code",
      "text" : "Job Title",
      "type" : "choice",
      "required" : true,
      "repeats" : false,
      "answerValueSet" : "http://ihris.org/fhir/ValueSet/ihris-job"
    },
    {
      "linkId" : "PractitionerRole.period.start",
      "definition" : "http://hl7.org/fhir/StructureDefinition/PractitionerRole#PractitionerRole.period.start",
      "text" : "Start Date",
      "type" : "date",
      "required" : true,
      "repeats" : false
    }]
  },
  {
    "linkId" : "Practitioner.identifier",
    "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner",
    "text" : "Identifiers|Identifiers for the practitioner",
    "type" : "group",
    "item" : [{
      "linkId" : "Practitioner.identifier[0]",
      "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.identifier",
      "text" : "Identifier",
      "type" : "group",
      "required" : false,
      "repeats" : true,
      "item" : [{
        "linkId" : "Practitioner.identifier[0].system",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.identifier.system",
        "text" : "System",
        "type" : "string",
        "required" : false,
        "repeats" : false
      },
      {
        "linkId" : "Practitioner.identifier[0].value",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.identifier.value",
        "text" : "ID Number",
        "type" : "string",
        "required" : false,
        "repeats" : false
      },
      {
        "linkId" : "Practitioner.identifier[0].type",
        "definition" : "http://hl7.org/fhir/StructureDefinition/Practitioner#Practitioner.identifier.type",
        "text" : "ID Type",
        "type" : "choice",
        "required" : false,
        "repeats" : false,
        "answerValueSet" : "http://hl7.org/fhir/ValueSet/identifier-type"
      }]
    }]
  }]
}

```
