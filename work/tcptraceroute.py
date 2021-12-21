#!/usr/bin/env python3

import optparse
import scapy.all as scapy


def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-d", "--destination", dest="dst_ip", help="Destination IP address.")
    parser.add_option("-p", "--port", dest="dst_port", help="Destination port.")
    opt, args = parser.parse_args()
    if not opt.dst_ip:
        parser.error("[-] Destination IP must be specified, for more information please use --help")
    if not opt.dst_port:
        parser.error("[-] Destination Port must be specified, for more information please use --help")
    return opt


def trace(ip, port):
    ip = scapy.IP(dst=ip, ttl=(1, 255), id=scapy.RandShort())
    tcp = scapy.TCP(flags="S", dport=int(port))
    ans, unans = scapy.sr(ip/tcp, timeout=5, verbose=False)
    print("HOP\t\t\tAddress\t\t\tSuccess?")
    for snd, rcv in ans:
        flags = rcv.sprintf("%TCP.flags%")
        icmp = rcv.sprintf("%ICMP.type%")
        print(f"{snd.ttl}\t\t\t{rcv.src}\t\t" + icmp if flags == "??" else f"{snd.ttl}\t\t\t{rcv.src}\t\t\t" + flags)
        if rcv.src == snd.dst: return


opt = parse_args()
trace(opt.dst_ip, opt.dst_port)
