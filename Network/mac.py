from getmac import getmac
from getmac import get_mac_address
from mac_vendor_lookup import MacLookup
eth_mac = get_mac_address(interface="eth0")
win_mac = get_mac_address(interface="Ethernet 3")
ip_mac = get_mac_address(ip="192.168.0.103")
ip6_mac = get_mac_address(ip6="::1")
host_mac = get_mac_address(hostname="localhost")
updated_mac = get_mac_address(ip="10.0.0.1", network_request=True)
getmac.PORT = 44444  
mac = getmac.get_mac_address(ip="192.168.0.103", network_request=True)
fabri = MacLookup().lookup(str(mac))
print(mac)
print(fabri)