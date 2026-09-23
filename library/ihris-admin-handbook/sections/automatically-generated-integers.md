---
title: "Automatically Generated Integers"
source: http://open.intrahealth.org/w/index.php?oldid=11560
contributors: ["Lduncan"]
pages: 32-32
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Automatically Generated Integers

## Automatically Generated Integers (INT\_GENERATE)

Automatically generated integers (or INT\_GENERATE) are used when a form needs an incremented number to use for an ID but the data entrant may not know what the next available value is. The user can check a checkbox to increment to the next value or if necessary can type in the number if it is known. As of version 4.0.2 INT\_GENERATE is only supported when the form uses the entry form storage mechanism. It uses the field\_sequence table to keep track of the current maximum value for each form field.

In the field\_sequence table there will be an entry with the form field id and the highest value that has been used. The system checks two possibilities for determining the next available number. It looks at the field\_sequence table if a row exists there for the form field and in the last\_entry table for the highest assigned value. Whichever is higher is then incremented by one and saved to the field\_sequence table so it can be accessed the next time a record is added.

If you want to start at 1000 you can just add the form field id and 1000 to field\_sequence. You only need to add something to the field\_sequence table if you want it to start higher than the currently saved values. For example, if you imported data that ranges from 100-400 but you want the generated numbers to start at 1000 then you’ll need to add a row to the field\_sequence table. But if you just want the next number to be 401 then you don’t need to do anything.
