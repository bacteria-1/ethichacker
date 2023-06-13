import scapy.all as scapy
import sys
import time


def get_mac_address(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False, iface='wlo1')[0]

    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py router_ip target_ip")
        sys.exit(1)

    router_ip = sys.argv[1]
    target_ip = sys.argv[2]

    target_mac = get_mac_address(target_ip)
    router_mac = get_mac_address(router_ip)

    print(f"Target MAC: {target_mac}")
    print(f"Router MAC: {router_mac}")

if __name__ == "__main__":
    main()





