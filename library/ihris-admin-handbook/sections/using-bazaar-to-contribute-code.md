---
title: "Using Bazaar to Contribute Code"
source: http://open.intrahealth.org/w/index.php?oldid=4230
contributors: ["Litlfred", "Lucaswood", "MarkAHershberger"]
pages: 527-530
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# Using Bazaar to Contribute Code

We maintain all of our code in Launchpad \[1\] using the Bazaar \[2\] version control system.

## Bazaar

### Installing Bazaar

You can install bazaar under ubuntu via

```
sudo apt-get install bzr bzrtools
```

### Using Bazaar

You should try the five minute tutorial \[4\]. The software sources are below as well as some directions to set up a development server. Happy committing.

### Bazaar Branches

There are a few software components that we maintain, and for each there is a release and development trunk.

- Release

- i2ce \[3\] bzr branch lp:i2ce/3.1
- ihris-common \[4\] bzr branch lp:ihris-common/3.1
- ihris-manage \[5\] bzr branch lp:ihris-manage/3.1
- ihris-plan \[6\] bzr branch lp:ihris-plan/1.0
- ihris-qualify \[7\] bzr branch lp:ihris-qualify/3.1

- textlayout \[8\] bzr branch lp:textlayout/3.1
- Development

- i2ce \[9\] bzr branch lp:i2ce
- ihris-common \[10\] bzr branch lp:ihris-common
- ihris-manage \[11\] bzr branch lp:ihris-manage
- ihris-plan \[12\] bzr branch lp:ihris-plan
- ihris-qualify \[13\] bzr branch lp:ihris-qualify

## Working On The Code

Suppose you want to setup a development server on your machine to play around with the code. Here are some steps that you can take to install iHRIS Manage under your home directory and setup up the apache and mysql web server.

### Installing The Required Software

First we need to install some prerequisites for the software

```
sudo apt-get tasksel install lamp-server
sudo apt-get install php-apc php5-gd php5-tidy
```

### Creating The Database

You can create the database, which we will call ihris\_manage by:

```
mysql -u root -p
mysql> CREATE DATABASE ihris_manage;
mysql> GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
```

here you should change 'PASS' to whatever you want. You can also use phpmyadmin to create the database.

### Getting The Code

Now we want to get the code from launchpad.

```
mkdir ~/ihris-dev
cd ~/ihris-dev
bzr branch lp:i2ce
bzr branch lp:ihris-common common
bzr branch lp:ihris-manage manage
bzr branch lp:textlayout/3.1 textlayout
```

### Binding The Code

You may wish to bind your branch to the launchpad hosted branch to automatically commit there. For example, for iHRIS Manage, you can do:

```
bzr bind bzr+ssh://<YOUR USER NAME>@bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/3.2-dev/
```

### Configuring The Software

In iHRIS Manage, there is a demo site setup with sample data. We can make this available in apache by doing the following:

```
cd /var/www
sudo mkdir ihris-dev
cd /var/www/ihris-dev
sudo ln -s ~/ihris-dev/manage/sites/Demo/pages manage
```

Once we complete some configuration options, you can access the site at:

```
http://127.0.0.1/ihris-dev/manage
```

To complete the configuration we need to tell the application which database we want to use: We will now edit the configuration to let the site know about the database user and options:

```
gedit ~/ihris-dev/manage/sites/Demo/pages/config.values.php
```

We now need to uncomment and set the value of a few variables. They are:

Variable Name Value

$i2ce\_site\_i2ce\_path /home/YOUR\_USER\_NAME/ihris-dev/i2ce

$i2ce\_site\_database ihris\_manage

$i2ce\_site\_database\_user ihris\_manage

$i2ce\_site\_database\_password PASS (the password you set above)

$i2ce\_site\_module\_config /home/YOUR\_USER\_NAME/ihris-dev/manage/sites/Demo/iHRIS-Manage-Demo.xml

Save and quit.

### URL Rewriting

Finally, we can make our url's pretty by turning on rewriting. This is an optional step.

```
sudo a2enmod rewrite
cd ~/ihris-dev/manage/sites/Demo/pages
cp htaccess.TEMPLATE .htaccess
gedit .htaccess
```

We need to look for the line RewriteBase and change it to the web directory we want to use we are using, /ihris-dev/manage. You may now save and quit.

To make sure we can use our new .htaccess file do:

```
sudo gedit /etc/apache2/sites-available/default
```

and change:

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

## Coding Policy

### Indentation and Formatting

No tabs please. All tabs should be converted to 4 spaces. The indentation style for (PHP) code should be bsd \[14\].

### Documentation

We document our php code with phpdoc \[15\].

## References

\[1\] http://www.launchpad.net \[2\] http://bazaar-vcs.org/ \[3\] https://code.launchpad.net/~intrahealth+informatics/i2ce/3.1.4-release \[4\] https://code.launchpad.net/~intrahealth+informatics/ihris-common/3.1.4-release \[5\] https://code.launchpad.net/~intrahealth+informatics/ihris-manage/3.1.4-release \[6\] https://code.launchpad.net/~intrahealth+informatics/ihris-plan/1.0.4-release \[7\] https://code.launchpad.net/~intrahealth+informatics/ihris-qualify/3.1.4-release \[8\] https://code.launchpad.net/~intrahealth+informatics/textlayout/3.1.4-release \[9\] https://code.launchpad.net/~intrahealth+informatics/i2ce/3.2-dev \[10\] https://code.launchpad.net/~intrahealth+informatics/ihris-common/3.2-dev \[11\] https://code.launchpad.net/~intrahealth+informatics/ihris-manage/3.2-dev \[12\] https://code.launchpad.net/~intrahealth+informatics/ihris-plan/1.1-dev \[13\] https://code.launchpad.net/~intrahealth+informatics/ihris-qualify/3.2-dev \[14\] http://en.wikipedia.org/wiki/Indent\_style#BSD\_KNF\_style \[15\] http://www.phpdoc.org/
