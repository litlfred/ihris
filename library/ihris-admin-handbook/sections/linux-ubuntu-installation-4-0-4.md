---
title: "Linux (Ubuntu) Installation - 4.0.4"
source: http://open.intrahealth.org/w/index.php?oldid=29082
contributors: ["Lduncan"]
pages: 471-477
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Linux (Ubuntu) Installation - 4.0.4

This page contains installation instructions on installing iHRIS version 4.0.4 manually.

Warning: See Installing iHRIS on Ubuntu 10.4 (Lucid) after completing these instructions to get iHRIS working on the latest release of Ubuntu.

Need help? Try our Project Communication

## Getting Ready

Here are instructions for installing the iHRIS Suite on an Linux (Ubuntu) system. If you need help installing Ubuntu you may want to take a look at these directions for installing a Server \[1\] or a Desktop \[2\] system.

Note: Unless specifically mentioned, all the commands below are run using a terminal. You can start this in Ubuntu by going to Applications -&gt; Accessories -&gt; Terminal. Any time a command begins with sudo it will prompt for your password because this will be run with administrative privileges. When you run sudo multiple times, only the first time will ask for your password.

Note: Some installation commands will prompt for inputs in the terminal window, usually with a blue background. The mouse doesn't work to click on options here. You can use Tab to move between options and the space bar to check or uncheck selections.

Note: Some commands will launch the gedit file editor. Look at the documentation \[3\] if you need additional help.

We begin by install a Lamp \[3\] server (You can find more help here \[4\]):

```
sudo tasksel install lamp-server
```

If you have never used mysql on your system, you will be asked to set the 'root' password for mysql. We will refer to this password as XXXXX below.

Important: Make sure your email system is correctly configured. Under a default Ubuntu installation, you can do this with one of two commands:

```
sudo apt-get install postfix
sudo dpkg-reconfigure postfix
```

Follow the on-screen instructions to set up email on your system. For additional help with installing Postfix, look at these instructions \[5\]. On Debian systems, the same commands can be used, but exim4 is the default MTA instead of postfix

If you are using another Linux distribution, make sure your system can send email properly before continuing.

## Configuring MYSQL

Make sure you have in /etc/mysql/my.cnf the following values set:

```
sudo gedit /etc/mysql/my.cnf
query_cache_limit       = 4M
query_cache_size        = 64M
```

It appears that they were reduced with Karmic

## Configuring PHP

Next, you'll need to increase the memory limit for PHP. You can do this by editing the /etc/php5/apache2/php.ini.

```
sudo gedit /etc/php5/apache2/php.ini
```

Change the following line:

```
memory_limit = 32M
```

to:

```
memory_limit = 128M
```

## Installing Pear and PECL Packages

We need to install a few Pear and PECL packages for PHP. For the Pear packages you can do:

```
sudo apt-get install php-pear php-apc  php-mdb2 php-mdb2-driver-mysql
sudo pear install text_password console_getopt
```

During certain activities like installation and upgrades you may need more memory than APC uses by default. The php-apc package should have installed a file in /etc/php5/conf.d/apc.ini. Edit this file:

```
sudo gedit /etc/php5/conf.d/apc.ini
```

Then add the following lines:

```
apc.shm_size=100
apc.slam_defense = Off
```

See slam defense \[6\] and this \[7\].

You'll need to restart Apache after making this change.

```
sudo /etc/init.d/apache2 restart
```

There are two optional packages you may wish to install:

```
sudo apt-get install php5-gd php5-tidy
```

which are used to for inserting images into PDF output of reports and for exporting XML files in a nicely formatted manner

### FileInfo

Note: If you're running Ubuntu 10.4 (Lucid Lynx) then you do not need to install Fileinfo.

The pecl package FileInfo is used to verify the validity of file types used for uploading (e.g. for uploaded images or documents)

```
sudo apt-get install libmagic-dev php5-dev
sudo pecl install Fileinfo
```

If this doesn't work, you can also try:

```
sudo pear install pecl/Fileinfo
echo extension=fileinfo.so | sudo tee
/etc/php5/apache2/conf.d/fileinfo.ini
```

## Configuring Apache Web Server

You will see later we are using the apache rewrite module. To enable the module:

```
sudo a2enmod rewrite
```

Now we need to make sure we can use the .htaccess file.

```
sudo gedit /etc/apache2/sites-available/default
```

Change:

```
<Directory /var/www/>
      Options Indexes FollowSymLinks MultiViews
      AllowOverride None
      Order allow,deny
      allow from all
</Directory>
```

to:

```
<Directory /var/www/>
      Options Indexes FollowSymLinks MultiViews
      AllowOverride All
      Order allow,deny
      allow from all
</Directory>
```

Save and quit.

Let us restart the Apache webserver using:

```
sudo /etc/init.d/apache2 restart
```

## Downloading the Software

To download the software you enter these commands:

```
sudo mkdir -p /var/lib/iHRIS/lib/4.0.4
cd /var/lib/iHRIS/lib
sudo ln -s 4.0.4 4.0
cd /var/lib/iHRIS/lib/4.0.4
sudo wget
http://launchpad.net/ihris-manage/4.0/4.0.4/+download/ihris-manage-full-4_0_4.tar.bz2
sudo tar -xjf ihris-manage-full-4_0_4.tar.bz2
```

## Database Setup

To create the needed database you can do:

```
mysql -u root -p
```

Enter the password you set above (XXXXX) for MySQL. You will now be able to send commands to MySQL and the prompt should always begin with 'mysql&gt; '. Type these commands:

```
CREATE DATABASE ihris_manage;
GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost
identified by 'PASS';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
```

Substitute PASS with something appropriate. We'll refer to this password as YYYYY.

If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan).

In version 4.0.1 of iHRIS we create mysql functions. If you are having trouble creating routines see this \[4\].

Alternatively, you may choose to install phpmyadmin to administer database through the web

```
sudo apt-get install phpmyadmin
```

A screen will come up asking if you want to install for apache2 or lighttpd. Highlight apache2 and press the spacebar to select it. It will ask for the root password (XXXXX) and you may also opt to create a phpmyadmin user to extra

features. Select a password for this user as well.

Now browse to:

http://localhost/phpmyadmin

login with the user 'root' and password XXXXX that you set above. Once logged in you will create a database and user called ihris\_manage. To do this, click on the 'Privileges' link and select 'Add a new User'. Then fill out the form as follows:

![Image:Phpmyadmin\_create\_user.gif](../images/img-p475-1.png)

Creating iHRIS\_Manage Database and User

For security, make sure the password you choose is different than the root password for MySQL. Let us refer to this password as YYYYY.

## Creating a Site Configuration File

We are going to start by modifying the BLANK site for iHRIS Manage. If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change manage to qualify or plan. To copy the BLANK site:

```
sudo mkdir -p /var/lib/iHRIS/sites
sudo cp -R /var/lib/iHRIS/lib/4.0/ihris-manage/sites/blank
/var/lib/iHRIS/sites/manage
```

We now need to edit the site configuration file:

```
sudo gedit /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml
```

by changing:

```
<path name='modules'>
  <value>./modules</value>
  <!-- If this site module is not installed under the iHRIS Manage
       file structure, then remember to include a path to the rest of
       the modules here. e.g.
   -->
</path>
```

to:

```
<path name='modules'>
  <value>./modules</value>
  <value>/var/lib/iHRIS/lib/4.0</value>
</path>
```

### Set Email Address

You may optionally choose to change the email address feedback is sent to by changing:

```
<configuration name='email' path='to' values='single'>
  <displayName>Email Address</displayName>
  <value>BLANK</value>
</configuration>
```

to:

```
<configuration name='email' path='to' values='single'>
  <displayName>Email Address</displayName>
  <value>my_email@somewhere.com</value>
</configuration>
```

## Making the Site Available

We will now edit the configuration to let the site know about the database user and options:

```
sudo gedit /var/lib/iHRIS/sites/manage/pages/config.values.php
```

We now need to uncomment and set the value of a few variables. Commented lines will begin with two slashes (//) that you'll need to remove.

They are:

Variable Name Value

$i2ce\_site\_i2ce\_path /var/lib/iHRIS/lib/4.0/I2CE

$i2ce\_site\_dsn mysql://ihris\_manage:YYYYY@localhost/ihris\_manage

$i2ce\_site\_module\_config /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml

In $i2ce\_site\_dsn, YYYYY is the password you set above.

Save and quit.

Finally, we make iHRIS Manage site we just created available via the webserver:

```
sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/manage
```

### Pretty URLs

This is an optional step to make URLs cleaner by removing the index.php.

```
sudo cp /var/www/manage/htaccess.TEMPLATE /var/www/manage/.htaccess
sudo gedit /var/www/manage/.htaccess
```

We need to look for the line RewriteBase and change it to the web directory we want to use we are using, /manage.

Change the line that looks like:

```
    RewriteBase /iHRIS/manage-BLANK
```

to:

```
    RewriteBase /manage
```

You may now save and quit.

## Finishing Up

Now we are ready to begin the site installation. Simply browse to:

http://localhost/manage

and wait for the site to initalize itself. Congratulations! You may log in as the i2ce\_admin with the password you used to connect to the database (YYYYY that you set above).

## Files

Here are samples of the files we edited above. WARNING THESE ARE OUT OF DATE AND REFER TO AN OLD VERSION OF THE SOFTWARE

- /etc/apache2/sites-available/default
- /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml
- /var/www/manage/.htaccess
- /var/www/manage/config.values.php

## References

\[1\] http://www.howtoforge.com/perfect-server-ubuntu8.04-lts \[2\] http://www.howtoforge.com/the-perfect-desktop-ubuntu-8.04-lts-hardy-heron \[3\] https://help.ubuntu.com/community/gedit \[4\] https://help.ubuntu.com/community/ApacheMySQLPHP \[5\] https://help.ubuntu.com/community/PostfixBasicSetupHowto \[6\] http://pecl.php.net/bugs/bug.php?id=16843 \[7\] http://t3.dotgnu.info/blog/php/user-cache-timebomb
