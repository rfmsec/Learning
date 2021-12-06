#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)                                                  # Create an ARP packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                  # Create Ethernet layer
    arp_request_broadcast = broadcast/arp_request                                     # Stack the layers
    answered_list = scapy.srp(arp_request_broadcast, timeout=2,verbose=False)[0]      # Capture the results (Scapy returns two lists, we're interested only in the first (answered))
    print("IP Address\t\t\tMAC Adderss")
    print("-------------------------------------------------")

    for element in answered_list:                                                     # Parsing the list (Return only meaningful values)
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)

scan(input("Please enter Host / Network address: "))