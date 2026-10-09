# Country - iHRIS Implementation Guide v0.1.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Country**

## Example Bundle: Country



## Resource Content

```json
{
  "resourceType" : "Bundle",
  "id" : "Country",
  "type" : "transaction",
  "entry" : [{
    "resource" : {
      "resourceType" : "Location",
      "id" : "AD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AD</b></p><a name=\"AD\"> </a><a name=\"hcAD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Andorra</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AD"
      }],
      "status" : "active",
      "name" : "Andorra",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AE</b></p><a name=\"AE\"> </a><a name=\"hcAE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: United Arab Emirates</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AE"
      }],
      "status" : "active",
      "name" : "United Arab Emirates",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AF</b></p><a name=\"AF\"> </a><a name=\"hcAF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Afghanistan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AF"
      }],
      "status" : "active",
      "name" : "Afghanistan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AG</b></p><a name=\"AG\"> </a><a name=\"hcAG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Antigua And Barbuda</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AG"
      }],
      "status" : "active",
      "name" : "Antigua And Barbuda",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AI</b></p><a name=\"AI\"> </a><a name=\"hcAI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Anguilla</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AI"
      }],
      "status" : "active",
      "name" : "Anguilla",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AL</b></p><a name=\"AL\"> </a><a name=\"hcAL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Albania</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AL"
      }],
      "status" : "active",
      "name" : "Albania",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AM</b></p><a name=\"AM\"> </a><a name=\"hcAM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Armenia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AM"
      }],
      "status" : "active",
      "name" : "Armenia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AN</b></p><a name=\"AN\"> </a><a name=\"hcAN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Netherlands Antilles</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AN"
      }],
      "status" : "active",
      "name" : "Netherlands Antilles",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AO</b></p><a name=\"AO\"> </a><a name=\"hcAO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Angola</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AO"
      }],
      "status" : "active",
      "name" : "Angola",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AQ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AQ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AQ</b></p><a name=\"AQ\"> </a><a name=\"hcAQ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AQ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Antarctica</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AQ"
      }],
      "status" : "active",
      "name" : "Antarctica",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AQ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AR</b></p><a name=\"AR\"> </a><a name=\"hcAR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Argentina</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AR"
      }],
      "status" : "active",
      "name" : "Argentina",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AS</b></p><a name=\"AS\"> </a><a name=\"hcAS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: American Samoa</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AS"
      }],
      "status" : "active",
      "name" : "American Samoa",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AT</b></p><a name=\"AT\"> </a><a name=\"hcAT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Austria</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AT"
      }],
      "status" : "active",
      "name" : "Austria",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AU</b></p><a name=\"AU\"> </a><a name=\"hcAU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Australia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AU"
      }],
      "status" : "active",
      "name" : "Australia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AW</b></p><a name=\"AW\"> </a><a name=\"hcAW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Aruba</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AW"
      }],
      "status" : "active",
      "name" : "Aruba",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AX",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AX\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AX</b></p><a name=\"AX\"> </a><a name=\"hcAX\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AX (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Åland Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AX"
      }],
      "status" : "active",
      "name" : "Åland Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AX"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "AZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_AZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location AZ</b></p><a name=\"AZ\"> </a><a name=\"hcAZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/AZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Azerbaijan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "AZ"
      }],
      "status" : "active",
      "name" : "Azerbaijan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/AZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BA</b></p><a name=\"BA\"> </a><a name=\"hcBA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bosnia And Herzegovina</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BA"
      }],
      "status" : "active",
      "name" : "Bosnia And Herzegovina",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BB",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BB\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BB</b></p><a name=\"BB\"> </a><a name=\"hcBB\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BB (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Barbados</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BB"
      }],
      "status" : "active",
      "name" : "Barbados",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BB"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BD</b></p><a name=\"BD\"> </a><a name=\"hcBD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bangladesh</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BD"
      }],
      "status" : "active",
      "name" : "Bangladesh",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BE</b></p><a name=\"BE\"> </a><a name=\"hcBE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Belgium</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BE"
      }],
      "status" : "active",
      "name" : "Belgium",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BF</b></p><a name=\"BF\"> </a><a name=\"hcBF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Burkina Faso</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BF"
      }],
      "status" : "active",
      "name" : "Burkina Faso",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BG</b></p><a name=\"BG\"> </a><a name=\"hcBG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bulgaria</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BG"
      }],
      "status" : "active",
      "name" : "Bulgaria",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BH</b></p><a name=\"BH\"> </a><a name=\"hcBH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bahrain</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BH"
      }],
      "status" : "active",
      "name" : "Bahrain",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BI</b></p><a name=\"BI\"> </a><a name=\"hcBI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Burundi</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BI"
      }],
      "status" : "active",
      "name" : "Burundi",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BJ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BJ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BJ</b></p><a name=\"BJ\"> </a><a name=\"hcBJ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BJ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Benin</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BJ"
      }],
      "status" : "active",
      "name" : "Benin",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BJ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BL</b></p><a name=\"BL\"> </a><a name=\"hcBL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint BarthÉlemy</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BL"
      }],
      "status" : "active",
      "name" : "Saint BarthÉlemy",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BM</b></p><a name=\"BM\"> </a><a name=\"hcBM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bermuda</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BM"
      }],
      "status" : "active",
      "name" : "Bermuda",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BN</b></p><a name=\"BN\"> </a><a name=\"hcBN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Brunei Darussalam</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BN"
      }],
      "status" : "active",
      "name" : "Brunei Darussalam",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BO</b></p><a name=\"BO\"> </a><a name=\"hcBO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bolivia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BO"
      }],
      "status" : "active",
      "name" : "Bolivia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BR</b></p><a name=\"BR\"> </a><a name=\"hcBR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Brazil</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BR"
      }],
      "status" : "active",
      "name" : "Brazil",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BS</b></p><a name=\"BS\"> </a><a name=\"hcBS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bahamas</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BS"
      }],
      "status" : "active",
      "name" : "Bahamas",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BT</b></p><a name=\"BT\"> </a><a name=\"hcBT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bhutan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BT"
      }],
      "status" : "active",
      "name" : "Bhutan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BV</b></p><a name=\"BV\"> </a><a name=\"hcBV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Bouvet Island</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BV"
      }],
      "status" : "active",
      "name" : "Bouvet Island",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BW</b></p><a name=\"BW\"> </a><a name=\"hcBW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Botswana</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BW"
      }],
      "status" : "active",
      "name" : "Botswana",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BY</b></p><a name=\"BY\"> </a><a name=\"hcBY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Belarus</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BY"
      }],
      "status" : "active",
      "name" : "Belarus",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "BZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_BZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location BZ</b></p><a name=\"BZ\"> </a><a name=\"hcBZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/BZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Belize</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "BZ"
      }],
      "status" : "active",
      "name" : "Belize",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/BZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CA</b></p><a name=\"CA\"> </a><a name=\"hcCA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Canada</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CA"
      }],
      "status" : "active",
      "name" : "Canada",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CC</b></p><a name=\"CC\"> </a><a name=\"hcCC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cocos (keeling) Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CC"
      }],
      "status" : "active",
      "name" : "Cocos (keeling) Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CD</b></p><a name=\"CD\"> </a><a name=\"hcCD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Congo, The Democratic Republic Of The</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CD"
      }],
      "status" : "active",
      "name" : "Congo, The Democratic Republic Of The",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CF</b></p><a name=\"CF\"> </a><a name=\"hcCF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Central African Republic</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CF"
      }],
      "status" : "active",
      "name" : "Central African Republic",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CG</b></p><a name=\"CG\"> </a><a name=\"hcCG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Congo</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CG"
      }],
      "status" : "active",
      "name" : "Congo",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CH</b></p><a name=\"CH\"> </a><a name=\"hcCH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Switzerland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CH"
      }],
      "status" : "active",
      "name" : "Switzerland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CI</b></p><a name=\"CI\"> </a><a name=\"hcCI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: CÔte D'ivoire</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CI"
      }],
      "status" : "active",
      "name" : "CÔte D'ivoire",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CK</b></p><a name=\"CK\"> </a><a name=\"hcCK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cook Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CK"
      }],
      "status" : "active",
      "name" : "Cook Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CL</b></p><a name=\"CL\"> </a><a name=\"hcCL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Chile</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CL"
      }],
      "status" : "active",
      "name" : "Chile",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CM</b></p><a name=\"CM\"> </a><a name=\"hcCM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cameroon</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CM"
      }],
      "status" : "active",
      "name" : "Cameroon",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CN</b></p><a name=\"CN\"> </a><a name=\"hcCN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: China</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CN"
      }],
      "status" : "active",
      "name" : "China",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CO</b></p><a name=\"CO\"> </a><a name=\"hcCO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Colombia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CO"
      }],
      "status" : "active",
      "name" : "Colombia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CR</b></p><a name=\"CR\"> </a><a name=\"hcCR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Costa Rica</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CR"
      }],
      "status" : "active",
      "name" : "Costa Rica",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CU</b></p><a name=\"CU\"> </a><a name=\"hcCU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cuba</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CU"
      }],
      "status" : "active",
      "name" : "Cuba",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CV</b></p><a name=\"CV\"> </a><a name=\"hcCV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cape Verde</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CV"
      }],
      "status" : "active",
      "name" : "Cape Verde",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CX",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CX\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CX</b></p><a name=\"CX\"> </a><a name=\"hcCX\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CX (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Christmas Island</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CX"
      }],
      "status" : "active",
      "name" : "Christmas Island",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CX"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CY</b></p><a name=\"CY\"> </a><a name=\"hcCY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cyprus</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CY"
      }],
      "status" : "active",
      "name" : "Cyprus",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "CZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_CZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location CZ</b></p><a name=\"CZ\"> </a><a name=\"hcCZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/CZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Czech Republic</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "CZ"
      }],
      "status" : "active",
      "name" : "Czech Republic",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/CZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DE</b></p><a name=\"DE\"> </a><a name=\"hcDE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Germany</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DE"
      }],
      "status" : "active",
      "name" : "Germany",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DJ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DJ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DJ</b></p><a name=\"DJ\"> </a><a name=\"hcDJ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DJ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Djibouti</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DJ"
      }],
      "status" : "active",
      "name" : "Djibouti",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DJ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DK</b></p><a name=\"DK\"> </a><a name=\"hcDK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Denmark</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DK"
      }],
      "status" : "active",
      "name" : "Denmark",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DM</b></p><a name=\"DM\"> </a><a name=\"hcDM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Dominica</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DM"
      }],
      "status" : "active",
      "name" : "Dominica",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DO</b></p><a name=\"DO\"> </a><a name=\"hcDO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Dominican Republic</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DO"
      }],
      "status" : "active",
      "name" : "Dominican Republic",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "DZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_DZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location DZ</b></p><a name=\"DZ\"> </a><a name=\"hcDZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/DZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Algeria</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "DZ"
      }],
      "status" : "active",
      "name" : "Algeria",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/DZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "EC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_EC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location EC</b></p><a name=\"EC\"> </a><a name=\"hcEC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/EC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Ecuador</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "EC"
      }],
      "status" : "active",
      "name" : "Ecuador",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/EC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "EE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_EE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location EE</b></p><a name=\"EE\"> </a><a name=\"hcEE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/EE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Estonia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "EE"
      }],
      "status" : "active",
      "name" : "Estonia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/EE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "EG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_EG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location EG</b></p><a name=\"EG\"> </a><a name=\"hcEG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/EG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Egypt</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "EG"
      }],
      "status" : "active",
      "name" : "Egypt",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/EG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "EH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_EH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location EH</b></p><a name=\"EH\"> </a><a name=\"hcEH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/EH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Western Sahara</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "EH"
      }],
      "status" : "active",
      "name" : "Western Sahara",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/EH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ER",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ER\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ER</b></p><a name=\"ER\"> </a><a name=\"hcER\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ER (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Eritrea</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ER"
      }],
      "status" : "active",
      "name" : "Eritrea",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ER"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ES",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ES\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ES</b></p><a name=\"ES\"> </a><a name=\"hcES\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ES (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Spain</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ES"
      }],
      "status" : "active",
      "name" : "Spain",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ES"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ET",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ET\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ET</b></p><a name=\"ET\"> </a><a name=\"hcET\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ET (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Ethiopia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ET"
      }],
      "status" : "active",
      "name" : "Ethiopia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ET"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FI</b></p><a name=\"FI\"> </a><a name=\"hcFI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Finland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FI"
      }],
      "status" : "active",
      "name" : "Finland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FJ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FJ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FJ</b></p><a name=\"FJ\"> </a><a name=\"hcFJ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FJ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Fiji</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FJ"
      }],
      "status" : "active",
      "name" : "Fiji",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FJ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FK</b></p><a name=\"FK\"> </a><a name=\"hcFK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Falkland Islands (malvinas)</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FK"
      }],
      "status" : "active",
      "name" : "Falkland Islands (malvinas)",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FM</b></p><a name=\"FM\"> </a><a name=\"hcFM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Micronesia, Federated States Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FM"
      }],
      "status" : "active",
      "name" : "Micronesia, Federated States Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FO</b></p><a name=\"FO\"> </a><a name=\"hcFO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Faroe Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FO"
      }],
      "status" : "active",
      "name" : "Faroe Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "FR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_FR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location FR</b></p><a name=\"FR\"> </a><a name=\"hcFR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/FR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: France</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "FR"
      }],
      "status" : "active",
      "name" : "France",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/FR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GA</b></p><a name=\"GA\"> </a><a name=\"hcGA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Gabon</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GA"
      }],
      "status" : "active",
      "name" : "Gabon",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GB",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GB\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GB</b></p><a name=\"GB\"> </a><a name=\"hcGB\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GB (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: United Kingdom</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GB"
      }],
      "status" : "active",
      "name" : "United Kingdom",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GB"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GD</b></p><a name=\"GD\"> </a><a name=\"hcGD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Grenada</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GD"
      }],
      "status" : "active",
      "name" : "Grenada",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GE</b></p><a name=\"GE\"> </a><a name=\"hcGE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Georgia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GE"
      }],
      "status" : "active",
      "name" : "Georgia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GF</b></p><a name=\"GF\"> </a><a name=\"hcGF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: French Guiana</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GF"
      }],
      "status" : "active",
      "name" : "French Guiana",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GG</b></p><a name=\"GG\"> </a><a name=\"hcGG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guernsey</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GG"
      }],
      "status" : "active",
      "name" : "Guernsey",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GH</b></p><a name=\"GH\"> </a><a name=\"hcGH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Ghana</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GH"
      }],
      "status" : "active",
      "name" : "Ghana",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GI</b></p><a name=\"GI\"> </a><a name=\"hcGI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Gibraltar</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GI"
      }],
      "status" : "active",
      "name" : "Gibraltar",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GL</b></p><a name=\"GL\"> </a><a name=\"hcGL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Greenland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GL"
      }],
      "status" : "active",
      "name" : "Greenland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GM</b></p><a name=\"GM\"> </a><a name=\"hcGM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Gambia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GM"
      }],
      "status" : "active",
      "name" : "Gambia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GN</b></p><a name=\"GN\"> </a><a name=\"hcGN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guinea</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GN"
      }],
      "status" : "active",
      "name" : "Guinea",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GP",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GP\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GP</b></p><a name=\"GP\"> </a><a name=\"hcGP\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GP (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guadeloupe</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GP"
      }],
      "status" : "active",
      "name" : "Guadeloupe",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GP"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GQ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GQ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GQ</b></p><a name=\"GQ\"> </a><a name=\"hcGQ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GQ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Equatorial Guinea</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GQ"
      }],
      "status" : "active",
      "name" : "Equatorial Guinea",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GQ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GR</b></p><a name=\"GR\"> </a><a name=\"hcGR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Greece</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GR"
      }],
      "status" : "active",
      "name" : "Greece",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GS</b></p><a name=\"GS\"> </a><a name=\"hcGS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: South Georgia And The South Sandwich Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GS"
      }],
      "status" : "active",
      "name" : "South Georgia And The South Sandwich Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GT</b></p><a name=\"GT\"> </a><a name=\"hcGT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guatemala</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GT"
      }],
      "status" : "active",
      "name" : "Guatemala",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GU</b></p><a name=\"GU\"> </a><a name=\"hcGU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guam</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GU"
      }],
      "status" : "active",
      "name" : "Guam",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GW</b></p><a name=\"GW\"> </a><a name=\"hcGW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guinea-bissau</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GW"
      }],
      "status" : "active",
      "name" : "Guinea-bissau",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "GY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_GY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location GY</b></p><a name=\"GY\"> </a><a name=\"hcGY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/GY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Guyana</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "GY"
      }],
      "status" : "active",
      "name" : "Guyana",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/GY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HK</b></p><a name=\"HK\"> </a><a name=\"hcHK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Hong Kong</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HK"
      }],
      "status" : "active",
      "name" : "Hong Kong",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HM</b></p><a name=\"HM\"> </a><a name=\"hcHM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Heard Island And Mcdonald Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HM"
      }],
      "status" : "active",
      "name" : "Heard Island And Mcdonald Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HN</b></p><a name=\"HN\"> </a><a name=\"hcHN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Honduras</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HN"
      }],
      "status" : "active",
      "name" : "Honduras",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HR</b></p><a name=\"HR\"> </a><a name=\"hcHR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Croatia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HR"
      }],
      "status" : "active",
      "name" : "Croatia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HT</b></p><a name=\"HT\"> </a><a name=\"hcHT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Haiti</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HT"
      }],
      "status" : "active",
      "name" : "Haiti",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "HU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_HU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location HU</b></p><a name=\"HU\"> </a><a name=\"hcHU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/HU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Hungary</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "HU"
      }],
      "status" : "active",
      "name" : "Hungary",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/HU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ID",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ID\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ID</b></p><a name=\"ID\"> </a><a name=\"hcID\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ID (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Indonesia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ID"
      }],
      "status" : "active",
      "name" : "Indonesia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ID"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IE</b></p><a name=\"IE\"> </a><a name=\"hcIE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Ireland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IE"
      }],
      "status" : "active",
      "name" : "Ireland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IL</b></p><a name=\"IL\"> </a><a name=\"hcIL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Israel</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IL"
      }],
      "status" : "active",
      "name" : "Israel",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IM</b></p><a name=\"IM\"> </a><a name=\"hcIM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Isle Of Man</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IM"
      }],
      "status" : "active",
      "name" : "Isle Of Man",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IN</b></p><a name=\"IN\"> </a><a name=\"hcIN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: India</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IN"
      }],
      "status" : "active",
      "name" : "India",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IO</b></p><a name=\"IO\"> </a><a name=\"hcIO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: British Indian Ocean Territory</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IO"
      }],
      "status" : "active",
      "name" : "British Indian Ocean Territory",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IQ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IQ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IQ</b></p><a name=\"IQ\"> </a><a name=\"hcIQ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IQ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Iraq</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IQ"
      }],
      "status" : "active",
      "name" : "Iraq",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IQ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IR</b></p><a name=\"IR\"> </a><a name=\"hcIR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Iran, Islamic Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IR"
      }],
      "status" : "active",
      "name" : "Iran, Islamic Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IS</b></p><a name=\"IS\"> </a><a name=\"hcIS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Iceland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IS"
      }],
      "status" : "active",
      "name" : "Iceland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "IT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_IT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location IT</b></p><a name=\"IT\"> </a><a name=\"hcIT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/IT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Italy</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "IT"
      }],
      "status" : "active",
      "name" : "Italy",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/IT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "JE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_JE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location JE</b></p><a name=\"JE\"> </a><a name=\"hcJE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/JE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Jersey</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "JE"
      }],
      "status" : "active",
      "name" : "Jersey",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/JE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "JM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_JM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location JM</b></p><a name=\"JM\"> </a><a name=\"hcJM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/JM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Jamaica</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "JM"
      }],
      "status" : "active",
      "name" : "Jamaica",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/JM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "JO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_JO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location JO</b></p><a name=\"JO\"> </a><a name=\"hcJO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/JO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Jordan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "JO"
      }],
      "status" : "active",
      "name" : "Jordan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/JO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "JP",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_JP\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location JP</b></p><a name=\"JP\"> </a><a name=\"hcJP\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/JP (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Japan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "JP"
      }],
      "status" : "active",
      "name" : "Japan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/JP"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KE</b></p><a name=\"KE\"> </a><a name=\"hcKE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Kenya</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KE"
      }],
      "status" : "active",
      "name" : "Kenya",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KG</b></p><a name=\"KG\"> </a><a name=\"hcKG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Kyrgyzstan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KG"
      }],
      "status" : "active",
      "name" : "Kyrgyzstan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KH</b></p><a name=\"KH\"> </a><a name=\"hcKH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cambodia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KH"
      }],
      "status" : "active",
      "name" : "Cambodia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KI</b></p><a name=\"KI\"> </a><a name=\"hcKI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Kiribati</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KI"
      }],
      "status" : "active",
      "name" : "Kiribati",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KM</b></p><a name=\"KM\"> </a><a name=\"hcKM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Comoros</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KM"
      }],
      "status" : "active",
      "name" : "Comoros",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KN</b></p><a name=\"KN\"> </a><a name=\"hcKN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Kitts And Nevis</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KN"
      }],
      "status" : "active",
      "name" : "Saint Kitts And Nevis",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KP",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KP\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KP</b></p><a name=\"KP\"> </a><a name=\"hcKP\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KP (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Korea, Democratic People's Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KP"
      }],
      "status" : "active",
      "name" : "Korea, Democratic People's Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KP"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KR</b></p><a name=\"KR\"> </a><a name=\"hcKR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Korea, Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KR"
      }],
      "status" : "active",
      "name" : "Korea, Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KW</b></p><a name=\"KW\"> </a><a name=\"hcKW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Kuwait</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KW"
      }],
      "status" : "active",
      "name" : "Kuwait",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KY</b></p><a name=\"KY\"> </a><a name=\"hcKY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Cayman Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KY"
      }],
      "status" : "active",
      "name" : "Cayman Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "KZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_KZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location KZ</b></p><a name=\"KZ\"> </a><a name=\"hcKZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/KZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Kazakhstan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "KZ"
      }],
      "status" : "active",
      "name" : "Kazakhstan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/KZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LA</b></p><a name=\"LA\"> </a><a name=\"hcLA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Lao People's Democratic Republic</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LA"
      }],
      "status" : "active",
      "name" : "Lao People's Democratic Republic",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LB",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LB\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LB</b></p><a name=\"LB\"> </a><a name=\"hcLB\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LB (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Lebanon</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LB"
      }],
      "status" : "active",
      "name" : "Lebanon",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LB"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LC</b></p><a name=\"LC\"> </a><a name=\"hcLC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Lucia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LC"
      }],
      "status" : "active",
      "name" : "Saint Lucia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LI</b></p><a name=\"LI\"> </a><a name=\"hcLI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Liechtenstein</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LI"
      }],
      "status" : "active",
      "name" : "Liechtenstein",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LK</b></p><a name=\"LK\"> </a><a name=\"hcLK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Sri Lanka</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LK"
      }],
      "status" : "active",
      "name" : "Sri Lanka",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LR</b></p><a name=\"LR\"> </a><a name=\"hcLR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Liberia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LR"
      }],
      "status" : "active",
      "name" : "Liberia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LS</b></p><a name=\"LS\"> </a><a name=\"hcLS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Lesotho</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LS"
      }],
      "status" : "active",
      "name" : "Lesotho",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LT</b></p><a name=\"LT\"> </a><a name=\"hcLT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Lithuania</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LT"
      }],
      "status" : "active",
      "name" : "Lithuania",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LU</b></p><a name=\"LU\"> </a><a name=\"hcLU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Luxembourg</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LU"
      }],
      "status" : "active",
      "name" : "Luxembourg",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LV</b></p><a name=\"LV\"> </a><a name=\"hcLV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Latvia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LV"
      }],
      "status" : "active",
      "name" : "Latvia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "LY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_LY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location LY</b></p><a name=\"LY\"> </a><a name=\"hcLY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/LY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Libyan Arab Jamahiriya</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "LY"
      }],
      "status" : "active",
      "name" : "Libyan Arab Jamahiriya",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/LY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MA</b></p><a name=\"MA\"> </a><a name=\"hcMA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Morocco</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MA"
      }],
      "status" : "active",
      "name" : "Morocco",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MC</b></p><a name=\"MC\"> </a><a name=\"hcMC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Monaco</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MC"
      }],
      "status" : "active",
      "name" : "Monaco",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MD</b></p><a name=\"MD\"> </a><a name=\"hcMD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Moldova, Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MD"
      }],
      "status" : "active",
      "name" : "Moldova, Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ME",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ME\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ME</b></p><a name=\"ME\"> </a><a name=\"hcME\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ME (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Montenegro</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ME"
      }],
      "status" : "active",
      "name" : "Montenegro",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ME"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MF</b></p><a name=\"MF\"> </a><a name=\"hcMF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Martin</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MF"
      }],
      "status" : "active",
      "name" : "Saint Martin",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MG</b></p><a name=\"MG\"> </a><a name=\"hcMG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Madagascar</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MG"
      }],
      "status" : "active",
      "name" : "Madagascar",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MH</b></p><a name=\"MH\"> </a><a name=\"hcMH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Marshall Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MH"
      }],
      "status" : "active",
      "name" : "Marshall Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MK</b></p><a name=\"MK\"> </a><a name=\"hcMK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Macedonia, The Former Yugoslav Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MK"
      }],
      "status" : "active",
      "name" : "Macedonia, The Former Yugoslav Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ML",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ML\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ML</b></p><a name=\"ML\"> </a><a name=\"hcML\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ML (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mali</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ML"
      }],
      "status" : "active",
      "name" : "Mali",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ML"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MM</b></p><a name=\"MM\"> </a><a name=\"hcMM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Myanmar</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MM"
      }],
      "status" : "active",
      "name" : "Myanmar",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MN</b></p><a name=\"MN\"> </a><a name=\"hcMN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mongolia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MN"
      }],
      "status" : "active",
      "name" : "Mongolia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MO</b></p><a name=\"MO\"> </a><a name=\"hcMO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Macao</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MO"
      }],
      "status" : "active",
      "name" : "Macao",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MP",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MP\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MP</b></p><a name=\"MP\"> </a><a name=\"hcMP\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MP (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Northern Mariana Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MP"
      }],
      "status" : "active",
      "name" : "Northern Mariana Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MP"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MQ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MQ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MQ</b></p><a name=\"MQ\"> </a><a name=\"hcMQ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MQ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Martinique</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MQ"
      }],
      "status" : "active",
      "name" : "Martinique",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MQ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MR</b></p><a name=\"MR\"> </a><a name=\"hcMR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mauritania</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MR"
      }],
      "status" : "active",
      "name" : "Mauritania",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MS</b></p><a name=\"MS\"> </a><a name=\"hcMS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Montserrat</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MS"
      }],
      "status" : "active",
      "name" : "Montserrat",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MT</b></p><a name=\"MT\"> </a><a name=\"hcMT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Malta</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MT"
      }],
      "status" : "active",
      "name" : "Malta",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MU</b></p><a name=\"MU\"> </a><a name=\"hcMU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mauritius</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MU"
      }],
      "status" : "active",
      "name" : "Mauritius",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MV</b></p><a name=\"MV\"> </a><a name=\"hcMV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Maldives</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MV"
      }],
      "status" : "active",
      "name" : "Maldives",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MW</b></p><a name=\"MW\"> </a><a name=\"hcMW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Malawi</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MW"
      }],
      "status" : "active",
      "name" : "Malawi",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MX",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MX\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MX</b></p><a name=\"MX\"> </a><a name=\"hcMX\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MX (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mexico</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MX"
      }],
      "status" : "active",
      "name" : "Mexico",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MX"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MY</b></p><a name=\"MY\"> </a><a name=\"hcMY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Malaysia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MY"
      }],
      "status" : "active",
      "name" : "Malaysia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "MZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_MZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location MZ</b></p><a name=\"MZ\"> </a><a name=\"hcMZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/MZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mozambique</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "MZ"
      }],
      "status" : "active",
      "name" : "Mozambique",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/MZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NA</b></p><a name=\"NA\"> </a><a name=\"hcNA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Namibia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NA"
      }],
      "status" : "active",
      "name" : "Namibia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NC</b></p><a name=\"NC\"> </a><a name=\"hcNC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: New Caledonia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NC"
      }],
      "status" : "active",
      "name" : "New Caledonia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NE</b></p><a name=\"NE\"> </a><a name=\"hcNE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Niger</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NE"
      }],
      "status" : "active",
      "name" : "Niger",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NF</b></p><a name=\"NF\"> </a><a name=\"hcNF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Norfolk Island</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NF"
      }],
      "status" : "active",
      "name" : "Norfolk Island",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NG</b></p><a name=\"NG\"> </a><a name=\"hcNG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Nigeria</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NG"
      }],
      "status" : "active",
      "name" : "Nigeria",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NI</b></p><a name=\"NI\"> </a><a name=\"hcNI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Nicaragua</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NI"
      }],
      "status" : "active",
      "name" : "Nicaragua",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NL</b></p><a name=\"NL\"> </a><a name=\"hcNL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Netherlands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NL"
      }],
      "status" : "active",
      "name" : "Netherlands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NO</b></p><a name=\"NO\"> </a><a name=\"hcNO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Norway</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NO"
      }],
      "status" : "active",
      "name" : "Norway",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NP",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NP\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NP</b></p><a name=\"NP\"> </a><a name=\"hcNP\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NP (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Nepal</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NP"
      }],
      "status" : "active",
      "name" : "Nepal",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NP"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NR</b></p><a name=\"NR\"> </a><a name=\"hcNR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Nauru</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NR"
      }],
      "status" : "active",
      "name" : "Nauru",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NU</b></p><a name=\"NU\"> </a><a name=\"hcNU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Niue</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NU"
      }],
      "status" : "active",
      "name" : "Niue",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "NZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_NZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location NZ</b></p><a name=\"NZ\"> </a><a name=\"hcNZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/NZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: New Zealand</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "NZ"
      }],
      "status" : "active",
      "name" : "New Zealand",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/NZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "OM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_OM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location OM</b></p><a name=\"OM\"> </a><a name=\"hcOM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/OM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Oman</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "OM"
      }],
      "status" : "active",
      "name" : "Oman",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/OM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PA</b></p><a name=\"PA\"> </a><a name=\"hcPA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Panama</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PA"
      }],
      "status" : "active",
      "name" : "Panama",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PE</b></p><a name=\"PE\"> </a><a name=\"hcPE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Peru</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PE"
      }],
      "status" : "active",
      "name" : "Peru",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PF</b></p><a name=\"PF\"> </a><a name=\"hcPF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: French Polynesia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PF"
      }],
      "status" : "active",
      "name" : "French Polynesia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PG</b></p><a name=\"PG\"> </a><a name=\"hcPG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Papua New Guinea</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PG"
      }],
      "status" : "active",
      "name" : "Papua New Guinea",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PH</b></p><a name=\"PH\"> </a><a name=\"hcPH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Philippines</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PH"
      }],
      "status" : "active",
      "name" : "Philippines",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PK</b></p><a name=\"PK\"> </a><a name=\"hcPK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Pakistan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PK"
      }],
      "status" : "active",
      "name" : "Pakistan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PL</b></p><a name=\"PL\"> </a><a name=\"hcPL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Poland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PL"
      }],
      "status" : "active",
      "name" : "Poland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PM</b></p><a name=\"PM\"> </a><a name=\"hcPM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Pierre And Miquelon</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PM"
      }],
      "status" : "active",
      "name" : "Saint Pierre And Miquelon",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PN</b></p><a name=\"PN\"> </a><a name=\"hcPN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Pitcairn</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PN"
      }],
      "status" : "active",
      "name" : "Pitcairn",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PR</b></p><a name=\"PR\"> </a><a name=\"hcPR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Puerto Rico</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PR"
      }],
      "status" : "active",
      "name" : "Puerto Rico",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PS</b></p><a name=\"PS\"> </a><a name=\"hcPS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Palestinian Territory, Occupied</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PS"
      }],
      "status" : "active",
      "name" : "Palestinian Territory, Occupied",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PT</b></p><a name=\"PT\"> </a><a name=\"hcPT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Portugal</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PT"
      }],
      "status" : "active",
      "name" : "Portugal",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PW</b></p><a name=\"PW\"> </a><a name=\"hcPW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Palau</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PW"
      }],
      "status" : "active",
      "name" : "Palau",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "PY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_PY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location PY</b></p><a name=\"PY\"> </a><a name=\"hcPY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/PY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Paraguay</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "PY"
      }],
      "status" : "active",
      "name" : "Paraguay",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/PY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "QA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_QA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location QA</b></p><a name=\"QA\"> </a><a name=\"hcQA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/QA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Qatar</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "QA"
      }],
      "status" : "active",
      "name" : "Qatar",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/QA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "RE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_RE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location RE</b></p><a name=\"RE\"> </a><a name=\"hcRE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/RE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: RÉunion</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "RE"
      }],
      "status" : "active",
      "name" : "RÉunion",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/RE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "RO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_RO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location RO</b></p><a name=\"RO\"> </a><a name=\"hcRO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/RO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Romania</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "RO"
      }],
      "status" : "active",
      "name" : "Romania",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/RO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "RS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_RS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location RS</b></p><a name=\"RS\"> </a><a name=\"hcRS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/RS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Serbia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "RS"
      }],
      "status" : "active",
      "name" : "Serbia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/RS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "RU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_RU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location RU</b></p><a name=\"RU\"> </a><a name=\"hcRU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/RU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Russian Federation</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "RU"
      }],
      "status" : "active",
      "name" : "Russian Federation",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/RU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "RW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_RW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location RW</b></p><a name=\"RW\"> </a><a name=\"hcRW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/RW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Rwanda</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "RW"
      }],
      "status" : "active",
      "name" : "Rwanda",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/RW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SA</b></p><a name=\"SA\"> </a><a name=\"hcSA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saudi Arabia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SA"
      }],
      "status" : "active",
      "name" : "Saudi Arabia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SB",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SB\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SB</b></p><a name=\"SB\"> </a><a name=\"hcSB\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SB (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Solomon Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SB"
      }],
      "status" : "active",
      "name" : "Solomon Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SB"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SC</b></p><a name=\"SC\"> </a><a name=\"hcSC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Seychelles</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SC"
      }],
      "status" : "active",
      "name" : "Seychelles",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SD</b></p><a name=\"SD\"> </a><a name=\"hcSD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Sudan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SD"
      }],
      "status" : "active",
      "name" : "Sudan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SDN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SDN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SDN</b></p><a name=\"SDN\"> </a><a name=\"hcSDN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SDN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Sudan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SDN"
      }],
      "status" : "active",
      "name" : "Sudan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SDN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SE</b></p><a name=\"SE\"> </a><a name=\"hcSE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Sweden</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SE"
      }],
      "status" : "active",
      "name" : "Sweden",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SG</b></p><a name=\"SG\"> </a><a name=\"hcSG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Singapore</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SG"
      }],
      "status" : "active",
      "name" : "Singapore",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SH</b></p><a name=\"SH\"> </a><a name=\"hcSH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Helena, Ascension And Tristan Da Cunha</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SH"
      }],
      "status" : "active",
      "name" : "Saint Helena, Ascension And Tristan Da Cunha",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SI</b></p><a name=\"SI\"> </a><a name=\"hcSI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Slovenia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SI"
      }],
      "status" : "active",
      "name" : "Slovenia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SJ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SJ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SJ</b></p><a name=\"SJ\"> </a><a name=\"hcSJ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SJ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Svalbard And Jan Mayen</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SJ"
      }],
      "status" : "active",
      "name" : "Svalbard And Jan Mayen",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SJ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SK</b></p><a name=\"SK\"> </a><a name=\"hcSK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Slovakia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SK"
      }],
      "status" : "active",
      "name" : "Slovakia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SL</b></p><a name=\"SL\"> </a><a name=\"hcSL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Sierra Leone</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SL"
      }],
      "status" : "active",
      "name" : "Sierra Leone",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SM</b></p><a name=\"SM\"> </a><a name=\"hcSM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: San Marino</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SM"
      }],
      "status" : "active",
      "name" : "San Marino",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SN</b></p><a name=\"SN\"> </a><a name=\"hcSN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Senegal</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SN"
      }],
      "status" : "active",
      "name" : "Senegal",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SO</b></p><a name=\"SO\"> </a><a name=\"hcSO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Somalia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SO"
      }],
      "status" : "active",
      "name" : "Somalia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SR</b></p><a name=\"SR\"> </a><a name=\"hcSR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Suriname</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SR"
      }],
      "status" : "active",
      "name" : "Suriname",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ST",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ST\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ST</b></p><a name=\"ST\"> </a><a name=\"hcST\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ST (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: São Tome And Principe</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ST"
      }],
      "status" : "active",
      "name" : "São Tome And Principe",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ST"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SV</b></p><a name=\"SV\"> </a><a name=\"hcSV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: El Salvador</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SV"
      }],
      "status" : "active",
      "name" : "El Salvador",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SY</b></p><a name=\"SY\"> </a><a name=\"hcSY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Syrian Arab Republic</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SY"
      }],
      "status" : "active",
      "name" : "Syrian Arab Republic",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "SZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_SZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location SZ</b></p><a name=\"SZ\"> </a><a name=\"hcSZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/SZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Swaziland</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "SZ"
      }],
      "status" : "active",
      "name" : "Swaziland",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/SZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TC</b></p><a name=\"TC\"> </a><a name=\"hcTC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Turks And Caicos Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TC"
      }],
      "status" : "active",
      "name" : "Turks And Caicos Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TD",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TD\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TD</b></p><a name=\"TD\"> </a><a name=\"hcTD\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TD (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Chad</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TD"
      }],
      "status" : "active",
      "name" : "Chad",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TD"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TF</b></p><a name=\"TF\"> </a><a name=\"hcTF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Taifafeki</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TF"
      }],
      "status" : "active",
      "name" : "Taifafeki",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TG</b></p><a name=\"TG\"> </a><a name=\"hcTG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Togo</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TG"
      }],
      "status" : "active",
      "name" : "Togo",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TH",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TH\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TH</b></p><a name=\"TH\"> </a><a name=\"hcTH\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TH (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Thailand</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TH"
      }],
      "status" : "active",
      "name" : "Thailand",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TH"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TJ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TJ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TJ</b></p><a name=\"TJ\"> </a><a name=\"hcTJ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TJ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tajikistan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TJ"
      }],
      "status" : "active",
      "name" : "Tajikistan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TJ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TK",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TK\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TK</b></p><a name=\"TK\"> </a><a name=\"hcTK\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TK (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tokelau</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TK"
      }],
      "status" : "active",
      "name" : "Tokelau",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TK"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TL",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TL\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TL</b></p><a name=\"TL\"> </a><a name=\"hcTL\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TL (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Timor-leste</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TL"
      }],
      "status" : "active",
      "name" : "Timor-leste",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TL"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TM</b></p><a name=\"TM\"> </a><a name=\"hcTM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Turkmenistan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TM"
      }],
      "status" : "active",
      "name" : "Turkmenistan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TN</b></p><a name=\"TN\"> </a><a name=\"hcTN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tunisia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TN"
      }],
      "status" : "active",
      "name" : "Tunisia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TO",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TO\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TO</b></p><a name=\"TO\"> </a><a name=\"hcTO\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TO (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tonga</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TO"
      }],
      "status" : "active",
      "name" : "Tonga",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TO"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TR",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TR\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TR</b></p><a name=\"TR\"> </a><a name=\"hcTR\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TR (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Turkey</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TR"
      }],
      "status" : "active",
      "name" : "Turkey",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TR"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TT</b></p><a name=\"TT\"> </a><a name=\"hcTT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Trinidad And Tobago</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TT"
      }],
      "status" : "active",
      "name" : "Trinidad And Tobago",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TV",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TV\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TV</b></p><a name=\"TV\"> </a><a name=\"hcTV\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TV (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tuvalu</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TV"
      }],
      "status" : "active",
      "name" : "Tuvalu",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TV"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TW</b></p><a name=\"TW\"> </a><a name=\"hcTW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Taiwan, Province Of China</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TW"
      }],
      "status" : "active",
      "name" : "Taiwan, Province Of China",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TW"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "TZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_TZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location TZ</b></p><a name=\"TZ\"> </a><a name=\"hcTZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/TZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Tanzania, United Republic Of</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "TZ"
      }],
      "status" : "active",
      "name" : "Tanzania, United Republic Of",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/TZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "UA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_UA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location UA</b></p><a name=\"UA\"> </a><a name=\"hcUA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/UA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Ukraine</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "UA"
      }],
      "status" : "active",
      "name" : "Ukraine",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/UA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "UG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_UG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location UG</b></p><a name=\"UG\"> </a><a name=\"hcUG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/UG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Uganda</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "UG"
      }],
      "status" : "active",
      "name" : "Uganda",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/UG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "UM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_UM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location UM</b></p><a name=\"UM\"> </a><a name=\"hcUM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/UM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: United States Minor Outlying Islands</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "UM"
      }],
      "status" : "active",
      "name" : "United States Minor Outlying Islands",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/UM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "US",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_US\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location US</b></p><a name=\"US\"> </a><a name=\"hcUS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/US (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: United States</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "US"
      }],
      "status" : "active",
      "name" : "United States",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/US"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "UY",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_UY\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location UY</b></p><a name=\"UY\"> </a><a name=\"hcUY\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/UY (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Uruguay</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "UY"
      }],
      "status" : "active",
      "name" : "Uruguay",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/UY"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "UZ",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_UZ\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location UZ</b></p><a name=\"UZ\"> </a><a name=\"hcUZ\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/UZ (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Uzbekistan</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "UZ"
      }],
      "status" : "active",
      "name" : "Uzbekistan",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/UZ"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VA</b></p><a name=\"VA\"> </a><a name=\"hcVA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Holy See (vatican City State)</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VA"
      }],
      "status" : "active",
      "name" : "Holy See (vatican City State)",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VC",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VC\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VC</b></p><a name=\"VC\"> </a><a name=\"hcVC\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VC (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Saint Vincent And The Grenadines</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VC"
      }],
      "status" : "active",
      "name" : "Saint Vincent And The Grenadines",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VC"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VE</b></p><a name=\"VE\"> </a><a name=\"hcVE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Venezuela</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VE"
      }],
      "status" : "active",
      "name" : "Venezuela",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VG",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VG\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VG</b></p><a name=\"VG\"> </a><a name=\"hcVG\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VG (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Virgin Islands, British</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VG"
      }],
      "status" : "active",
      "name" : "Virgin Islands, British",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VG"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VI",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VI\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VI</b></p><a name=\"VI\"> </a><a name=\"hcVI\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VI (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Virgin Islands, U.s.</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VI"
      }],
      "status" : "active",
      "name" : "Virgin Islands, U.s.",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VI"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VN",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VN\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VN</b></p><a name=\"VN\"> </a><a name=\"hcVN\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VN (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Viet Nam</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VN"
      }],
      "status" : "active",
      "name" : "Viet Nam",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VN"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "VU",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_VU\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location VU</b></p><a name=\"VU\"> </a><a name=\"hcVU\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/VU (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Vanuatu</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "VU"
      }],
      "status" : "active",
      "name" : "Vanuatu",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/VU"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "WF",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_WF\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location WF</b></p><a name=\"WF\"> </a><a name=\"hcWF\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/WF (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Wallis And Futuna</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "WF"
      }],
      "status" : "active",
      "name" : "Wallis And Futuna",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/WF"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "WS",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_WS\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location WS</b></p><a name=\"WS\"> </a><a name=\"hcWS\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/WS (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Samoa</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "WS"
      }],
      "status" : "active",
      "name" : "Samoa",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/WS"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "YE",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_YE\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location YE</b></p><a name=\"YE\"> </a><a name=\"hcYE\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/YE (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Yemen</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "YE"
      }],
      "status" : "active",
      "name" : "Yemen",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/YE"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "YT",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_YT\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location YT</b></p><a name=\"YT\"> </a><a name=\"hcYT\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/YT (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Mayotte</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "YT"
      }],
      "status" : "active",
      "name" : "Mayotte",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/YT"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ZA",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ZA\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ZA</b></p><a name=\"ZA\"> </a><a name=\"hcZA\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ZA (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: South Africa</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ZA"
      }],
      "status" : "active",
      "name" : "South Africa",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ZA"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ZM",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ZM\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ZM</b></p><a name=\"ZM\"> </a><a name=\"hcZM\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ZM (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Zambia</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ZM"
      }],
      "status" : "active",
      "name" : "Zambia",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ZM"
    }
  },
  {
    "resource" : {
      "resourceType" : "Location",
      "id" : "ZW",
      "meta" : {
        "profile" : ["http://ihe.net/fhir/StructureDefinition/IHE.mCSD.Location",
        "http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction"]
      },
      "text" : {
        "status" : "generated",
        "div" : "<div xmlns=\"http://www.w3.org/1999/xhtml\"><a name=\"Location_ZW\"> </a><p class=\"res-header-id\"><b>Generated Narrative: Location ZW</b></p><a name=\"ZW\"> </a><a name=\"hcZW\"> </a><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\"/><p style=\"margin-bottom: 0px\">Profiles: <a href=\"StructureDefinition-IHE.mCSD.Location.html\">IHEmCSDLocation</a>, <code>http://ihris.org/fhir/StructureDefinition/ihris-jurisdiction</code></p></div><p><b>identifier</b>: <a href=\"http://terminology.hl7.org/7.4.0/NamingSystem-v3-iso3166-1.html\" title=\"Identifies the coding system published in the ISO 3166-1 Standard for Country codes. This standard is released periodically, and a new OID will be assigned by ISO for new editions.\">ISO 3166 Part 1 Country Codes</a>/ZW (use: official, )</p><p><b>status</b>: Active</p><p><b>name</b>: Zimbabwe</p><p><b>type</b>: <span title=\"Codes:{http://ihris.org/fhir/CodeSystem/ihris-jurisdiction country}\">Country</span></p><p><b>physicalType</b>: <span title=\"Codes:{http://hl7.org/fhir/codesystem-location-physical-type.html jdn}\">Jurisdiction</span></p></div>"
      },
      "identifier" : [{
        "use" : "official",
        "system" : "urn:iso:std:iso:3166",
        "value" : "ZW"
      }],
      "status" : "active",
      "name" : "Zimbabwe",
      "type" : [{
        "coding" : [{
          "system" : "http://ihris.org/fhir/CodeSystem/ihris-jurisdiction",
          "code" : "country"
        }],
        "text" : "Country"
      }],
      "physicalType" : {
        "coding" : [{
          "system" : "http://hl7.org/fhir/codesystem-location-physical-type.html",
          "code" : "jdn"
        }],
        "text" : "Jurisdiction"
      }
    },
    "request" : {
      "method" : "PUT",
      "url" : "Location/ZW"
    }
  }]
}

```
