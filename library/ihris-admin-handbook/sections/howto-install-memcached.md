---
title: "HowTo: Install Memcached"
source: http://open.intrahealth.org/w/index.php?oldid=29088
contributors: ["Lduncan", "Litlfred"]
pages: 103-104
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# HowTo: Install Memcached

With version 4.0.4 of iHRIS you can use memcahced to improve performance.

## Install Memcached

First install memcached by opening a terminal and typing:

```
sudo apt-get install memcached
```

Then make sure that memcached is enabled. Look at /etc/default/memcached and make sure that it is set to be enabled. You can edit it by typing:

```
sudo gedit /etc/default/memcached
```

Then make sure the content is:

```
ENABLE_MEMCACHED=yes
```

If memcached wasn't enabled then after editing that file you'll need to restart it by typing:

```
sudo /etc/init.d/memcached restart
```

## Install PHP Module

If you are using Ubuntu Lucid, you can simply do

```
sudo apt-get install php5-memcached
```

Otherwise, we need to link memcached with PHP using the memcached PECL library. First make sure the development packages are installed so PECL can compile memcached. Type the following in a terminal:

```
sudo apt-get install libmemcached2 libmemcached-dev apache2-prefork-dev
 php5-dev
```

Now install memcached by typing:

```
sudo pecl install memcached
```

Now enable the module by creating and editing a config file for PHP.

```
sudo gedit /etc/php5/conf.d/memcached.ini
```

Save the following for that file:

```
extension=memcached.so
```

## Restart Apache

Now restart apache to enable the PHP memcached library by typing the following in a terminal:

```
sudo /etc/init.d/apache2 restart
```
