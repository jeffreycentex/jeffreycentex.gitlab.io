---



date:  "2007-01-29"
aliases: ["/2007/01/29/vista-availability/"]
title: Vista Availability
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
&lt;Updated&gt;See <a href="/archives/2007/02/rant-toshiba-and-windows-vista-woes/">here</a> for information on Vista support for the Toshiba M7/R25 Tablets&lt;/Updated&gt;


Well, finally Vista is out for the public.  It has been a long road.  I remember a meeting at Microsoft way back in 2003 when Longhorn was first being discussed.  Much has changed in the past 4 years.  But it is finally done.  Or at least as done as it could possibly be.


Since the vast majority of searches of my site in the past few days have been some variation of Toshiba and Vista, I thought I would get a few points out of the way to answer a few questions (particularly related to Toshiba laptops and tablets):


<ul>
<li>Public Vista Drivers are available for a select few laptops through the normal support channel (M400, for instance) available <a href="http://www.csd.toshiba.com/cgi-bin/tais/su/su_sc_home.jsp">here</a>.</li>
<li>Beta Drivers are available for some other selected machines <a href="http://www.csdsupport.toshiba.com/tais/csd/support/windows_vista/vista_beta.cgi">here</a>.  This list should get shorter as the days go by as drivers are moved from the beta site to the full site.</li>
<li>A Toshiba R25 Tablet PC will work fine with most of the Tecra M7 Toshiba drivers available at the Beta site.</li>
<li>No official support for a Portege M200 is available.  The <a href="http://mobilepcwiki.com/mpc/index.php?title=Toshiba/M200/Windows_Vista_Installation_Notes">Mobile PC Wiki</a> has information on what works and the available drivers for the M200.  A fellow at my office has a M200 and has had issues primarily with the Nvidia display.</li>
<li>The battery life out-of-the-box with Vista and a Toshiba laptop will be pathetic.  However, you can tweak the battery situation by changing the Advanced Settings of your selected profile and tweaking the Cooling Method (under Toshiba Power Savings), Optical Drive Management (same section), Power Saving Mode (under Wireless Adapter Settings), Link State Power Management (under PCI Express), and Power Savings Mode (under Search and Indexing).  Note that you can also tweak the display and the processor states to your liking.  These settings will recover your system to about 90% of the life under XP, at least on my machine.</li>
<li>Glass/Aero works on the Tecra M7/Satellite R20/25 if you have at least 1GB of RAM.  It does not work on the Satellite R10/15.  It may work on the M200 depending on what driver you are using.</li>
<li>Firefox/Tablet Tip:  Install the <a href="http://geckotip.mozdev.org/">GeckoTIP addin</a> for tablet support.</li>
<li>The three Lenovo registry patches referenced <a href="http://www.gottabemobile.com/forum/forum_posts.asp?TID=1547&amp;PN=1">here</a> seem to work on my machine with no ill effects (power management).</li>
<li>The Satellite R25 supports Bitlocker after making the Group Policy changes to allow USB devices (no TPM).  The R15 does not seem to work for me (may be dependent on the updated BIOS that currently refuses to install on the R15 I have available).</li>
<li>Key Tip:  If you upgrade to Vista and have no sound, you need to temporarily go back to XP or a Linux distribution and unmute your system volume.  Better yet, un-mute your audio BEFORE upgrading to Windows Vista.</li>
</ul>
That's it for now.  See ya tomorrow...


