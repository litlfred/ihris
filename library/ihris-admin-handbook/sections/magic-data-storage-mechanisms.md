---
title: "Magic Data Storage Mechanisms"
source: http://open.intrahealth.org/w/index.php?oldid=4198
contributors: ["Litlfred", "MarkAHershberger"]
pages: 478-478
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Magic Data Storage Mechanisms

You can add database storage mechanisms to I2CE\_MagicData. The last one that is added is the "permanent" storage mechanism methods. All others that are added are used to cache the data stored in the permanent storage mechansim.

## Database

This magic data storage mechanism is intended to be used as the "permanent" storage mechanism. By default it is stored into the database table 'config'

## APC

There is magic data storage mechanism based on the Pear APC module and implemented by the class I2CE\_MagicDataStorageAPC. It caches data in the memory segment between reqeusts with a timeout of 5 minutes. Data cached by Apache is not cached on the command line.

To clear the cache manually you can use php-apc web interface.

## SysV

There is magic data storage mechanism based on SysV I2CE\_MagicDataStorageSysV. It is not available in windows. It creates shared memory segments to cache the data between requests. It's advantage over APC is that the same shared segments can be accessed via the command line. There is no time-out for the data stored.

To clear manually from the command line the shared memory segments

```
ipcs -m | grep www-data | awk '{print "ipcrm -m "$2}' | sudo bash
```
