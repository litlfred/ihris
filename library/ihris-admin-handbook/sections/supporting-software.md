---
title: "Supporting Software"
source: http://open.intrahealth.org/w/index.php?oldid=4200
contributors: ["Litlfred", "MarkAHershberger", "Sturlington"]
pages: 507-507
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Supporting Software

This documentation is current as of iHRIS version 3.1 (August 15, 2008).

The server has been installed with Ubuntu 8.04 LTS, a long-term release that will be supported for five years. The IP address is #.#.#.# and can be accessed from inside the local network. All references below will use this address and should be updated if it is changed.

General documentation on Ubuntu can be found at the Ubuntu website \[1\].

## Server Information

### Updates

Install software updates using the Update Manager (System → Administration → Update Manager). It will display any packages that need updating, and those packages can then be installed. Install new packages using Synaptic Package Manager (System → Administration → Synaptic Package Manager).

### MySQL

MySQL can be administered using terminal commands (Applications → Accessories → Terminal). See documentation on MySQL \[2\].

MySQL can also be administered using PHP MyAdmin at http://#.#.#.#/phpmyadmin/.The administrative login is XXXX and the password is XXXXXXX. The password can be changed via the privileges link with PHP MyAdmin.

### Apache 2

The installed web server is Apache 2. See documentation \[3\]. The configuration files are located in /etc/apache2/ on the server. The log files are saved in /var/log/apache2/. The files displayed by the web server are in /var/www/.

### PHP 5

PHP 5 is installed to run the iHRIS Plan software. See documentation \[4\].

## References

\[1\] http://help.ubuntu.com/8.04/ \[2\] http://dev.mysql.com/doc/refman/5.0/en/index.html \[3\] http://httpd.apache.org/docs/2.2/ \[4\] http://www.php.net/manual/en/
