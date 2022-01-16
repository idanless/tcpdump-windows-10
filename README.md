<p style="text-align: center;"><span style="text-decoration: underline;"><strong>Tcpdump on Windows 10</strong></span></p>
<p style="text-align: center;"><em>wrapper&nbsp; <a href="https://docs.microsoft.com/en-us/windows-server/networking/technologies/pktmon/pktmon">microsoft pktmon</a></em></p>
<p style="text-align: center;">Note: this sniffer project can capture only packets from layer 4 of the OSI model (segments), as a result you will not see ARP for example, also DHCP packets cannot be captured.</p>
<p style="text-align: center;">&nbsp;</p>
<p><span style="text-decoration: underline;"><strong>About:</strong></span></p>
<p>As a security \ network guy you need to assist IT, programers or DevOps in debug their app or config from a network perspective to check if the issues are related to the network. Most of the time the they don't have knowledge in how to activate or operate "Wireshark" sniffer, also install "Wireshark" is not easy and not always allowed, for those reasons they need a basic and easy tool like linux "tcpdump" task. This is a windows based on Pktmon "tcpdump", enjoy.</p>
<p><span style="color: #00ff00;">1. First, you must have Admin privileges, so run the project as Admin.</span></p>
<p>*press Enter to select from which network card do you want to capture packets.</p>
<p><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Main.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">2. set a filter, use space button to select which to apply, you can select multiple filters together.</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Filter1.JPG?raw=true" alt="" width="1317" height="260" /></p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Filter2.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">3. You can see the output in one of two options, live or as a pcap file.</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/Recoded.JPG?raw=true" alt="" /></p>
<p style="text-align: left;"><span style="text-decoration: underline;"><strong>live {like tcpdump}:</strong></span></p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/livetraffic.JPG?raw=true" alt="" width="1071" height="516" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">save to pcap:</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/status.JPG?raw=true" alt="" width="947" height="500" /></p>
<p style="text-align: left;">Now you will see counters showing live packets captured, press ctrl+c to stop the capture and get the pcap file.</p>
<p style="text-align: left;"><img src="https://github.com/idanless/tcpdump-windows-10/blob/main/pcapfile.JPG?raw=true" alt="" /></p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">windows will be open the directory with the pcap file waiting :)</p>
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
