# AuditEvent - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **AuditEvent**

## Example Basic: AuditEvent

Profile: [iHRIS Page](StructureDefinition-ihris-page.md)

> **iHRIS Page Display**
* resource: [StructureDefinition iHRIS Audit Event](StructureDefinition-ihris-auditevent.md)
* search: Id|AuditEvent.id
* search: User AltId|AuditEvent.agent.altId
* search: User|AuditEvent.agent.name
* search: Action|AuditEvent.subtype.display
* search: Resource|AuditEvent.entity.what.reference
* search: Outcome|AuditEvent.outcome
* search: Resource(If Error)|AuditEvent.entity.detail.where(type='resource').valueString
* search: Error|AuditEvent.entity.detail.where(type='error').valueString
* search: Time/Date|AuditEvent.recorded
* filter: Action|subtype|http://dicom.nema.org/resources/ontology/DCM
* filter: User AltId|altid
* filter: User|agent-name:contains
* filter: Date|date

> **iHRIS Page Section**
* title: Audit Events/Logs
* description: System Logs details
* name: AuditEvent
* field: AuditEvent.agent.altIdd
* field: AuditEvent.agent.name
* field: AuditEvent.subtype.display
* field: AuditEvent.entity.what.reference
* field: AuditEvent.outcome
* field: AuditEvent.recorded

**code**: iHRIS Page



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-page-auditevent",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-page"]
  },
  "extension" : [{
    "extension" : [{
      "url" : "resource",
      "valueReference" : {
        "reference" : "StructureDefinition/ihris-auditevent"
      }
    },
    {
      "url" : "search",
      "valueString" : "Id|AuditEvent.id"
    },
    {
      "url" : "search",
      "valueString" : "User AltId|AuditEvent.agent.altId"
    },
    {
      "url" : "search",
      "valueString" : "User|AuditEvent.agent.name"
    },
    {
      "url" : "search",
      "valueString" : "Action|AuditEvent.subtype.display"
    },
    {
      "url" : "search",
      "valueString" : "Resource|AuditEvent.entity.what.reference"
    },
    {
      "url" : "search",
      "valueString" : "Outcome|AuditEvent.outcome"
    },
    {
      "url" : "search",
      "valueString" : "Resource(If Error)|AuditEvent.entity.detail.where(type='resource').valueString"
    },
    {
      "url" : "search",
      "valueString" : "Error|AuditEvent.entity.detail.where(type='error').valueString"
    },
    {
      "url" : "search",
      "valueString" : "Time/Date|AuditEvent.recorded"
    },
    {
      "url" : "filter",
      "valueString" : "Action|subtype|http://dicom.nema.org/resources/ontology/DCM"
    },
    {
      "url" : "filter",
      "valueString" : "User AltId|altid"
    },
    {
      "url" : "filter",
      "valueString" : "User|agent-name:contains"
    },
    {
      "url" : "filter",
      "valueString" : "Date|date"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-display"
  },
  {
    "extension" : [{
      "url" : "title",
      "valueString" : "Audit Events/Logs"
    },
    {
      "url" : "description",
      "valueString" : "System Logs details"
    },
    {
      "url" : "name",
      "valueString" : "AuditEvent"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.agent.altIdd"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.agent.name"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.subtype.display"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.entity.what.reference"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.outcome"
    },
    {
      "url" : "field",
      "valueString" : "AuditEvent.recorded"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "page"
    }]
  }
}

```
