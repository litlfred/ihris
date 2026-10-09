# iHRIS Task To Read AuditEvent resource - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Read AuditEvent resource**

## Example Basic: iHRIS Task To Read AuditEvent resource

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: read-auditevent-resource

> **Task Attributes**
* permission: read
* resource: AuditEvent

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-read-auditevent-resource",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "read-auditevent-resource"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "read"
    },
    {
      "url" : "resource",
      "valueCode" : "AuditEvent"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "task"
    }]
  }
}

```
