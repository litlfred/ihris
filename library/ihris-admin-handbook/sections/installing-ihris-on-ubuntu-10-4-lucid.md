---
title: "Installing iHRIS on Ubuntu 10.4 (Lucid)"
source: http://open.intrahealth.org/w/index.php?oldid=33731
contributors: ["Lduncan", "Litlfred"]
pages: 446-447
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Installing iHRIS on Ubuntu 10.4 (Lucid)

Ubuntu 10.4 comes with PHP 5.3 so there a few a few issues that need to be corrected.

## APC

To compile pecl packages yourself you'll need these packages installed. They may already be installed.

```
sudo apt-get install php5-dev apache2-prefork-dev
```

The version of APC that ships with 10.4 causes problems. You'll need to downgrade it for it to work. When it asks if you want to use the spin locks type in yes. Run the following commands in a terminal:

```
sudo apt-get remove php-apc
sudo pecl config-set preferred_state beta
sudo pecl install APC-3.1.2
sudo pecl config-set preferred_state stable
```

Now you need to set the configuration options for APC. Create or edit the ini file by typing:

```
sudo gedit /etc/php5/conf.d/apc.ini
```

The contents should be:

```
extension=apc.so
apc.shm_size=100
apc.write_lock=1
apc.slam_defense=0
```

## Sessions

Now you need to set the session save path. The default is /tmp but that is causing problems and the script to clean up sessions doesn't look there. You'll need to edit the files for apache and cli and make the same change. To edit the apache php config type:

```
sudo gedit /etc/php5/apache2/php.ini
```

Find the line that looks like:

```
;session.save_path = "/tmp"
```

And change it to be (don't forget to remove the semi-colon):

```
session.save_path = "/var/lib/php5"
```

Now edit the cli config file and make the same change:

```
sudo gedit /etc/php5/cli/php.ini
```

## Restart

Now restart apache and memcached (if you're using it) and try to access your site again.

```
sudo /etc/init.d/apache2 restart
sudo /etc/init.d/memcached restart
```
