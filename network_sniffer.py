from scapy.all import *

print("Basic Network Sniffer Started...")
def packet_callback(packet):
    print(packet.summary())

sniff(prn=packet_callback, count=5)