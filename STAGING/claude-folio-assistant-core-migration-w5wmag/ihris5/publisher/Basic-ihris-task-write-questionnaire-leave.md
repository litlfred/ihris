# iHRIS Task To Write Questionnaire ihris-leave - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Task To Write Questionnaire ihris-leave**

## Example Basic: iHRIS Task To Write Questionnaire ihris-leave

Profile: [iHRIS Task](StructureDefinition-ihris-task.md)

**iHRIS Basic Name**: write-questionnaire

> **Task Attributes**
* permission: write
* resource: Questionnaire
* instance: ihris-leave

**Composite Task**: [Basic iHRIS Task](Basic-ihris-task-read-questionnaire-resource.md)

**code**: iHRIS Task



## Resource Content

```json
{
  "resourceType" : "Basic",
  "id" : "ihris-task-write-questionnaire-leave",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-task"]
  },
  "extension" : [{
    "url" : "http://ihris.org/fhir/StructureDefinition/ihris-basic-name",
    "valueString" : "write-questionnaire"
  },
  {
    "extension" : [{
      "url" : "permission",
      "valueCode" : "write"
    },
    {
      "url" : "resource",
      "valueCode" : "Questionnaire"
    },
    {
      "url" : "instance",
      "valueId" : "ihris-leave"
    }],
    "url" : "http://ihris.org/fhir/StructureDefinition/task-attributes"
  },
  {
    "url" : "http://ihris.org/fhir/StructureDefinition/composite-task",
    "valueReference" : {
      "reference" : "Basic/ihris-task-read-questionnaire-resource"
    }
  }],
  "code" : {
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-resource-codesystem",
      "code" : "task"
    }]
  }
}

```
