---



date:  "2004-02-05"
aliases: ["/2004/02/05/remote-desktop-tip-from-darrell-norton/"]
title: Remote Desktop Tip from Darrell Norton
categories: ["old network blog"]
tags: ["old network blog"]
type: "oldnetblog"
---
<a href="http://dotnetjunkies.com/WebLog/darrell.norton">Darrell Norton</a> over at <a href="http://dotnetjunkies.com/WebLog">dotnetjunkies</a> posted a useful tip for those of you who frequently use Windows 2003 Remote Desktop Sessions: 


<blockquote>I have found at least one answer to this problem!  In Windows Server 2003 (only), there is a new group policy setting called <b>Restrict Terminal Services Users to a Single Remote Session</b>.  In the Group Policy snap-in, it is located under (Local Computer Policy/Computer Configuration/Administrative Templates/Windows Components/Terminal Services).  Set the state to <b>Enabled</b>, and people won&#8217;t be able to have two connections.   So they will either reconnect to their session, or come complain for help.  But you won&#8217;t be locked out!


If the users just don&#8217;t understand the difference between Disconnect and Logoff, another useful policy is <b>Remove Disconnect Option from Shut Down Dialog</b>.  Then the only way to disconnect is to close the Remote Desktop Window.� But doing that will popup a dialog box that tells the user the session will still be active.  


</blockquote>
<a href="http://dotnetjunkies.com/WebLog/darrell.norton/posts/6513.aspx">[Darrell Norton&#8217;s Blog]</a>


