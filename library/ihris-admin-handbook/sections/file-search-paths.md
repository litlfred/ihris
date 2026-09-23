---
title: "File Search Paths"
source: http://open.intrahealth.org/w/index.php?oldid=4188
contributors: ["Litlfred", "MarkAHershberger"]
pages: 90-91
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# File Search Paths

The I2CE (Intrahealth Informatics Core Engine) uses a File Search utility to organize the files into categories and define priorties for searching the directories. As of version 3.2 it also provides localization of files.

All files, with very few exceptions, are found using the I2CE\_FileSearch class defined in I2CE/lib/I2CE\_FileSearch.php. The exceptions are those files under I2CE/lib.

## Path Categories

Commonly used pathed categories are:

- templates These are the directories to search for html template files
- images These are the directories to search for image files
- css These are the directories to search for CSS files
- scripts These are the directories to search for javascript files
- classes These are the directories to search for files containing php classes. The convention here is that MyClass is located in the file MyClass.php
- modules These are the directories to look for modules in

You are free to create your own path categories.

## Priorties

Directories in a given category are searched for a file in order of lowest priority to highest priority. If two directories have the same priority and the same file, there is no guarantee which file will be returned.

The paths added by a module have the negative priority of that module. For example an template file in I2CE has priority 0, while a template file found in ihris-manage has priority -200 so that the template file in ihris-manage is found first. There are two exceptions: the paths added by a module in the 'classes' or 'modules' are added with the priority of the module so that a php class found in I2CE takes precedence over one in ihris-manage which has priority 200.

## Adding Paths

The most common way to add a directory to a search path is to do so through a modules \[\[Techincal Overview: Module Structure#Module Configuration File|configuration file\]. For example:

```
<path name='classes'>
  <value>./lib</value>
</path>
```

The &lt;value&gt; tags can be either absolute paths or relative paths. If they are relative paths, they are relative to the directory which contains this configuration file. Some Caveats:

- If you add a '\*' to the end of a path which ends in '/' (or '\\' for windows), this says that all sub-directories of this directory should be added to path. For example, &lt;value&gt;./my\_path/\*&lt;/value&gt; adds in all sub-directories under ./my\_path/

- If you add a '\*' to the end of a path which does not end in a '/' (or '\\' for windows) this says that we add all directories that match the file glob. For example, &lt;value&gt;./my\_paths/go\*&lt;/value&gt; adds in all sub-directories of my\_paths which start with go.
- If you add a '\*\*' to the end of a path which ends in '/' (or '\\' for windows) it will add in all sub-directories, sub-sub-directories, sub-sub-sub-directories etc of the given path.
- If a directory that you add has a sub-directory named 'local' it will first check realtive to this subdirectory for this file. This is useful for development purposes to prevent things from getting committed to bazaar.
- See localization

## Localization

Beginning with version 3.2, we have added in the ability to localize a path. When a path is added to the file search utility, it first checks to see if there is the sub-directory en\_US. If it does not exist, the this directory is not considered to be localized. If it does exist, the path is considered to be localized. In this case, we consider each sub-directory to correspond to a locale.

The preferred locales are set per user. For example, if my preferred locales were fr\_RW and then fr\_FR and then en\_US and I was looking for the file main.html in ./templates which has en\_US as a sub-directory I would look for main.html in this order:

- ./templates/fr\_RW/main.html
- ./templates/fr\_FR/main.html
- ./templates/en\_US/main.html

until I found the file I wanted. If it wasn't there, I would then check for main.html in a directory of higher priority.

## Caching

Because of the high overhead of looking for files all the time, a successful file search will have its results cached in memory via apc \[1\]. In version 3.1, these results are stored globally. Starting in version 3.2, because the localization preference is defined per user, these results are cached per user.

By default, a file is considered to be stale after 60 seconds. The cache can be turned off by modifying the magic data at /I2CE/fileSearch/stale\_time (see I2CE/I2CE\_Configuration.xml).

Caution:If you are developing a new module and add in a template file, the system won't file that file immediately because the file search results are cached. You can either wait the 60 seconds or clear the results stored in the apc \[1\]

memory cache.
