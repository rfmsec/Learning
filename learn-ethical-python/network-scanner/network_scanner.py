#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)                                                  # Create an ARP packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                  # Create Ethernet layer
    arp_request_broadcast = broadcast/arp_request                                     # Stack the layers
    answered_list = scapy.srp(arp_request_broadcast, timeout=2,verbose=False)[0]      # Capture the results (Scapy returns two lists, we're interested only in the first (answered))
 
    scan_results = []

    for element in answered_list:                                                     # Parsing the list (Return only meaningful values)
        scan_results.append({"ip": element[1].psrc, "mac":element[1].hwsrc})

    return scan_results

def print_results(scan_results):
    print("IP Address\t\t\tMAC Adderss")
    print("-------------------------------------------------")
    for client in scan_results:
        print(client['ip'] + "\t\t\t" + client['mac'])


# scan(input("Please enter Host / Network address: "))
scan_results = scan("192.168.1.1/24")
print_results(scan_results)