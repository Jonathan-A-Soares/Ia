import socket
import json
import functools
from ipaddress import IPv4Address
from ping3 import ping
from getmac import getmac
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
import os

try:
    dir = 'return'       
    os.makedirs(dir)
except FileExistsError:
    print("Cod: 551")

def IpScanNetwork(Ini, End,speed):
    if speed == "fast":
        Speed = 0.3
    elif speed == "low":
        Speed = 4
    r ={}
    with open( 'return/Ips.json', 'w') as json_file:
        json.dump(r, json_file, indent=4)

    with open('return/Ips.json') as f:
        fre = json.load(f)

    inicial = IPv4Address(Ini)
    final = IPv4Address(End)
    o =0
    ips = [str(IPv4Address(ip)) for ip in range(int(inicial), int(final))]
    try:
        for ip in ips:
            t = ping(ip, timeout=Speed)
            status = False if t is None else True
            

            if status:
                o = o + 1
                print(f'IP: {ip} [{status}]')
                try:
                    eth_mac = get_mac_address(interface="eth0")
                    win_mac = get_mac_address(interface="Ethernet 3")
                    ip_mac = get_mac_address(ip=ip)
                    ip6_mac = get_mac_address(ip6="::1")
                    host_mac = get_mac_address(hostname="localhost")
                    updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)
                    getmac.PORT = 44444
                    mac = getmac.get_mac_address(ip=ip, network_request=True)
                    fabri = MacLookup().lookup(mac)
                    result = {
                        "Ip": ip,
                        "Status": status,
                        "mac":mac,
                        "fabri":fabri
                    }

                    fre[f"Scan{o}"] = result
                except AttributeError:
                    print('Cod: 703')
                    
                    return "Network Erro 02 703"

        with open('return/ips.json', 'w') as json_file:
            json.dump(fre, json_file, indent=4)
            json_file.close()
    except PermissionError:
        print('Cod: 359')

hg = IpScanNetwork('192.168.0.1', '192.168.0.255', "fast")
print(hg)
