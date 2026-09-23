---
title: "Recreate All Form Caches"
source: http://open.intrahealth.org/w/index.php?oldid=4337
contributors: ["Lduncan", "Litlfred"]
pages: 505-505
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Recreate All Form Caches

If you've imported data multiple times, the form cache will include some of that old data. To completely recreate all the form caches follow these steps. These instructions are for iHRIS version 3.1.x. These are advanced instructions and should only be done if you know what you are doing. You should back up your database before doing this in case anything goes wrong.

1. Open up two browser windows. One to the site and one on phpmyadmin. 2. Go to Configure System then Browse Magic Data. 3. Click modules 4. Click CachedForms 5. Click times 6. Click generation 7. This should list all the forms on the site with a number. Click the Erase button at the bottom of the page. Make sure the path at the top is: /modules/CachedForms/times/generation 8. With PHPMyAdmin drop all the tables that start with hippo\_. You can check them all in the table list and then select “Drop” from the dropdown at the bottom. It’ll display a confirmation message. Just make sure it’s only the hippo\_\* tables. 9. Back on the site go to Configure System then Cached Forms. 10. At the bottom of the page click the link at Generate Cache for all forms. 11. That should be it when it finishes redoing the form caches. 12. You can then wait for the reports to regenerate automatically or go to Create Reports -&gt; Reports and click the generate link next to them all.
