---
title: "Form Storage -- Magic Data"
source: http://open.intrahealth.org/w/index.php?oldid=4191
contributors: ["Litlfred", "MarkAHershberger"]
pages: 96-96
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Form Storage -- Magic Data

## Features

Storing form data in magic data is intended to be used in the following situtations:

- centrally maintained data that does not change frequently
- data that you want translations/localizations for
- data that you do not care to track the history of changes
- data that you want to load in easily for a module

## Storage

All the data for form $form is stored in the magic data instance at the path

```
/I2CE/formsData/forms/$form
```

with each node underneath corresponding to an instance of the form. For example, under

```
/I2CE/formsData/forms/gender
```

we have

```
'F' => Array [
   'last_modified' => '2009-04-27 1:23:45'
   'fields' => Array [
         'name' => 'Female'
     ]
]
'M' => Array [
    'last_modified' => '2009-04-27 1:23:45'
    'fields' => Array [
         'name' => 'Male'
      ]
 ]
```

If there is a parent form for the form, it is saved under 'parent' node for form instance.
