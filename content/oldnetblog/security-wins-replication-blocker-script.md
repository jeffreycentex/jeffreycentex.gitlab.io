---



date:  "2004-12-07"
aliases: ["/2004/12/07/security-wins-replication-blocker-script/"]
title: 'Security:  WINS Replication Blocker Script'
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
<acronym title="Microsoft">MS</acronym> has posted a script that will allow netadmins to work around the new WINS security vulnerability&#8230;  


<blockquote>This script accomplishes this by creating an IPSec policy with two filter rules that:<br />
1. Block inbound packets destined for TCP or UDP port 42 from any host<br />
2. Block outbound packets destined for TCP or UDP port 42 to any host


</blockquote>
Note that this only works with Windows 2000/2003 based systems&#8230;


Ooops&#8230;  I forgot the link&#8230;  <a href="http://www.microsoft.com/downloads/details.aspx?FamilyID=20f8df98-7eee-4293-b80a-c34bb1208828&#38;DisplayLang=en">Click Here</a>


(this brings back memories from the early 2000/2001 when I used to use IPSec to firewall my machines&#8230;)


