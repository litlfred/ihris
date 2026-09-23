---
title: "Exporting and Updating Form Caches Using Profiles - 4.0.6"
source: http://open.intrahealth.org/w/index.php?oldid=32923
contributors: ["Litlfred"]
pages: 82-83
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Exporting and Updating Form Caches Using Profiles - 4.0.6

To see this tutorial for different versions of the software see the following:

In version 4.0.6 we add the ability to create profiles of form caches. A profile is a simply a list of forms that you can use to rapidly:

- Update the cache for each of the forms in the profile
- Export the cache, via a mysqldump, for each of the forms in the profile. This is particularly useful for exporting data from a regional or district office to the national level.

This functionality is part of the Cached Forms modules and can be accessed by clicking on the links for Configure System and then Cached Forms

## Creating A Profile

The first step is to create a profile of the forms. A profile is a list of forms with a short name that you can use to help you identify the list.

1. Look under Create/Edit Profile on the Cached Forms page. Here make sure "Create a new profile" is selected in the drop-down, and then click the "Edit" button. 2. Now type a name for the profile. It is best to keep it short with limited punctuation such as "nightly\_update" 3. Now select each of the forms you wish to include in the profile 4. Finally, click the "Submit" button at the bottom of the page

## Updating the Cache of a Profile

You can update all of the forms in a profile under Cache Forms on the Cached Forms page.

1. Choose the profile for which you wish to cache forms 2. Click the "Cache" button

## Exporting the Cache of a Profile

There are two main usages of exporting all of the forms in profile, you can either get all the data, or only the modifications to the data since the last date. Both can be accessed under Export Cached Forms on the Cached Forms page.

1. Choose the profile you wish to export 2. Choose to enable bzip2 compression or not 3. Optionally select the modification time.

1. If you do not set the modification time, you will get all of the data for the forms. The mysqldump will include "DROP TABLE IF EXISTS" and "CREATE" statements for each of the hippo\_XXXX tables. Data is populated via "INSERT" statements 2. If you do not set the modification time, you will get all of the data for the forms. The mysqldump will include neither the "DROP TABLE IF EXISTS" nor the "CREATE" statement for each of the hippo\_XXXX tables. Data is populated via "REPLACE" statements. 4. click the "Export" button

Note: When you export the cache, it does not first update it. You will need to do this manually.

## Crontab and Command Line Interaction

For example, you may wish to put an update of the profile "nightly\_update" in your crontab:

```
 30     1     *     *     *         /usr/bin/php /var/www/ihris-manage/index.php --page=/CachedForms/cache --get=profile=nightly_update
```

will cause all forms in the 'nightly\_update' profile to be update at 1:30am. Putting:

```
 10     *     *     *     *         /usr/bin/php /var/www/ihris-manage/index.php --page=/CachedForms/cache --get=profile=hourly_update
```

in your profile will update every form in the 'hourly\_update' profile at ten minutes past the hour.
