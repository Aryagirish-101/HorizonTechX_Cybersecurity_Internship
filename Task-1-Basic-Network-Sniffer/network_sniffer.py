from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from collections import Counter
from datetime import datetime
import argparse
import csv
import os
import sys


# ============================================================
# Configuration
# ============================================================

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "network_traffic.csv")

os.makedirs(LOG_DIR, exist_ok=True)


# ============================================================
# Command-line arguments
# ============================================================

parser = argparse.ArgumentParser(
    description="Network Traffic Analyzer - Capture and analyze IP traffic."
)

parser.add_argument(
    "--protocol",
    choices=["ALL", "TCP", "UDP", "ICMP"],
    default="ALL",
    help="Protocol to monitor (default: ALL)"
)

parser.add_argument(
    "--count",
    type=int,
    default=10,
    help="Number of matching packets to capture (default: 10)"
)

args = parser.parse_args()

if args.count <= 0:
    print("Error: packet count must be greater than 0.")
    sys.exit(1)


# ============================================================
# Runtime statistics
# ============================================================

packet_count = 0
protocol_stats = Counter()


# ============================================================
# CSV log initialization
# ============================================================

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "source_ip",
            "destination_ip",
            "protocol",
            "source_port",
            "destination_port"
        ])


# ============================================================
# Display header
# ============================================================

print("=" * 65)
print("              NETWORK TRAFFIC ANALYZER")
print("=" * 65)
print(f"Protocol : {args.protocol}")
print(f"Packets  : Capturing {args.count} matching packets")
print("Press Ctrl+C to stop")
print("=" * 65)


# ============================================================
# Packet processing
# ============================================================

def packet_callback(packet):
    global packet_count

    # Ignore non-IP packets
    if not packet.haslayer(IP):
        return

    # --------------------------------------------------------
    # Identify protocol
    # --------------------------------------------------------

    if packet.haslayer(TCP):
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"
        source_port = "-"
        destination_port = "-"

    else:
        protocol = "OTHER"
        source_port = "-"
        destination_port = "-"

    # --------------------------------------------------------
    # Apply protocol filter
    # --------------------------------------------------------

    if args.protocol != "ALL" and protocol != args.protocol:
        return

    # --------------------------------------------------------
    # Update statistics
    # --------------------------------------------------------

    packet_count += 1
    protocol_stats[protocol] += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    # --------------------------------------------------------
    # Display packet information
    # --------------------------------------------------------

    print("\n" + "-" * 65)
    print(f"Timestamp        : {timestamp}")
    print(f"Packet            : #{packet_count}")
    print(f"Source IP         : {source_ip}")
    print(f"Destination IP    : {destination_ip}")
    print(f"Protocol          : {protocol}")
    print(f"Source Port       : {source_port}")
    print(f"Destination Port  : {destination_port}")

    # --------------------------------------------------------
    # Save packet to CSV log
    # --------------------------------------------------------

    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            source_ip,
            destination_ip,
            protocol,
            source_port,
            destination_port
        ])

    # --------------------------------------------------------
    # Stop after requested number of matching packets
    # --------------------------------------------------------

    if packet_count >= args.count:
        raise KeyboardInterrupt


# ============================================================
# Start packet capture
# ============================================================

try:

    sniff(
        prn=packet_callback,
        store=False
    )

except KeyboardInterrupt:
    print("\n\nCapture completed/stopped.")

except PermissionError:
    print("\nError: Administrator/root privileges are required.")
    sys.exit(1)

except Exception as error:
    print(f"\nCapture error: {error}")
    sys.exit(1)


# ============================================================
# Capture summary
# ============================================================

print("\n" + "=" * 65)
print("                    CAPTURE SUMMARY")
print("=" * 65)

print(f"Total captured : {packet_count}")
print(f"Log file       : {LOG_FILE}")

print("\nProtocol Statistics:")

if protocol_stats:

    for protocol, count in protocol_stats.items():
        print(f"  {protocol:<10}: {count}")

else:
    print("  No matching packets captured.")

print("=" * 65)
print("Network monitoring session completed.")
print("=" * 65)