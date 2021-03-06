---



date:  "2005-08-25"
aliases: ["/2005/08/25/8021x-not-secure-for-wired-networks%e2%80%a6/"]
title: 802.1x Not Secure for Wired Networks…
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
Steve Riley has posted a fairly long <a href="http://www.microsoft.com/technet/community/columns/secmgmt/sm0805.mspx">article</a> about why 802.1X should not be deployed on wired networks&#8230;  


This is relatively new to me, considering that the 802.1X was the backbone of the Network Access Protection feature that will ultimately be included in Longhorn Server.  My problem with the proposed solution that <acronym title="Microsoft">MS</acronym> is advocating - domain isolation - seems to be limited to Windows products.  Even when one looks at the <a href="http://www.microsoft.com/technet/itsolutions/msit/security/ipsecdomisolwp.mspx">Improving Security with Domain Isolation: Microsoft IT implements IP Security (IPsec)</a>, <acronym title="Microsoft">MS</acronym> recommends using Boundary computers to allow unsecure connections from UNIX, Mac, Pocket PC, and other networking devices otherwise incompatible with the IPSec security features in Windows.  This isn&#8217;t manageable for small and mid-sized organizations that also have a need for wired security.  Will there be a better solution in the Longhorn Server timeframe?  I&#8217;m not sure (yet).


How do the rest of you secure your wired networks (especially in small/mid-sized businesses)?  I have resorted to disconnecting unused network drops at the patch panel to keep rogue laptops from our private network&#8230;  All network drops in public areas and conference rooms are connected to a public network that either has limited internet or <acronym title="Virtual Private Network">VPN</acronym> access.


Tags: <a href="http://technorati.com/tag/802.1X" title="See the Technorati tag page for '802.1X'." rel="tag">802.1X</a>, <a href="http://technorati.com/tag/IPSec" title="See the Technorati tag page for 'IPSec'." rel="tag">IPSec</a>


