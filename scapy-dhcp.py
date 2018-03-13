#!/usr/bin/env python
#
# script used for packet crafting DHCPdiscover with DHCP Vendor-Class option 60
# dafb // mail@dannyfb.dk

from scapy.all import *

select.iface = "enp0s31f6"

ethernet = Ether(dst='ff:ff:ff:ff:ff:ff',src='50:7b:9d:e2:f4:2b',type=0x800)
ip = IP(src='0.0.0.0',dst='255.255.255.255') 
udp = UDP(sport=68,dport=67)
bootp = BOOTP(chaddr='50:7b:9d:e2:f4:2b', op=1, xid = 0xDEADBEEF, flags=1)
dhcp = DHCP(options=[("message-type", "discover"), (60, "MSFT_IPTV"), "end"])
packet = ethernet / ip / udp / bootp / dhcp

sendp(packet, iface=select.iface)
