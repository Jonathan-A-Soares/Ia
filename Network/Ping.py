import os
import socket
from icmplib import ping, multiping, traceroute, resolve, Host, Hop
import json
import functools
from ipaddress import IPv4Address
import datetime
xy = datetime.datetime.now()

try:
    dir = 'return'
    os.makedirs(dir)
except FileExistsError:
    print("Cod: 551")

def PingNetwork(Endereco):

    hos = ping(Endereco, count=32, interval=0.5, timeout=1)

    print(f"IP:{hos.address}")
    print(f"Min:{hos.min_rtt}ms")
    print(f"Med:{hos.avg_rtt}ms")
    print(f"Max:{hos.max_rtt}ms")
    print(f"Enviados:{hos.packets_sent}")
    print(f"Recebido:{hos.packets_received}")
    print(f"Perda:{hos.packet_loss}")
    print(f"Host:{hos.is_alive}")
    print(xy.strftime("%X"))
    print(xy.strftime("%x"))

    Result = {
        "Domain": Endereco,
        "Ip": hos.address,
        "Ping-Min": hos.min_rtt,
        "Ping-Avg": hos.avg_rtt,
        "Ping-Max": hos.max_rtt,
        "PacketsSent": hos.packets_sent,
        "PacketsReceived": hos.packets_received,
        "Loss": hos.packet_loss,
        "Accessible host": hos.is_alive,
        "Date": xy.strftime("%x"),
        "hora": xy.strftime("%X")
        

    }
    with open('return/Ping.json', 'w') as json_file:
        json.dump(Result, json_file, indent=4)
        json_file.close()
    return "Network Ok 01"


ip = PingNetwork('192.168.0.1')
print(ip)
