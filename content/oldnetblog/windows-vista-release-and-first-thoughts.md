---



date:  "2005-07-28"
aliases: ["/2005/07/28/windows-vista-release-and-first-thoughts/"]
title: Windows Vista Release and First Thoughts
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
Well, most of y&#8217;all probably already know that Windows Vista (although I will always think of it as Longhorn) Beta 1 was released this afternoon.  I finished the download off of MSDN this evening (my beta access is Active, but it doesn&#8217;t allow me to do anything yet) and have spent the past two hours kicking the tires on it&#8230;


First thoughts:


1.  The install supplemental drivers tool is nice.  However, my laptop was still missing drivers for my sound card (standard AC97 drivers), TI Ultramedia drive, and modem.  I installed these off of my system drivers disk and was set&#8230;


2.  IE7 is much nicer than the last time I played with Longhorn (the WinHEC build).  The User interface is much better, with much less wasted space than the earlier build.  My rant - bring back the Refresh icon!


3.  I had one BSOD when I logged out, but I haven&#8217;t been able to reproduce it&#8230;  So for those of you who have it installed, try logging out and see if your machine bugchecks.


4.  McAfee Antivirus On-Access scan and the Windows Search Engine do not mix&#8230;  If I leave the On-Access scan running, then it seems that when the WSE indexes the various files on the machine, it causes McAfee to virus scan them and it completely bogs the system down (100% CPU for two minutes until I could end the McAfee AV task from task manager).


5.  Where did Add/Remove Windows Components go?  I still can&#8217;t find it&#8230;  I wanted to install IIS 7 and see how it changed (I don&#8217;t have access to the server build until sometime tomorrow when the Connect folks fix the access via the beta site), but I can&#8217;t find where to install it&#8230;


6.  The install took a bit over an hour from first booting until I was sitting at the desktop.  This is on an AMD64 3Ghz laptop with 768 MB of RAM.  XP took somewhere around 45 minutes to do the same, but the installer now copies over many more files.


7.  For other beta testers - another bug to reproduce &#8212;  try installing Microsoft Office 2003 from an Administrative install point using the Setup.exe file.  Do you get a setup bootstrap error?  I get it on all of the Office 2003 suite applications.


I&#8217;ll continue to play around with it this week and will try to dogfood it into my daily use to see what else pops up.  I&#8217;ve bugged what I could, but I have about 30~40 bugs or improvement suggestions floating around that I will try to submit tomorrow.


Congratulations to the Windows team for shipping B1.  <a href="http://scoble.weblogs.com">Scoble</a> has some <a href="http://radio.weblogs.com/0001011/2005/07/27.html#a10760">pictures</a> from the Launch Party this morning.  I bet there was a line outside of the build lab this morning for the final disk.


Tags: <a href="http://technorati.com/tag/Windows+Vista" title="See the Technorati tag page for 'Windows Vista'." rel="tag">Windows Vista</a>, <a href="http://technorati.com/tag/Longhorn" title="See the Technorati tag page for 'Longhorn'." rel="tag">Longhorn</a>


