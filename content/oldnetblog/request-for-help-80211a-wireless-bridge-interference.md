---



date:  "2007-04-25"
aliases: ["/2007/04/25/request-for-help-80211a-wireless-bridge-interference/"]
title: 'Request for Help:  802.11A Wireless Bridge Interference'
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
OK, for the second item of the day, I want to make a general call for help in troubleshooting a particularly nasty 802.11A problem I am seeing between our office and branch office (basically, 1/4 of a mile down the road with LOS).


The wireless network works flawlessly for about 166 hours a week.  However, everyday at about 4 PM, we get a few glitches in the data stream.  When I look at the wireless performance data, I am getting about 15% of packet retries for about 5 minutes.  This affects only the data (LAN) transfers and DFS replication.  VOIP does not seem affected at all.  On Wednesdays, however, this packet loss lasts considerably longer (for about an hour or so).  This wreaks havoc with our CAD files (which are still being sent over the WAN).


During Normal Operations:<br />
Strength:  -53 dbm<br />
Noise Level:  -103 dbm


During the "Glitch":<br />
Strength:  -90 dbm<br />
Noise Level:  -103 dbm


I have switched to all of the channels that the device (Tranzeo TR6) will support to no avail...


I'm working with the equipment provider, but I wanted to see if anyone out there has seen this..


I have tried to eliminate other interference sources, but there isn't much that would cause problems throughout the 5 Ghz band...


Thanks for any help.


