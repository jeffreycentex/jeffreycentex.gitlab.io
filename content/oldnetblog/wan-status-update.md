---



date:  "2007-06-18"
aliases: ["/2007/06/18/wan-status-update/"]
title: WAN Status Update
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
Thanks for all of the help to my request for assistance with out two Tranzeo wireless bridge units.  The ultimate answer was so simple that I am still beating my head on the wall about it..


First, for those of you out there reading this who haven't already met me, I live and work in the Central Texas area.  The place where being outside many hours a day in the spring/summer will result in you being "well done".  Well, this contributed to the problem.  One of our WAN units is completely out in the open and faces west and gets full sun all afternoon.  Ever try going into your car on a hot day with a window pointing west?  It is an oven.  Well, that was what was happening to the WAN unit.  However, it was designed to work this way.  The problem was more related to our signal strength combined with the heat.  Our two units are only a quarter of mile apart and clear line-of-sight.    The problem was the way we were overdriving the units.  I had the power cap set to the full 30dbm on both ends.  This was getting me a normal signal strength between -48 and -53dbm.  However, this was causing the units to be completely overdrived and then the signal completely dropped off, resulting in the -90's we had seen.


The solution?  I changed the power cap from 30dbm down to 8dbm.  Now I get a signal averaging -62dbm and I'm not overdriving the unit.


Woohoo.


This has been a pretty nasty thorn in my side lately.  I have been covering it up by DFS replication, but the link had to be fixed and it had to happen soon.


Now I can sleep better.  :)


