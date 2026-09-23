---
title: "Form Storage Mechanisms"
source: http://open.intrahealth.org/w/index.php?oldid=33551
contributors: ["Lduncan", "Litlfred", "MarkAHershberger"]
pages: 100-100
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Form Storage Mechanisms

A storage mechanism is defined by subclass I2CE\_FormStorage\_Mechanism which provides the methods to read, and possibly write, the data for any form with the given mechanism. If the data is stored in a database, it can sub-class I2CE\_FormStorage\_DB and provide read access to the data as a form by only defining one method, getRequiredFieldsQuery(). To make a storage mechanism writable, you only need to write a method which defines how to store a data field.

Once a storage mechanism is written, the data for that form can be queried via searches with limits.

The currently (or soon-to-be) available storage mechanisms are:

- entry: A vertical database storage mechanism which keeps a history of when and by who individual fields (data elements) were changed. This is the default storage mechanism, and the storage mechanism that was used in version prior to 3.2.
- flat: A horizontal database storage mechanism, where a row of a table corresponds to an instance of a form. The columns, or any SQL function, of the table are used to define the fields.
- multi\_flat: A horizontal database storage mechanism similar to the flat storage mechanism but combining several identically structured tables. It is primarily intended for data collation.
- magicdata: A locale aware storage mechanism primarily intended for centrally maintained lists of data.
- CSV: A storage mechanism to read data from a CSV file
- Eval: A storage mechanism to populate and get records based on php function calls
- XML: A storage mechanism to populate and get records based on an XML file.
- SDMX-HD: A storage mechanism to populate and get records based on SDMX-HD code lists.
- SDMX Cross Sectional: A storage mechanism to populate and get records based on SDMX Cross Sectional Data.

## Aggregating Storage Mechansims

You may be in a situation in which you need to aggregate from several different instances of iHRIS Manage (or Qualify). You can mark a specific a storage mechanism, $storage\_mechanism, as being aggregating by setting:

```
/modules/forms/storage_options/$storage_mechanism/componentized
```

to 1. Then each form $form that uses that storage mechanism, will be componetized.

At the moment, only the Multi-Flat storage mechanism is an aggregating storage mechanism.

Once the form-storage module is enabled, an instance of I2CE\_Form has the method isComponentized() to check if a form is componentized. You can also check via I2CE\_FormStorage::isComponentized($form)
