#!/usr/bin/env python3

import subprocess
import optparse
import re

MAC_pattern = r"(\w\w:){5}\w\w"

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option("-R","--reset", dest="reset", default=False, help="Reset to original MAC")
    parser.add_option("-i","--interface", dest="interface", help="Interface name")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    (opt, arg) = parser.parse_args()
    if opt.reset:
        print("[+] Reverting to original MAC address")
        opt.new_mac = get_def_mac(opt.interface)
    elif not opt.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not opt.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return opt

def get_current_mac(interface):
    print(f"[+] Checking for the MAC address of interface {interface}.")
    ifconfig_output = subprocess.run(['ifconfig',interface], capture_output=True, encoding='utf-8')
    if re.search(MAC_pattern, ifconfig_output.stdout):
        found = re.search(MAC_pattern, ifconfig_output.stdout).group(0)
        print(f"[+] Found the following MAC address: {found}.")
        return found
    else:
        print(f"[-] ERROR! Could not locate the current MAC address for inteface {interface}")
        exit()

def get_def_mac(interface):
    cmd = "ethtool -P " + interface + " | awk '{print $3}'"
    def_mac = subprocess.run(cmd, capture_output=True, shell=True, encoding='utf-8')
    return def_mac.stdout.strip()

def change_mac(interface, new_mac):
    current_mac = get_current_mac(interface)
    print(f"[+] Changing the MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw", "ether", new_mac])
    subprocess.call(["ifconfig",interface,"up"])
    new_mac = get_current_mac(interface)
    print("[+] Success? True" if new_mac != current_mac else "[-] Success? False")

opt = parse_args()
change_mac(opt.interface, opt.new_mac)