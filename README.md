<p style="text-align: center;"><span style="text-decoration: underline;"><strong>Tcpdump on Windows 10</strong></span></p>
<p style="text-align: center;"><em>wrapper&nbsp; <a href="https://docs.microsoft.com/en-us/windows-server/networking/technologies/pktmon/pktmon">microsoft pktmon</a></em></p>
<p style="text-align: center;"><span style="color: #ff0000;">this cover only&nbsp; network level 4 this mean you will not see</span></p>
<p style="text-align: center;"><span style="color: #ff0000;">ARP\DHCP&nbsp;</span></p>
<p style="text-align: left;"><span style="color: #0000ff;"><span style="color: #0000ff;"><span style="text-align: center; color: #0000ff;"><span style="text-decoration: underline;"><strong><span style="color: #ff0000; text-decoration: underline;">background:</span></strong></span></span></span></span></p>
<p>we as security \ network&nbsp; need to help users debug network \ app issue and check if this related to us most the time the users dont know how work with "wireshark" and for basic task they not needed so i build basic "tcpdump " based on Pktmon built in windows</p>
<p><span style="color: #00ff00;">1. you must have Admin runnig this sofware so first runnig as Admin</span></p>
<p><span style="color: #00ff00;">*press Enter to select the card</span></p>
<p><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Main.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">2. set filter <span style="color: #00ff00;"> select by space button you can set "multi filter"&nbsp;</span></p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Filter1.JPG?raw=true" alt="" width="1317" height="260" /></p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Filter2.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">3. how show the traffic live or save to pcap</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Recoded.JPG?raw=true" alt="" /></p>
<p style="text-align: left;"><span style="text-decoration: underline;"><strong>live {like tcpdump}:</strong></span></p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/livetraffic.JPG?raw=true" alt="" width="1071" height="516" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">save to pcap:</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/status.JPG?raw=true" alt="" width="947" height="500" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/pcapfile.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">you will see live counters and press ctrl+c</p>
<p style="text-align: left;">windows will be open with the pcap file :)</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/openpcap.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;"><span style="text-decoration: underline;"><strong>to do list:</strong></span></p>
<ul>
<li style="text-align: left;">make it as class</li>
<li style="text-align: left;">support wifi&nbsp;</li>
<li style="text-align: left;">make a pip library</li>
</ul>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">&nbsp;</p>
