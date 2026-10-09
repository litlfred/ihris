# Security (audio transcript)

## Slide 1

In this module, we will look at two of the main security principals used in computing and information technology. We will discuss how this applies to the LAMP architecture on which iHRIS is based. Remember that LAMP is an acronym for Linux, Apache, MySQL and PHP. We will then get into some specifics of the security model used by iHRIS.

## Slide 2

One of the more common security principals in computing is “Security through Obscurity” which is based on the assumption that the details of the security system are not known to those who wish to try and breech the security. In this model, the security of the system rests solely on the ability to keep these details hidden, or obscured. Thus, the main weakness with this security model is if the details become known, then it can more readily be broken or compromised. We will see some examples of this in a few minutes.

## Slide 3

A second security principal, “Secure by Design,” aims to address the weakness of Security through Obscurity. Rather than relying on keeping secrets, in the Secure by Design model, you make known all of the details on how the security system works. These details are known to the system designers, users, as well as potential attackers.

The design of such a system then depends on creating a “hardened” system that can minimize any potential negative impacts from system vulnerabilities. All user input is assumed to be a potential attack, and care is taken to ensure that the user input is valid. The question now is: How do we get such a “hardened” system? One approach is to adopt the methods of open source software.

## Slide 4

The language that computer software is written in is its “source code.” Open source software, is software in which the source code is made available to anyone who wants to read it, and which also gives permission to anyone to make changes to it. And all of this is free of charge!

Linus Torvalds was the person who created the Linux operating systems. One of the fundamental axioms of open source software is known as “Linus’s Law” which states that “Many eyes make all bugs shallow.”

In other words, the more people reviewing and checking for bugs in a software system, the more rapidly bugs are found and fixed. So if the software is open-source, then we have opened the source code up for anyone to read it and find bugs. We have added many more “eyes.”

Now, if we think of a security vulnerability as being one type of a “bug” in the system, then Linus’s law is telling us how a Secure by Design system becomes “hardened.” Namely, that as more and more people review the software, more potential security problems are identified and subsequently fixed.

## Slide 5

Modern cryptography is the basis of the security systems used to protect sensitive data, for example by banks and cell phones. It is also the security system that your web-browser uses whenever you use a site with “https" in the address. Not only are the mathematical details of the cryptographic system well known, the way that the details are implemented in software are as well. Thus this follows the Secure by Design principal.

Another example of Secure by Design is the LAMP architecture which stands for Linux, Apache, MySQL and PHP. Each of these four components of the LAMP architecture are open source software products. Currently, more than 60% of all servers are running Linux, and 90% of the top 500 supercomputers are running Linux. Approximately 60% of the web-servers in the world are running Apache. As Linux and Apache are open source with many users relying on them for very critical applications, you can be sure Linus’s law applies and these are hardened systems.

As another example, consider the security systems used to protect digital media such as DVDs, computer games, eBooks and password-protected commercial software. These security systems are known collectively as different forms of DRM, or Digital Rights Management, and are often based on the Security through Obscurity principal. A quick Google search reveals that many of these systems have been compromised.

## Slide 6

Now let us look at how these security models apply to the iHRIS software. First, as iHRIS has been built to run on the LAMP architecture, we already take advantage of the Secure by Design hardened systems of Linux, Apache, MySQL, and PHP. Next, iHRIS itself is open source, with all of its source code published on a publically accessible site called Launchpad. We have adopted the Secure by Design principal in designing the system. As it has been around for many years, and is in active development and use, there are constantly “eyes” on the iHRIS software.

The iHRIS software is web-based and access to the system is only given to appropriate users. Each user has their own password, and changes to the data can be tracked down to the individual user.

It is expected that the administrators of a server running iHRIS take care of the physical security of the server. This means that the computer should be kept locked away with access provided only as needed.

## Slide 7

The user security model used in version 4.0 of the iHRIS software has two tiers, or layers, which are roles and tasks.

First each user is assigned a role in the system. The role of the user, such as Guest, HR Manager, or Administrator, determines what that user can do as a collection of tasks that they can perform. There are over 300 different tasks in iHRIS and they range from “Adding a person,” to “Viewing a person’s salary history,” to “Editing the details of a position,” to “Creating a new cadre.”

We are now developing version 4.1 of the iHRIS software, in which we add a third tier to our security model – “Record Level Security.” Record Level Security will enable things such as “Self Service” where a user can access and make limited changes to their own information. It will also enable administrators to restrict users to be able to only modify limited parts of the data. For example, only records in a particular facility or district.

## Slide 8

Any web-based software, which includes iHRIS, can take advantage of another level of security, https.

Http is the “usual” way that you access internet sites, such as Google or YouTube. With http there is some potential that someone could be sitting between your computer and the website and listening to your traffic.

To prevent this from happening, https, or “secure http” was developed, which encrypts all communications between your computer and the website. As previously mentioned, https operates on the Secure by Design principal, and it is what is used for things like accessing your bank account online. You may want to consider using https if you are opening up your iHRIS site to the internet, and not just on the Local Area Network, or LAN, that you have at your organization.

If you are considering using https, then there are a few disadvantages that you should be aware of. The first two are minor. It can be slightly slower and requires more configuration of the Apache web server.

The third is that, unless you pay for a third party “signed certificate,” the user will be presented with a scary looking “Security Exception” when first accessing the website. If they are not trained on the meaning of this, this may prevent them from using iHRIS.
