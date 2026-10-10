# Home - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:http://ihris.org/fhir/ImplementationGuide/ihris | *Version*:0.1.0 |
| Active as of 2026-10-10 | *Computable Name*:iHRISImplementationGuide |

# iHRIS Health Workforce Information Systems Software implementation Guide

This **iHRIS implementation Guide** describes the set up of iHRIS (configs, modules, Library ) and data (Practitioner,PractitionerRole, Organization e.t.c) needed to have the intergrated Human Resource Information System. This guide was put together by **IntraHealth International** is a based on FHIR and HL7.

### Background

iHRIS, IntraHealth International's free, open source software, helps countries around the world track and manage their health workforce data to improve access to services. Countries use it to capture and maintain high-quality information for health workforce planning, management, regulation, and training.

Demo or download the current version of iHRIS.

iHRIS is built on a flexible framework that allows ministries of health, professional councils, and health service delivery organizations to adapt applications for a wide variety of uses. Developed in collaboration with national stakeholders beginning in 2005, with support from USAID, iHRIS is used in more than 20 countries to manage over a million health worker records at a potential cost savings of over $275 million when compared to commercial software.

### Key Approaches

iHRIS has been developed into multiple, interoperable applications to meet the needs of a variety of stakeholders and support health workers throughout their life cycle:

```
- iHRIS Manage allows tracking and management of health workers actively engaged in service delivery
- iHRIS Qualify enables professional councils and associations to register, license, and regulate health workers to support increased quality of care
- iHRIS Plan projects the likely changes in the health workforce under different scenarios and compares them with projected needs
- iHRIS Retain, developed in collaboration with the World Health Organization, helps countries plan and cost recruitment and retention interventions
- iHRIS Train assists in tracking and managing health worker preservice education pipelines and in-service training.

```

**Global Support Community:** We open access to iHRIS through publishing the software, source code, and other resources at www.ihris.org and by supporting a global community of software developers and information technologists with an online forum and interactive discussions and training sessions. The community raises and resolves technical issues on its own; contributes code to iHRIS; provides tools, guidance, and case studies for the iHRIS Implementation Toolkit; and translates iHRIS applications into other languages.

**International Standards and Interoperability:** iHRIS conforms to a variety of international standards for data exchange to ensure that data that might otherwise be siloed are accessible to all parts of a health system. We worked with an international standards organization, Integrating the Healthcare Enterprise, to develop a new global standard for exchanging health worker information. In addition, IntraHealth has collaborated in the Open Health Information Exchange (OpenHIE) initiative, including leading the development of a health worker registry that enables countries to link the various systems (including iHRIS) in their health information architecture.

### Building iHRIS IG

#### FHIR ShortHand Files

iHRIS IG is developed in [FHIR Shorthand (FSH)](http://build.fhir.org/ig/HL7/fhir-shorthand/), a domain-specific language (DSL) for defining the content of FHIR Implementation Guides (IG).

After you check out iHRIS IG from Github, add the **.fsh** files for your profiles, codesystems, valuesets e.t.c in **/fsh/** folder

#### Set iHRIS IG template paths

You need to set the path to the iHRIS IG template folder or else the publisher will give errors. To do this go to the **/fsh/ig-data/ig.ini** and then set the template value to the full path to the **/fsh/ig-data/ihristemplate** i.e **/User/nobert/FHIR/iHRIS/fsh/ig-data/ihristemplate**

#### Compiling with SUSHI

Install SUSHI (the FSH compiler), [as instructed here](http://build.fhir.org/ig/HL7/fhir-shorthand/sushi.html).

To compile iHRIS IG, open a command window and navigate to the directory where iHRIS IG has been checked out. Issue the following command:

`$ sushi fsh -o .

NOTE: With the latest publisher, sushi is part of the package, so you can sometimes skip the above step.

#### Running the IG Publisher

Next,

Download the latest publisher using this **_updatePublisher.sh** file like this on linux `./_updatePublisher.sh`

Now run:

LINUX: `JAVA -jar input-cache/org.hl7.fhir.publisher.jar -ig .`

This will run the HL7 IG Publisher, which will take several minutes to complete. After the publisher is finished, open the file **/output/index.html** to see the resulting IG.

### Further Customization of the IG

Introduce customizations of the IG into the following files:

* **Menus:** Edit the **/input/include/menu.xml** file
* **List of pages and artifacts to be included in the IG:** Edit **/input/ImplementationGuide-ihris.ig.json** file. See [ImplementationGuide resource](https://www.hl7.org/fhir/implementationguide.html) for details.
* **Additional pages, images, other content:** Add files to **/input/pagecontent** directory, and link them to menus or other pages.
* **Version history:** Edit **/package-list.json**.



## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "ihris",
  "url" : "http://ihris.org/fhir/ImplementationGuide/ihris",
  "version" : "0.1.0",
  "name" : "iHRISImplementationGuide",
  "title" : "iHRIS Implementation Guide",
  "status" : "active",
  "date" : "2026-10-10T05:51:05+00:00",
  "publisher" : "Luke Duncan",
  "contact" : [{
    "name" : "Luke Duncan",
    "telecom" : [{
      "system" : "email",
      "value" : "lduncan@intrahealth.org"
    }]
  }],
  "description" : "Conformance resources that define the base installation of iHRIS 5",
  "packageId" : "ihris",
  "license" : "CC0-1.0",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [{
    "id" : "hl7tx",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on HL7 Terminology"
    }],
    "uri" : "http://terminology.hl7.org/ImplementationGuide/hl7.terminology",
    "packageId" : "hl7.terminology.r4",
    "version" : "7.4.0"
  },
  {
    "id" : "hl7ext",
    "extension" : [{
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/implementationguide-dependency-comment",
      "valueMarkdown" : "Automatically added as a dependency - all IGs depend on the HL7 Extension Pack"
    }],
    "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
    "packageId" : "hl7.fhir.uv.extensions.r4",
    "version" : "5.3.0"
  }],
  "definition" : {
    "extension" : [{
      "extension" : [{
        "url" : "code",
        "valueString" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2020+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "CI Build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "show-inherited-invariants"
      },
      {
        "url" : "value",
        "valueString" : "false"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://ihris.org/fhir/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
      "valueCode" : "hl7.fhir.uv.tools.r4#1.1.2"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2020+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "CI Build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "show-inherited-invariants"
      },
      {
        "url" : "value",
        "valueString" : "false"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://ihris.org/fhir/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    }],
    "resource" : [{
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-active-user.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/active-user"
      },
      "name" : "active-user",
      "description" : "Search by active status for a Person resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-address-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/address-type"
      },
      "name" : "AddressType",
      "description" : "The type of an address (physical / postal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-address-type.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/address-type"
      },
      "name" : "AddressType",
      "description" : "The type of an address (physical / postal).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-address-use.html"
      }],
      "reference" : {
        "reference" : "ValueSet/address-use"
      },
      "name" : "AddressUse",
      "description" : "The use of an address.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-address-use.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/address-use"
      },
      "name" : "AddressUse",
      "description" : "The use of an address.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-administrative-gender.html"
      }],
      "reference" : {
        "reference" : "ValueSet/administrative-gender"
      },
      "name" : "AdministrativeGender",
      "description" : "The gender of a person used for administrative purposes.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-administrative-gender.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/administrative-gender"
      },
      "name" : "AdministrativeGender",
      "description" : "The gender of a person used for administrative purposes.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-page-auditevent.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-page-auditevent"
      },
      "name" : "AuditEvent",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-page"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-basic-location-constraint.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/basic-location-constraint"
      },
      "name" : "basic-location-constraint",
      "description" : "Search by related location for a Basic resource Role.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-basic-name.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/basic-name"
      },
      "name" : "basic-name",
      "description" : "Search by name for a Basic resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-basic-practitioner.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/basic-practitioner"
      },
      "name" : "basic-practitioner",
      "description" : "Search by practitioner for a Basic resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-basic-related-location.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/basic-related-location"
      },
      "name" : "basic-related-location",
      "description" : "Search by related location for a Basic resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-basic-related-practitioner.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/basic-related-practitioner"
      },
      "name" : "basic-related-practitioner",
      "description" : "Search by related practitioner for a Basic resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-currencies.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/currencies"
      },
      "name" : "Code System for Currencies.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-document-category.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-document-category"
      },
      "name" : "Code system for document categories.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-document-category.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-document-category"
      },
      "name" : "Code system for document categories.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-resource-codesystem.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-resource-codesystem"
      },
      "name" : "Code System for iHRIS Basic Resources.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-task-permission.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-task-permission"
      },
      "name" : "Code system for task permissions.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-task-resource.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-task-resource"
      },
      "name" : "Code system for task permissions.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-task-permission.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-task-permission"
      },
      "name" : "Code system for task permissions.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-task-resource.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-task-resource"
      },
      "name" : "Code system for task permissions.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-languages.html"
      }],
      "reference" : {
        "reference" : "ValueSet/languages"
      },
      "name" : "Common Languages",
      "description" : "This value set includes common codes from BCP-47 (http://tools.ietf.org/html/bcp47)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-composite-task.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/composite-task"
      },
      "name" : "Composite Task",
      "description" : "Tasks Inheritance",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-contactentity-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/contactentity-type"
      },
      "name" : "Contact entity type",
      "description" : "This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-contactentity-type.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/contactentity-type"
      },
      "name" : "Contact entity type",
      "description" : "This example value set defines a set of codes that can be used to indicate the purpose for which you would contact a contact party.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:complex-type"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ContactPoint.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ContactPoint"
      },
      "name" : "ContactPoint",
      "description" : "Base StructureDefinition for ContactPoint Type: Details for all kinds of technology mediated contact points for a person or organization, including telephone, email, etc.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-contact-point-system.html"
      }],
      "reference" : {
        "reference" : "ValueSet/contact-point-system"
      },
      "name" : "ContactPointSystem",
      "description" : "Telecommunications form for contact point.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-contact-point-system.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/contact-point-system"
      },
      "name" : "ContactPointSystem",
      "description" : "Telecommunications form for contact point.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-contact-point-use.html"
      }],
      "reference" : {
        "reference" : "ValueSet/contact-point-use"
      },
      "name" : "ContactPointUse",
      "description" : "Use of contact point.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-contact-point-use.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/contact-point-use"
      },
      "name" : "ContactPointUse",
      "description" : "Use of contact point.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Bundle"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Bundle-Country.html"
      }],
      "reference" : {
        "reference" : "Bundle/Country"
      },
      "name" : "Country",
      "exampleBoolean" : true
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-currencies.html"
      }],
      "reference" : {
        "reference" : "ValueSet/currencies"
      },
      "name" : "CurrencyCode",
      "description" : "Currency codes from ISO 4217 (see https://www.iso.org/iso-4217-currency-codes.html)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-days-of-week.html"
      }],
      "reference" : {
        "reference" : "ValueSet/days-of-week"
      },
      "name" : "DaysOfWeek",
      "description" : "The days of the week.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-days-of-week.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/days-of-week"
      },
      "name" : "DaysOfWeek",
      "description" : "The days of the week.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-3654.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/3654"
      },
      "name" : "degreeLicenseCertificate",
      "description" : "Code system of concepts specifying an educational degree (e.g., MD).  Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging.  Used in HL7 Version 2.x messaging in the CNN segment; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-iHRISReportDetails.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/iHRISReportDetails"
      },
      "name" : "Details of a report",
      "description" : "Defines the primary resource of the relationship",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-employment-status-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/employment-status-search"
      },
      "name" : "employment-status-search",
      "description" : "Search for a practitionerRole employment-status.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-gofr-search-isbroadcast.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/gofr-search-isbroadcast"
      },
      "name" : "gofr-search-isbroadcast",
      "description" : "search parameter for broadcasted messages",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-gofr-search-isflowstart.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/gofr-search-isflowstart"
      },
      "name" : "gofr-search-isflowstart",
      "description" : "search parameter for flow starts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-v2-0360.html"
      }],
      "reference" : {
        "reference" : "ValueSet/v2-0360"
      },
      "name" : "hl7VS-degreeLicenseCertificate",
      "description" : "Concepts specifying an educational degree (e.g., MD).  Used in the CNN datatype (names and identifiers of clinicians) in Version 2 messaging.  Used in Version 2 messaging; note that in releases of HL7 prior to 2.3.1, was also used in person names (XPN), but this use was deprecated, then withdrawn in 2.7.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-identifier-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/identifier-type"
      },
      "name" : "IdentifierType",
      "description" : "A coded type for an identifier that can be used to determine which identifier to use for a specific purpose.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-2103.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/2103"
      },
      "name" : "identifierType",
      "description" : "HL7-defined code system of concepts specifying type of identifier. Used in HL7 Version 2.x messaging data types CX, PLN, PPN, XCN and XON.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-identifier-use.html"
      }],
      "reference" : {
        "reference" : "ValueSet/identifier-use"
      },
      "name" : "IdentifierUse",
      "description" : "Identifies the purpose for this identifier, if known .",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-identifier-use.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/identifier-use"
      },
      "name" : "IdentifierUse",
      "description" : "Identifies the purpose for this identifier, if known .",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-IHE.mCSD.FacilityLocation.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/IHE.mCSD.FacilityLocation"
      },
      "name" : "IHEmCSDFacilityLocation",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-IHE.mCSD.Location.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/IHE.mCSD.Location"
      },
      "name" : "IHEmCSDLocation",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "DocumentReference"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "DocumentReference-page-about.html"
      }],
      "reference" : {
        "reference" : "DocumentReference/page-about"
      },
      "name" : "iHRIS About Page",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-document"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Questionnaire-ihris-task.html"
      }],
      "reference" : {
        "reference" : "Questionnaire/ihris-task"
      },
      "name" : "iHRIS Add Task Workflow",
      "description" : "iHRIS workflow to record a Role",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Questionnaire-ihris-role.html"
      }],
      "reference" : {
        "reference" : "Questionnaire/ihris-role"
      },
      "name" : "iHRIS AddRole Workflow",
      "description" : "iHRIS workflow to record a Role",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-role-admin.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-role-admin"
      },
      "name" : "iHRIS Admin Role",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-role"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-assign-role.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-assign-role"
      },
      "name" : "iHRIS Assign Role",
      "description" : "iHRIS Assign Role to a user or other role.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-assign-task.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-assign-task"
      },
      "name" : "iHRIS Assign Task",
      "description" : "iHRIS Assign Task to a user or other task.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-auditevent.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-auditevent"
      },
      "name" : "iHRIS Audit Event",
      "description" : "iHRIS profile for AuditEvent",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-basic-name.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-basic-name"
      },
      "name" : "iHRIS Basic Name",
      "description" : "iHRIS name field for basic resources.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-cadre.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-cadre"
      },
      "name" : "iHRIS Cadre",
      "description" : "Sample iHRIS ValueSet for: IhrisCadre",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-cadre.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-cadre"
      },
      "name" : "iHRIS Cadre",
      "description" : "Sample iHRIS CodeSystem for: IhrisCadre",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-classification.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-classification"
      },
      "name" : "iHRIS Classification",
      "description" : "Sample iHRIS ValueSet for: IhrisClassification",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-classification.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-classification"
      },
      "name" : "iHRIS Classification",
      "description" : "Sample iHRIS CodeSystem for: IhrisClassification",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-dashboard.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-dashboard"
      },
      "name" : "iHRIS Dashboard",
      "description" : "iHRIS Profile of the Basic resource to manage dashboards.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-dashboard-visualization.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-dashboard-visualization"
      },
      "name" : "iHRIS Dashboard Visualization",
      "description" : "iHRIS Dashboard Visualization",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-data-visualization.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-data-visualization"
      },
      "name" : "iHRIS Data Visualizer",
      "description" : "iHRIS Profile of the Basic resource to manage visualizations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-document.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-document"
      },
      "name" : "iHRIS Document",
      "description" : "iHRIS Profile of the DocumentReference resource to manage static documents.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-job.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-job"
      },
      "name" : "iHRIS Job",
      "description" : "Sample iHRIS ValueSet for: IhrisJob",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-job.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-job"
      },
      "name" : "iHRIS Job",
      "description" : "Sample iHRIS CodeSystem for: IhrisJob",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-module.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-module"
      },
      "name" : "iHRIS Module",
      "description" : "iHRIS profile of Library resource to manage modules.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Library"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Library-ihris-module-example.html"
      }],
      "reference" : {
        "reference" : "Library/ihris-module-example"
      },
      "name" : "iHRIS Module Example",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-module"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-role-open.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-role-open"
      },
      "name" : "iHRIS Open Role",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-role"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-page.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-page"
      },
      "name" : "iHRIS Page",
      "description" : "iHRIS Profile of the Basic resource to manage pages.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-page-display.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-page-display"
      },
      "name" : "iHRIS Page Display",
      "description" : "iHRIS Page Display details.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-page-section.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-page-section"
      },
      "name" : "iHRIS Page Section",
      "description" : "iHRIS Page Section information.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-page-task.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-page-task"
      },
      "name" : "iHRIS Page Task",
      "description" : "iHRIS Page Task details.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-parameters-local-config.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-parameters-local-config"
      },
      "name" : "iHRIS Parameters Local Config",
      "description" : "Configuration Parameters to be loaded from a local file for iHRIS.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-parameters-remote-config.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-parameters-remote-config"
      },
      "name" : "iHRIS Parameters Remote Config",
      "description" : "Configuration Parameters to be loaded from a remote file for iHRIS.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-test-dependent.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-test-dependent"
      },
      "name" : "iHRIS Practitioner Dependent Detail",
      "description" : "iHRIS Test extension for Practitioner Dependent Detail.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-test-residence.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-test-residence"
      },
      "name" : "iHRIS Practitioner Residence",
      "description" : "iHRIS Test extension for Practitioner residence.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-questionnaire.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-questionnaire"
      },
      "name" : "iHRIS Questionnaire",
      "description" : "iHRIS Profile of the Questionnaire resource for data entry and validation.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-es-report-mhero-send-message.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-es-report-mhero-send-message"
      },
      "name" : "iHRIS Relationship Example",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/iHRISRelationship"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-report.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-report"
      },
      "name" : "iHRIS Report",
      "description" : "iHRIS Profile of the Basic resource to manage reports.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-iHRISReportParameters.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/iHRISReportParameters"
      },
      "name" : "ihRIS Report parameters",
      "description" : "Lists parameters",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-resource-relationships.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-resource-relationships"
      },
      "name" : "iHRIS Resource Relationships",
      "description" : "iHRIS Resource Relationships",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-iHRISRelationship.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/iHRISRelationship"
      },
      "name" : "iHRIS Resources Relationship Profile",
      "description" : "iHRIS Resources Relationship Profile",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-role.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-role"
      },
      "name" : "iHRIS Role",
      "description" : "iHRIS Profile of the Basic resource to manage roles.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-role-primary.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-role-primary"
      },
      "name" : "iHRIS Role Primary",
      "description" : "iHRIS flag for roles to indicate a primary role for assignment to users.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-salary-grade.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-salary-grade"
      },
      "name" : "iHRIS Salary Grade",
      "description" : "Sample iHRIS ValueSet for: iHRISSalaryGrade",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-salary-grade.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-salary-grade"
      },
      "name" : "iHRIS Salary Grade",
      "description" : "Sample iHRIS CodeSystem for: iHRISSalaryGrade",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-role-self.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-role-self"
      },
      "name" : "iHRIS Self Service Role",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-role"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-task.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-task"
      },
      "name" : "iHRIS Task",
      "description" : "iHRIS Profile of the Basic resource to manage tasks.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-navigation-evaluation.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-navigation-evaluation"
      },
      "name" : "iHRIS Task To Navigate to evaluation",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-navigation-leave.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-navigation-leave"
      },
      "name" : "iHRIS Task To Navigate to Leave",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-navigation-password.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-navigation-password"
      },
      "name" : "iHRIS Task To Navigate to password",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-navigation-profile.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-navigation-profile"
      },
      "name" : "iHRIS Task To Navigate to Profile",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-auditevent-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-auditevent-resource"
      },
      "name" : "iHRIS Task To Read AuditEvent resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-basic-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-basic-resource"
      },
      "name" : "iHRIS Task To Read Basic resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-code-system.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-code-system"
      },
      "name" : "iHRIS Task To Read CodeSystem resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-document-reference.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-document-reference"
      },
      "name" : "iHRIS Task To Read DocumentReference",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-location-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-location-resource"
      },
      "name" : "iHRIS Task To Read Location resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-organization-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-organization-resource"
      },
      "name" : "iHRIS Task To Read Organization resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-person-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-person-resource"
      },
      "name" : "iHRIS Task To Read Person resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-ihris-page-practitioner.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-ihris-page-practitioner"
      },
      "name" : "iHRIS Task To Read Practitioner Page",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-practitioner-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-practitioner-resource"
      },
      "name" : "iHRIS Task To Read Practitioner resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-ihris-page-practitioner-role.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-ihris-page-practitioner-role"
      },
      "name" : "iHRIS Task To Read PractitionerRole Page",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-practitioner-role-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-practitioner-role-resource"
      },
      "name" : "iHRIS Task To Read PractitionerRole resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-questionnaire-leave.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-questionnaire-leave"
      },
      "name" : "iHRIS Task To Read Questionnaire ihris-leave",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-questionnaire-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-questionnaire-resource"
      },
      "name" : "iHRIS Task To Read Questionnaire resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-questionnaire-response-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-questionnaire-response-resource"
      },
      "name" : "iHRIS Task To Read Questionnaire Response resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-structure-definition.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-structure-definition"
      },
      "name" : "iHRIS Task To Read StructureDefinition Resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-read-value-set.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-read-value-set"
      },
      "name" : "iHRIS Task To Read Valueset Resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-auditevent-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-auditevent-resource"
      },
      "name" : "iHRIS Task To Write AuditEvent resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-basic-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-basic-resource"
      },
      "name" : "iHRIS Task To Write Basic resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-code-system.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-code-system"
      },
      "name" : "iHRIS Task To Write CodeSystem resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-document-reference.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-document-reference"
      },
      "name" : "iHRIS Task To Write DocumentReference",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-location-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-location-resource"
      },
      "name" : "iHRIS Task To Write Location resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-organization-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-organization-resource"
      },
      "name" : "iHRIS Task To Write Organization resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-person-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-person-resource"
      },
      "name" : "iHRIS Task To Write Person resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-practitioner-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-practitioner-resource"
      },
      "name" : "iHRIS Task To Write Practitioner resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-practitioner-role-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-practitioner-role-resource"
      },
      "name" : "iHRIS Task To Write PractitionerRole resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-questionnaire-leave.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-questionnaire-leave"
      },
      "name" : "iHRIS Task To Write Questionnaire ihris-leave",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-questionnaire-change-password.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-questionnaire-change-password"
      },
      "name" : "iHRIS Task To Write Questionnaire ihris-password",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-questionnaire-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-questionnaire-resource"
      },
      "name" : "iHRIS Task To Write Questionnaire resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-questionnaire-response-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-questionnaire-response-resource"
      },
      "name" : "iHRIS Task To Write Questionnaire Response resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-structure-definition.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-structure-definition"
      },
      "name" : "iHRIS Task To Write StructureDefinition Resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-value-set.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-value-set"
      },
      "name" : "iHRIS Task To Write Valueset Resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-write-valueset-resource.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-write-valueset-resource"
      },
      "name" : "iHRIS Task To Write Valueset Resource",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-task-all-permissions-to-everything.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-task-all-permissions-to-everything"
      },
      "name" : "iHRIS Task With All Permissions To Everything",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-task"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-page-task.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-page-task"
      },
      "name" : "iHRIS Tasks",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-page"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ihris-test-codesystem.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ihris-test-codesystem"
      },
      "name" : "iHRIS Test CodeSystem",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-page-test-codesystem.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-page-test-codesystem"
      },
      "name" : "iHRIS Test CodeSystem Page",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-page"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-page-test-practitioner.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-page-test-practitioner"
      },
      "name" : "iHRIS Test Practitioner Page",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-page"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-test-practitioner-role.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-test-practitioner-role"
      },
      "name" : "iHRIS Test Practitioner Role",
      "description" : "iHRIS Test profile of Practitioner Role.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Questionnaire-ihris-test.html"
      }],
      "reference" : {
        "reference" : "Questionnaire/ihris-test"
      },
      "name" : "iHRIS Test Questionnaire",
      "description" : "iHRIS Test initial data entry questionnaire.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-categories.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-categories"
      },
      "name" : "iHRIS Visualization Categories",
      "description" : "iHRIS visualization categories",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-dataset.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-dataset"
      },
      "name" : "iHRIS Visualization Dataset",
      "description" : "iHRIS visualization dataset",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-filters.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-filters"
      },
      "name" : "iHRIS Visualization Filters",
      "description" : "iHRIS visualization filters",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-permissions.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-permissions"
      },
      "name" : "iHRIS Visualization Permissions",
      "description" : "iHRIS Visualization Permissions",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-series.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-series"
      },
      "name" : "iHRIS Visualization Series",
      "description" : "iHRIS visualization series",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-visualization-settings.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-visualization-settings"
      },
      "name" : "iHRIS Visualization Settings",
      "description" : "iHRIS visualization settings for the data visualizer",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Parameters"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Parameters-ihris-dashboard.html"
      }],
      "reference" : {
        "reference" : "Parameters/ihris-dashboard"
      },
      "name" : "ihris-dashboard",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-parameters-remote-config"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-es-report-staff-directorate.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-es-report-staff-directorate"
      },
      "name" : "ihris-es-report-staff-directorate",
      "exampleBoolean" : true
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-ihris-test-practitioner.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ihris-test-practitioner"
      },
      "name" : "IhrisTestPractitioner",
      "description" : "iHRIS profile of Practitioner for tests.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-iso3166-1-2.html"
      }],
      "reference" : {
        "reference" : "ValueSet/iso3166-1-2"
      },
      "name" : "Iso 3166 Part 1: 2 Letter Codes",
      "description" : "This value set defines the ISO 3166 Part 1 2-letter codes",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-ISO3166Part1.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/ISO3166Part1"
      },
      "name" : "ISO 3166-1 Codes for the representation of names of countries and their subdivisions — Part 1: Country code",
      "description" : "ISO 3166-1 establishes codes that represent the current names of countries, dependencies, and other areas of particular geopolitical interest, on the basis of country names obtained from the United Nations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-job-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/job-search"
      },
      "name" : "job-search",
      "description" : "Search for a practitionerRole job.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-leaveperiod-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/leaveperiod-search"
      },
      "name" : "leaveperiod-search",
      "description" : "Search for a practitioner's Leave Period",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-leavetype-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/leavetype-search"
      },
      "name" : "leavetype-search",
      "description" : "Search for a practitioner's Leave Type.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-iHRISReportLink.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/iHRISReportLink"
      },
      "name" : "Links to the primary resource",
      "description" : "Links to the primary resource",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-location-physical-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/location-physical-type"
      },
      "name" : "Location type",
      "description" : "This example value set defines a set of codes that can be used to indicate the physical form of the Location.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-location-physical-type.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/location-physical-type"
      },
      "name" : "Location type",
      "description" : "This example value set defines a set of codes that can be used to indicate the physical form of the Location.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-location-related-location.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/location-related-location"
      },
      "name" : "location-related-location",
      "description" : "Search by related location for a Location resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-location-mode.html"
      }],
      "reference" : {
        "reference" : "ValueSet/location-mode"
      },
      "name" : "LocationMode",
      "description" : "Indicates whether a resource instance represents a specific location or a class of locations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-location-mode.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/location-mode"
      },
      "name" : "LocationMode",
      "description" : "Indicates whether a resource instance represents a specific location or a class of locations.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-location-status.html"
      }],
      "reference" : {
        "reference" : "ValueSet/location-status"
      },
      "name" : "LocationStatus",
      "description" : "Indicates whether the location is still in use.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-location-status.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/location-status"
      },
      "name" : "LocationStatus",
      "description" : "Indicates whether the location is still in use.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-name-use.html"
      }],
      "reference" : {
        "reference" : "ValueSet/name-use"
      },
      "name" : "NameUse",
      "description" : "The use of a human name.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-name-use.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/name-use"
      },
      "name" : "NameUse",
      "description" : "The use of a human name.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-organization-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/organization-type"
      },
      "name" : "Organization type",
      "description" : "This example value set defines a set of codes that can be used to indicate a type of organization.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-organization-type.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/organization-type"
      },
      "name" : "Organization type",
      "description" : "This example value set defines a set of codes that can be used to indicate a type of organization.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "DocumentReference"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "DocumentReference-page-home.html"
      }],
      "reference" : {
        "reference" : "DocumentReference/page-home"
      },
      "name" : "page-home",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-document"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-performanceperiod-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/performanceperiod-search"
      },
      "name" : "performanceperiod-search",
      "description" : "Search for a practitioner's Performance Period",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-position-status-search.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/position-status-search"
      },
      "name" : "position-status-search",
      "description" : "Search for a practitionerRole position status.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-c80-practice-codes.html"
      }],
      "reference" : {
        "reference" : "ValueSet/c80-practice-codes"
      },
      "name" : "Practice Setting Code Value Set",
      "description" : "This is the code representing the clinical specialty of the clinician or provider who interacted with, treated, or provided a service to/for the patient. The value set used for clinical specialty has been limited by HITSP to the value set reproduced from HITSP C80 Table 2-149 Clinical Specialty Value Set Definition.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-birthdate.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-birthdate"
      },
      "name" : "practitioner-birthdate",
      "description" : "Search by birthdate for a Practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-employeeNumber.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-employeeNumber"
      },
      "name" : "practitioner-employeeNumber",
      "description" : "Search by employee number for a practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-phone.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-phone"
      },
      "name" : "practitioner-phone",
      "description" : "Search by phone for a Practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-related-location.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-related-location"
      },
      "name" : "practitioner-related-location",
      "description" : "Search by related location for a Practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-related-practitioner.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-related-practitioner"
      },
      "name" : "practitioner-related-practitioner",
      "description" : "Search by related practitioner for a Practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitioner-renewrole.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitioner-renewrole"
      },
      "name" : "practitioner-renewrole",
      "description" : "Search by employee ID for a practitioner resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitionerrole-related-location.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitionerrole-related-location"
      },
      "name" : "practitionerrole-related-location",
      "description" : "Search by related location for a PractitionerRole resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "SearchParameter"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "SearchParameter-practitionerrole-related-practitioner.html"
      }],
      "reference" : {
        "reference" : "SearchParameter/practitionerrole-related-practitioner"
      },
      "name" : "practitionerrole-related-practitioner",
      "description" : "Search by related practitioner for a PractitionerRole resource.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-iHRISReportElement.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/iHRISReportElement"
      },
      "name" : "Resource Fields",
      "description" : "Lists fields of a resource to be displayed/cached",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Basic"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "Basic-ihris-page-role.html"
      }],
      "reference" : {
        "reference" : "Basic/ihris-page-role"
      },
      "name" : "Roles",
      "exampleCanonical" : "http://ihris.org/fhir/StructureDefinition/ihris-page"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-service-category.html"
      }],
      "reference" : {
        "reference" : "ValueSet/service-category"
      },
      "name" : "Service category",
      "description" : "This value set defines an example set of codes that can be used to classify groupings of service-types/specialties.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-service-category.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/service-category"
      },
      "name" : "Service category",
      "description" : "This value set defines an example set of codes that can be used to classify groupings of service-types/specialties.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-service-type.html"
      }],
      "reference" : {
        "reference" : "ValueSet/service-type"
      },
      "name" : "Service type",
      "description" : "This value set defines an example set of codes of service-types.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-service-type.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/service-type"
      },
      "name" : "Service type",
      "description" : "This value set defines an example set of codes of service-types.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-service-provision-conditions.html"
      }],
      "reference" : {
        "reference" : "ValueSet/service-provision-conditions"
      },
      "name" : "ServiceProvisionConditions",
      "description" : "The code(s) that detail the conditions under which the healthcare service is available/offered.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-service-provision-conditions.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/service-provision-conditions"
      },
      "name" : "ServiceProvisionConditions",
      "description" : "The code(s) that detail the conditions under which the healthcare service is available/offered.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-snomedct.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/snomedct"
      },
      "name" : "SNOMED CT (all versions)",
      "description" : "SNOMED CT is the most comprehensive and precise clinical health terminology product in the world, owned and distributed around the world by The International Health Terminology Standards Development Organisation (IHTSDO).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "StructureDefinition-task-attributes.html"
      }],
      "reference" : {
        "reference" : "StructureDefinition/task-attributes"
      },
      "name" : "Task Attributes",
      "description" : "Task attributes.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "CodeSystem-v3-RoleCode.html"
      }],
      "reference" : {
        "reference" : "CodeSystem/v3-RoleCode"
      },
      "name" : "v3 Code System RoleCode",
      "description" : " A set of codes further specifying the kind of Role; specific classification codes for further qualifying RoleClass codes.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-v3-ServiceDeliveryLocationRoleType.html"
      }],
      "reference" : {
        "reference" : "ValueSet/v3-ServiceDeliveryLocationRoleType"
      },
      "name" : "V3 Value SetServiceDeliveryLocationRoleType",
      "description" : " A role of a place that further classifies the setting (e.g., accident site, road side, work site, community location) in which services are delivered.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      },
      {
        "url" : "http://hl7.org/fhir/StructureDefinition/implementationguide-page",
        "valueUri" : "ValueSet-ihris-resource-valueset.html"
      }],
      "reference" : {
        "reference" : "ValueSet/ihris-resource-valueset"
      },
      "name" : "Value Set for iHRIS Basic Resources.",
      "exampleBoolean" : false
    }],
    "page" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
        "valueUrl" : "toc.html"
      }],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [{
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "index.html"
        }],
        "nameUrl" : "index.html",
        "title" : "Home",
        "generation" : "markdown"
      }]
    },
    "parameter" : [{
      "code" : "path-resource",
      "value" : "input/capabilities"
    },
    {
      "code" : "path-resource",
      "value" : "input/examples"
    },
    {
      "code" : "path-resource",
      "value" : "input/extensions"
    },
    {
      "code" : "path-resource",
      "value" : "input/models"
    },
    {
      "code" : "path-resource",
      "value" : "input/operations"
    },
    {
      "code" : "path-resource",
      "value" : "input/profiles"
    },
    {
      "code" : "path-resource",
      "value" : "input/resources"
    },
    {
      "code" : "path-resource",
      "value" : "input/vocabulary"
    },
    {
      "code" : "path-resource",
      "value" : "input/maps"
    },
    {
      "code" : "path-resource",
      "value" : "input/testing"
    },
    {
      "code" : "path-resource",
      "value" : "input/history"
    },
    {
      "code" : "path-resource",
      "value" : "fsh-generated/resources"
    },
    {
      "code" : "path-pages",
      "value" : "template/config"
    },
    {
      "code" : "path-pages",
      "value" : "input/images"
    },
    {
      "code" : "path-tx-cache",
      "value" : "input-cache/txcache"
    }]
  }
}

```
