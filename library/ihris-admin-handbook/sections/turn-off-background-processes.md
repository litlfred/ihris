---
title: "Turn Off Background Processes"
source: http://open.intrahealth.org/w/index.php?oldid=14814
contributors: ["Lduncan", "Litlfred"]
pages: 524-524
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Turn Off Background Processes

Background processes are run at configured intervals as users access the site. The main use of background processes is to keep report caches up to date for your site. On sites with large amounts of data you may want to disable running background processes and manually set up a cron job \[1\] to cache reports on a predefined interval instead of as users access the site. This may speed up access on some pages when users begin to access your site after a longer lull in activity. See the How To Configuring Report Generation Timing and Configuring Form Cache Generation Timing for more information on the settings to control report generation.

Here is a sample cron-job entry to generate all reports every night at 2:00am.

```
 0 2 * * * /usr/bin/php '''/var/www/manage'''/index.php
--page=/CustomReports/generate --nocheck=1 > /dev/null 2>&1
```

## References

\[1\] http://en.wikipedia.org/wiki/Cron
