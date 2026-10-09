# iHRIS About Page - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS About Page**

## Example DocumentReference: iHRIS About Page

Profile: [iHRIS Document](StructureDefinition-ihris-document.md)

**status**: Current

**docStatus**: Final

**category**: Open Access

**date**: 2020-06-07 14:54:00+0000

> **content**

### Attachments

| | | | |
| :--- | :--- | :--- | :--- |
| - | **ContentType** | **Data** | **Title** |
| * | text/markdown | `IyBBYm91dCBpSFJJUwoKVGhpcyBpcyBhIHRlc3RpbmcgYWJvdXQgcGFnZS4K` | About iHRIS |




## Resource Content

```json
{
  "resourceType" : "DocumentReference",
  "id" : "page-about",
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
  "date" : "2020-06-07T14:54:00Z",
  "content" : [{
    "attachment" : {
      "contentType" : "text/markdown",
      "data" : "IyBBYm91dCBpSFJJUwoKVGhpcyBpcyBhIHRlc3RpbmcgYWJvdXQgcGFnZS4K",
      "title" : "About iHRIS"
    }
  }]
}

```
