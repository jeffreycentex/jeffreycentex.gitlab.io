---



date:  "2007-01-28"
aliases: ["/2007/01/28/network-product-review-pfsense-101-bsd-based-firewall/"]
title: 'Network Product Review:  pfSense 1.0.1 - BSD-based Firewall'
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
OK, I promised all of you a product review in my last blog entry.  My first entrant is an open-source firewall project that I am currently using at my workplace.  I was seeking a relatively "cheap" software-based firewall solution that would provide me with a dual-WAN setup that will allow our office to continue using both our new T1 and the existing DSL connection.


The problems?


<ul>
<li>Incoming Mail (or Spam Traffic) was maxing out the incoming rate for our DSL line.  This resulted in many dropped connections while using the internet in our office.  We had incoming services set as the highest priority to limit problems connecting to our company website and email server.</li>
<li>Our VPN connections were pathetically slow.  This was due to a combination of the mail traffic problem from above and the fact that our incoming connection pipe was capped by SBC at 51.2 KB/sec.</li>
<li>Our new T1 line is fine and dandy for incoming services and VPN connections.  However, we would experience a big dropoff on the web browsing "experience" in the office since the T1 pipe is limited to 150 KB/sec.  This would not be acceptable to the company management.</li>
<li>In addition to our office network, we also have two additional "secured" networks that we wanted to bring into the fold.</li>
<li>Finally, our budget for this project was a spare computer and our time.  Thus is life when one works for a small/mid-sized business that has historically ranked IT as one of the lowest priority levels (this is slowly changing, however)</li>
</ul>
Our new requirements for this project included the following:


<ul>
<li>Push incoming web, email, and VPN traffic in through the T1.</li>
<li>Push office web traffic out via the higher speed DSL connection.</li>
<li>Allow backup access in the event that either transport fails.</li>
<li>Integrate our Surveying and Accounting networks into the new system.</li>
<li>Simple to operate for relatively non-technical people.</li>
<li>Built-in controls to limit P2P and IM traffic</li>
<li>Low cost.</li>
</ul>
After searching far and wide, including various OSS and commercial software firewalls (such as ISA Server) that I could possibly use, I found only two solutions that could possibly work.  However, after installing and testing each product, only one made it through with flying colors - the BSD-licensed open source solution named pfSense.  From the pfSense site:


<blockquote>pfSense is a open source firewall derived from the m0n0wall operating system platform with radically different goals such as using OpenBSD's ported Packet Filter, FreeBSD 6.1 ALTQ (HFSC) for excellent packet queueing and finally an integrated package management system for extending the environment with new features.

</blockquote>
(OT:  I tried m0n0wall, but it did not contain the support to easily setup and administer a dual-WAN setup.)


pfSense contains many features - more than I will ever want and need.  However, it's interface is fairly simple and straight-forward.  Actually, it is very intuitive for anyone with networking experience.  This is good since there is very limited documentation available - for many features, the documentation will refer you to the m0n0wall docs.


Here are some of the key features that may be of use to many small- to mid-sized business IT departments:


<ul>
<li>Wireless Captive Portal</li>
<li>Multiple WAN support</li>
<li>Package Support</li>
<li>Incoming and Outgoing Load Balancing</li>
<li>Wizard-based Traffic Shaping setup</li>
</ul>
For my configuration, I am using pfSense as a dual-WAN solution (T1 and DSL) and I currently have two networks attached (LAN and GPS).  You can configure as many networks as you have network cards.  I am using NAT rules to direct incoming web/mail/vpn traffic to the appropriate servers on our private LAN and firewall/QOS rules to enforce the following network policies:


<ul>
<li>Route all web browsing traffic to a transparent filtering proxy then out through the DSL connection.</li>
<li>Redirect all internal mail transport to our local exchange server, thus limiting our exposure to any wayward laptops or rogue computers exposing us to email viruses/worms.</li>
<li>Restrict all P2P traffic (identified by l7filter) to an incoming and outgoing transfer rate of 1 bit/sec (effectively killing such traffic).</li>
<li>Restricting traffic transport as necessary between separate internal networks.</li>
</ul>
<strong>Installation:</strong>


The installation of pfSense uses a BSD Live CD image that contains an options that will allow you to ability to install it to a hard drive.  You can run it off the CD and a floppy/memory device, but you will be limited on packages and log storage.


<blockquote><strong>Important Note:</strong>


The console of pfSense is NOT secure and a user who has local access can reboot or reset the firewall to factory settings.  So remember one of the cardinal rules of security - <strong>MAINTAIN PHYSICAL CONTROL OF YOUR SYSTEM. </strong>

</blockquote>
A screenshot (of an older version) of the console session is available <a href="http://www.pfsense.com/screens/m0n0wall_console.JPG">here</a>.


During the setup, you will assign network interfaces and will set up the LAN IP address that you will need (later) to access the web interface.


<strong>Post-Installation:</strong>


Once you have it installed (and have the console in a "safe" area), you can administer and setup the firewall from a web browser on your local network.


Here is a view of the opening screen after logging on to the firewall (from my install):


<a href="http://www.networkblog.net/wp-content/uploads/pfsense-main.jpg" title="pfsense-main.jpg"><img src="assets/pfsense-main.thumbnail.jpg" alt="pfsense-main.jpg" /></a>


(Click on image to open a larger view)


On the left, you can see some of the configuration options that are available in pfSense (see <a href="http://www.pfsense.com/index.php?id=27">here</a> for more screenshots of these other options).


For a typical setup, you will be staying in the Interfaces and Firewall section.  Each section is somewhat self explanatory and have all of the options that you would expect for a normal firewall appliance.  The key areas are the NAT and Rules options under the Firewall section.


The NAT section is fairly standard:


<img src="assets/pfsense-nat.jpg" alt="pfsense-nat.jpg" />


As you can see, there are three additional subcategories under NAT - Port Forward, 1:1 (NAT), and Outbound NAT.  In my case, all of the rules were either on the Port Forward and the Outbound tabs.  The Port Forward tab is self explanatory - it works in the same manner as other firewall appliances.  All Firewall rules necessary to add these NAT policies are automatically created on the appropriate interfaces.  However, the Outbound NAT tab is where you set up the dual-WAN magic that pfSense allows:


<img src="assets/pfsense-outbound.jpg" alt="pfsense-outbound.jpg" />


In the case of my configuration, I was allowing two of my internal networks (the LAN and the "GPS" network) access to the 2 different WANs (the DSL and the WAN/T1).  That's all there is to it.


Also, for completeness, here is an example of what the firewall rules interface looks like:


<img src="assets/pfsense-firewall.jpg" alt="pfsense-firewall.jpg" />


Note that there are 4 tabs on this interface.  The number of tabs that you will see depends on the number of interfaces you have defined.


<strong>Other Information:</strong>


There are a few other features that I find extremely useful on a day-to-day basis:


<ul>
<li>Real-Time Traffic Graphs</li>
<li>Extensive logging</li>
<li>IMspector - this is a plugin that allows you to capture all instant messaging conversations on MSN, AOL, and Yahoo IM.  This is useful to install (pending the appropriate company policies) to help you comply with retention policies, if necessary.</li>
<li>Simple backups - you can backup the entire configuration to an XML file that you can reimport in to a different appliance.</li>
</ul>
That is about it..  Comment away if you have any questions.


(BTW:  pfSense is IPV6-capable, but I am not running my local network on IPV6 "yet".  Maybe when I have more time...)


Project Site:  <a href="http://www.pfsense.com">pfSense</a>


Download:  <a href="http://www.pfsense.com/index.php?id=22">Download Site </a>


<a href="http://www.pfsense.com/index.php?id=27">Screenshots </a>


