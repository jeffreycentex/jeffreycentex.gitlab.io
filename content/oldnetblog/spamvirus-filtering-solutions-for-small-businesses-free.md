---



date:  "2006-04-06"
aliases: ["/2006/04/06/spamvirus-filtering-solutions-for-small-businesses-free/"]
title: Spam/Virus Filtering Solutions for Small Businesses (Free)
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
OK, for all of you out there who work in a small business environment (or a &#8220;stingy&#8221; company, IT-wise), I have a recommendation for you on an excellent way to filter spam/virus email and even limited web traffic virus scanning - and best of all, it is free.


<strong>CopFilter (for the IPCop software firewall distribution)</strong>


From the <a href="http://www.copfilter.org/">website</a>:


<blockquote>The main goal of <a href="http://www.copfilter.org/">Copfilter</a> is to provide a free and easy to use solution to filter and scan traffic           from any unsecure network, like the internet, for viruses and spam. It has been designed            as a preconfigured and easy to install addon for the opensource firewall <a href="http://www.ipcop.org/">IPCop</a>           .  Copfilter is a package of various opensource traffic filtering software and tools, customized and built to work            together smoothly.  All included proxies filter traffic transparently, which means that no client reconfiguration is necessary.  It scans POP3 and SMTP emails for viruses and spam. Instead of a virus infected emails, a user will receive virus<br />
notification messages containing details about originally sent emails, which can also be quarantined if desired.            Spam emails will be tagged as spam by inserting the following text into the subject field:   *** SPAM ***            . With this procedure any email client will be able to use its own message filtering rules to           automatically delete or move these spam messages into a different folder for a later review.           HTTP and FTP traffic will also be scanned for viruses. If a virus is found, access to that web page or file will be denied.


</blockquote>
I use a subset of this capability at the office to provide limited virus and scanning checking (I also use an Exchange-based solution, along with IMF, to enhance the Spam and Virus tracking).  I have offloaded much of the core scanning infrastructure off of our somewhat &#8220;overloaded&#8221; exchange server.


This type of setup is also ideal when you need to set up a quarantine network.  I put untrusted machines from the &#8220;wild&#8221; on this network in order to get their patch and AV level back up to snuff before allowing them on the real LAN.


For a small (under 25 person) business, this is an ideal, low cost solution.  The standard caveats exist, though - keep the box up-to-date with all security fixes and lock it down as much as you can.


Tags: <a href="http://technorati.com/tag/IPCOP" title="See the Technorati tag page for 'IPCOP'." rel="tag">IPCOP</a>, <a href="http://technorati.com/tag/COPFILTER" title="See the Technorati tag page for 'COPFILTER'." rel="tag">COPFILTER</a>, <a href="http://technorati.com/tag/" title="See the Technorati tag page for ''." rel="tag"></a>


