---
title: "Technical Overview: Form Storage -- Eval"
source: http://open.intrahealth.org/w/index.php?oldid=11498
contributors: ["Litlfred"]
pages: 518-518
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Technical Overview: Form Storage -- Eval

This form storage mechanism is present in version &gt;= 4.0.3.

## Form Storage Options

The options specifying a php-eval storage for $form are stored at:

```
/modules/forms/forms/$form/storage_options/eval
```

It has the following structure:

- records: The function to call to get the list of available records/form ids
- parent: optional parent node

- populate: optional scalar node. if set, it is the php code used to get the parent id of the current id. the current id can be accessed as $id
- fields: optional parent node containing a sub node for each field indexed by the $fieldName

- $fieldName: optional parent node

- populate: optional scalar node. if set, it is the php code used to get the db-value of the field for the current id. the current id can be accessed as $id
