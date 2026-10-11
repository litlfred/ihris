# page-home - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **page-home**

## Example DocumentReference: page-home

Profile: [iHRIS Document](StructureDefinition-ihris-document.md)

**status**: Current

**docStatus**: Final

**category**: Open Access

**date**: 2020-08-19 14:54:00+0000

> **content**

### Attachments

| | | | |
| :--- | :--- | :--- | :--- |
| - | **ContentType** | **Data** | **Title** |
| * | text/markdown | `KipXZWxjb21lIHRvIHRoZSBpSFJJUyBEZW1vKioK` | iHRIS Demo |




## Resource Content

```json
{
  "resourceType" : "DocumentReference",
  "id" : "page-home",
  "meta" : {
    "profile" : ["http://ihris.org/fhir/StructureDefinition/ihris-document"]
  },
  "status" : "current",
  "docStatus" : "final",
  "category" : [{
    "coding" : [{
      "system" : "http://ihris.org/fhir/CodeSystem/ihris-document-category",
      "code" : "open",
      "display" : "Open Access"
    }]
  }],
  "date" : "2020-08-19T14:54:00Z",
  "content" : [{
    "attachment" : {
      "contentType" : "text/markdown",
      "data" : "KipXZWxjb21lIHRvIHRoZSBpSFJJUyBEZW1vKioK",
      "title" : "iHRIS Demo"
    }
  }]
}

```
