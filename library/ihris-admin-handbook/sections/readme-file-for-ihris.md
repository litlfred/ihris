---
title: "README File for iHRIS"
source: http://open.intrahealth.org/w/index.php?oldid=32580
contributors: ["Cbales", "Litlfred", "Sturlington"]
pages: 502-505
licence: GFDL-1.2
capturedFrom: uploads/ihris-admin-handbook/ihris_admin_handbook_sep_17_2010.pdf
---
# README File for iHRIS

iHRIS Full Suite: Manage, Qualify, Common, I2CE and TextLayout

Version 4.0.5

Release date: 2010-6-14

CONTENTS

1. Contact Information

2. About This Software

3. New Features/Bug Fixes in This Release

4. Hardware and Software Requirements

5. Getting Started

6. Known Issues

7. About the Capacity Project

## 1. CONTACT INFORMATION

HRIS Strengthening team of CapacityPlus

Web: www.capacityplus.org/hris/

Email: \[e-mail redacted\]

Voice: \[phone number redacted\]

IntraHealth International

6340 Quadrangle Drive, Suite 200

Chapel Hill NC 27517 USA

## 2. ABOUT THIS SOFTWARE

CapacityPlus develops the iHRiS Suite core solutions addressing specific issues in human resources for health (HRH) leadership. The iHRIS Suite is free and Open Source software, distributed under the GPL.

iHRIS Manage is a human resources management tool that enables an organization to design and manage a comprehensive human resources strategy. iHRIS Manage helps an organization manage its workforce more effectively and efficiently, while reducing costs and data errors. Using the system, the HR professional can create a hierarchy of positions for an organization based on standard titles, job classifications and job descriptions, even spread over diverse geographic locations, offices and facilities. HR staff can solicit job applications for open positions, assign employees to fill positions and maintain a searchable database of all employees, their identifying information and their qualifications. Managers can track each employee's history with the organization, including their position and salary histories, and record the reason for departure when the employee leaves. iHRIS Manage is primarily intended to be used to manage health care workers employed by a country's Ministry of Health, a hospital or other large health care organization, or a private provider of health care services. However, it may be readily adapted to other types of organizations and workforces.

iHRIS Qualify is a health worker training, licensing and certification tracking system. The system enables a licensing or certification authority for a health worker cadre, such as nurses or physicians, to track data on the complete cadre in a country from pre-service training through attrition. The database captures information about health professionals from the time they enter pre-service training through registration, certification and licensure, and it is updated every time a professional's license or certification is renewed. This system is also capable of tracking continuing medical education attained by health workers, capturing data about foreign-trained workers applying to work within the country and recording out migration verification requests.

iHRIS Common includes common page classes, template files and images for the iHRIS Suite of software: iHRIS Manage, iHRIS Qualify and iHRIS Plan.

IntraHealth Informatics Core Engine (I2CE) is a set of classes for handling database-driven HTML forms with templates and database abstraction. It is the core programming engine for the iHRIS Suite of software.

TexLayout is tools to handle text layout designed to create nicely formatted PDF files. This is used to generate PDF versions of reports.

## 3. NEW FEATURES/BUG FIXES IN THIS RELEASE

View a full list of new features and bug fixes here: \[\[1\]\]

The following new user functions are included in this release:

- The ability to generate and archive standardized documents such as a License Certificate or Employment/Hire Letter
- Speed improvements and better handling of geography in report generation
- A Dependents Module, which was coded-in-country at a Tanzania developer training and enables iHRIS Manage to track information on health worker dependents
- Support for SDMX-HD code lists, http://www.sdmx-hd.org/, to increase interoperability of iHRIS with other Health Information Systems such as OpenMRS and DHIS

Full Italian and French translations for beta testing

The following bug fixes are included in this release:

## 4. HARDWARE AND SOFTWARE REQUIREMENTS

The following software is required to be installed before installing iHRIS:

- Apache Webserver 2.2+: http://www.apache.org
- MySQL 5.0+: http://www.mysql.com
- PHP 5.2.6+: http://www.php.net
- MDB2 from PEAR: http://pear.php.net/package/MDB2
- MySQL driver from PEAR: http://pear.php.net/package/MDB2\_Driver\_mysql
- Text Password from PEAR: http://pear.php.net/package/Text\_Password
- Console GetOpt from PEAR: http://pear.php.net/package/Console\_Getopt
- APC from PECL: http://pecl.php.net/package/APC or http://pecl4win.php.net (Windows)

In order to generate PDF reports, the tcpdf package (http://www.tcpdf.org) is required.

A web browser is required to run the software. Firefox 2+ (http://www.mozilla.com/en-US/firefox/) or Internet Explorer 7+ (http://www.microsoft.com/windows/downloads/ie/getitnow.mspx) is highly recommended.

Optional:

- Tidy from PECL: http://pecl.php.net/package/tidy (included by default for Ubuntu but not Windows)
- GD Php Library: http://www.libgd.org

## 5. INSTALLATION INSTRUCTIONS

Linux (Ubuntu) installation instructions are available on our wiki: http://open.intrahealth.org/wiki/index.php/ Linux\_%28Ubuntu%29\_Installation

Before using the system, you should read the User's Manual, which can be accessed by clicking the Help button on any screen or on our wiki at http://open.intrahealth.org/ihrismanual/.The section "Before Installing the System" provides helpful worksheets for collecting the data needed to enter in the system.

If you have questions or need support, please visit the iHRIS Website by clicking that button on any screen (http:// www.capacityproject.org/hris/) and use the Contact Us form to send us your question.

## 6. KNOWN ISSUES

The following are known bugs in this release of iHRIS. These bugs will be corrected as soon as possible in a subsequent minor release. Please report any bugs to \[e-mail redacted\] or by submitting a bug report at https:/ /bugs.launchpad.net/ihris-suite/.

## 7. ABOUT CapacityPlus

CapacityPlus is developing free, Open Source HRIS solutions, distributed under the GPL, to supply health sector leaders and managers with the information they need to assess HR problems, plan effective interventions and evaluate those interventions. We don't provide just software but rather a program of technical assistance and expertise to ensure that the technology is transferred effectively and serves the ability of decision makers to use data to lead and manage. Our participatory approach results in systems that are appropriate for the context in which they are used and sustainable after we leave.

CapacityPlus is a USAID-funded global project focused on the health workforce needed to achieve the Millennium Development Goals. CapacityPlus is led by IntraHealth International, Inc. Find out more at www.capacityplus.org

Development of this software was made possible by the support of the American people through USAID. The contents are the responsibility of the user and do not reflect the views of USAID, the United States Government or IntraHealth International.

## References

\[1\] http://open.intrahealth.org/mediawiki/IHRIS\_Suite\_4.0\_Development
