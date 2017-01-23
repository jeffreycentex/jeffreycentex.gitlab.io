---



date:  "2008-01-19"
aliases: ["/2008/01/19/quick-vista-networking-tips/"]
title: Quick Vista Networking Tips
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
After spending the past two months wading through the Vista Networking public newsgroup over at msnews.microsoft.com, I have come up with the following tips that will save the users from many problems:


1.  If you are having network access/connectivity issues AND you have a Norton or McAfee network security (not AV, but I won't go there on that one) product, your issue is more than likely the Norton or McAfee product.  I haven't been answering these questions as I made a conscious decision years ago to never let either of these software manufacturers near any computer system I own/manage.  However, there have been countless posts in which Norton/McAfee security products are either blocking communications altogether, or have otherwise made networking the PC's virtually impossible.


2.  Make sure you disable network autotuning to get faster file copying/network access to other workgroup/domain computers.


This is easy, though.  Run the following command from a Command Prompt as an administrator:


<blockquote>
<pre>netsh int tcp set global autotuninglevel=disabled</pre>
<pre>netsh int tcp set global rss=disabled</pre>
</blockquote>
3.  If you can't enable sharing, make sure that you have identified your network as Private.  If it is unidentified or Public, you will not be able to enable sharing (without hacking).


I would hazard to guess that these three issues probably represent about 50% of the issues on an average day. 


