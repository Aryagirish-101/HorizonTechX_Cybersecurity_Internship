from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

print("Starting Basic Network Sniffer...\n")

def packet_callback(packet):
    if packet.haslayer(IP):
        print("-" * 50)
        print("Source IP      :", packet[IP].src)
        print("Destination IP :", packet[IP].dst)

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

sniff(prn=packet_callback, count=5)