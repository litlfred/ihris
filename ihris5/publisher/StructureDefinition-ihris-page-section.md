# iHRIS Page Section - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **iHRIS Page Section**

## Extension: iHRIS Page Section 

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/StructureDefinition/ihris-page-section | *Version*:0.1.0 |
| Active as of 2026-10-09 | *Computable Name*:IhrisPageSection |

iHRIS Page Section information.

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [iHRIS Page](StructureDefinition-ihris-page.md)
* Examples for this Extension: [Basic/ihris-page-auditevent](Basic-ihris-page-auditevent.md), [Basic/ihris-page-role](Basic-ihris-page-role.md), [Basic/ihris-page-task](Basic-ihris-page-task.md), [Basic/ihris-page-test-codesystem](Basic-ihris-page-test-codesystem.md) and [Basic/ihris-page-test-practitioner](Basic-ihris-page-test-practitioner.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/ihris|current/StructureDefinition/StructureDefinition-ihris-page-section.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-ihris-page-section.csv), [Excel](StructureDefinition-ihris-page-section.xlsx), [Schematron](StructureDefinition-ihris-page-section.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "ihris-page-section",
  "url" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section",
  "version" : "0.1.0",
  "name" : "IhrisPageSection",
  "title" : "iHRIS Page Section",
  "status" : "active",
  "date" : "2026-10-09T12:24:20+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "iHRIS Page Section information.",
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
    "expression" : "IhrisPage"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "iHRIS Page Section",
      "definition" : "iHRIS Page Section information."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "min" : 3
    },
    {
      "id" : "Extension.extension:title",
      "path" : "Extension.extension",
      "sliceName" : "title",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:title.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:title.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "title"
    },
    {
      "id" : "Extension.extension:title.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Title",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:description",
      "path" : "Extension.extension",
      "sliceName" : "description",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:description.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:description.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "description"
    },
    {
      "id" : "Extension.extension:description.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Description",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:name",
      "path" : "Extension.extension",
      "sliceName" : "name",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:name.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:name.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "name"
    },
    {
      "id" : "Extension.extension:name.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Name",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field",
      "path" : "Extension.extension",
      "sliceName" : "field",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:field.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:field.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:field.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Field",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:hide",
      "path" : "Extension.extension",
      "sliceName" : "hide",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:hide.extension",
      "path" : "Extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:hide.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "hide"
    },
    {
      "id" : "Extension.extension:hide.value[x]",
      "path" : "Extension.extension.value[x]",
      "label" : "Hide",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource",
      "path" : "Extension.extension",
      "sliceName" : "resource",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension",
      "path" : "Extension.extension.extension",
      "min" : 3
    },
    {
      "id" : "Extension.extension:resource.extension:resource",
      "path" : "Extension.extension.extension",
      "sliceName" : "resource",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:resource.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:resource.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "resource"
    },
    {
      "id" : "Extension.extension:resource.extension:resource.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Secondary Resource",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/StructureDefinition"]
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:linkfield",
      "path" : "Extension.extension.extension",
      "sliceName" : "linkfield",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:linkfield.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:linkfield.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "linkfield"
    },
    {
      "id" : "Extension.extension:resource.extension:linkfield.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Secondary Resource Link Field",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:searchfield",
      "path" : "Extension.extension.extension",
      "sliceName" : "searchfield",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:searchfield.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:searchfield.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "searchfield"
    },
    {
      "id" : "Extension.extension:resource.extension:searchfield.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Secondary Resource Search Field (if different from the link field)",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:searchfieldtarget",
      "path" : "Extension.extension.extension",
      "sliceName" : "searchfieldtarget",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:searchfieldtarget.extension",
      "path" : "Extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:searchfieldtarget.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "searchfieldtarget"
    },
    {
      "id" : "Extension.extension:resource.extension:searchfieldtarget.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "label" : "Target Resource of the Secondary Resource Search Field",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column",
      "path" : "Extension.extension.extension",
      "sliceName" : "column",
      "min" : 1,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension",
      "path" : "Extension.extension.extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:header",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "header",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:header.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:header.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "header"
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:header.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Column Header",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:field",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "field",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:field.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:field.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "field"
    },
    {
      "id" : "Extension.extension:resource.extension:column.extension:field.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "FHIRPath Expression",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:column.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "column"
    },
    {
      "id" : "Extension.extension:resource.extension:column.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action",
      "path" : "Extension.extension.extension",
      "sliceName" : "action",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension",
      "path" : "Extension.extension.extension.extension",
      "min" : 2
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:link",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "link",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:link.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:link.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "link"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:link.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Action Link",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:text",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "text",
      "min" : 1,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:text.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:text.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "text"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:text.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Action Text",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:row",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "row",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:row.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:row.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "row"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:row.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Is Row Action?",
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:condition",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "condition",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:condition.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:condition.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "condition"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:condition.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "FHIRPation Condition do Display",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:emptyDisplay",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "emptyDisplay",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:emptyDisplay.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:emptyDisplay.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "emptyDisplay"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:emptyDisplay.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Show when no records?",
      "type" : [{
        "code" : "boolean"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:class",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "class",
      "min" : 0,
      "max" : "1",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:class.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:class.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "class"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:class.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Element Class for the Action",
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:role",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "role",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:role.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:role.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "role"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:role.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Roles that has access to the action",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:task",
      "path" : "Extension.extension.extension.extension",
      "sliceName" : "task",
      "min" : 0,
      "max" : "*",
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:task.extension",
      "path" : "Extension.extension.extension.extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:task.url",
      "path" : "Extension.extension.extension.extension.url",
      "fixedUri" : "task"
    },
    {
      "id" : "Extension.extension:resource.extension:action.extension:task.value[x]",
      "path" : "Extension.extension.extension.extension.value[x]",
      "label" : "Tasks that has access to the action",
      "type" : [{
        "code" : "id"
      }],
      "mustSupport" : true
    },
    {
      "id" : "Extension.extension:resource.extension:action.url",
      "path" : "Extension.extension.extension.url",
      "fixedUri" : "action"
    },
    {
      "id" : "Extension.extension:resource.extension:action.value[x]",
      "path" : "Extension.extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.extension:resource.url",
      "path" : "Extension.extension.url",
      "fixedUri" : "resource"
    },
    {
      "id" : "Extension.extension:resource.value[x]",
      "path" : "Extension.extension.value[x]",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://ihris.org/fhir/StructureDefinition/ihris-page-section"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "max" : "0"
    }]
  }
}

```
