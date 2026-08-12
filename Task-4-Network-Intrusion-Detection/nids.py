from datetime import datetime
from pathlib import Path

from scapy.all import sniff, IP, TCP, UDP, ICMP


BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "security_events.log"

MONITORED_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    3389: "RDP",
}


def log_event(message):
    LOG_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")


def analyze_packet(packet):
    if not packet.haslayer(IP):
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    if packet.haslayer(TCP):
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

        print(
            f"{source_ip} -> {destination_ip} | "
            f"{protocol} | {source_port} -> {destination_port}"
        )

        if destination_port in MONITORED_PORTS:
            service = MONITORED_PORTS[destination_port]

            alert = (
                f"Potentially suspicious {service} traffic detected | "
                f"{source_ip}:{source_port} -> "
                f"{destination_ip}:{destination_port}"
            )

            print(f"[ALERT] {alert}")
            log_event(alert)

    elif packet.haslayer(UDP):
        print(
            f"{source_ip} -> {destination_ip} | UDP"
        )

    elif packet.haslayer(ICMP):
        print(
            f"{source_ip} -> {destination_ip} | ICMP"
        )


def main():
    LOG_DIR.mkdir(exist_ok=True)

    print("=" * 65)
    print("          NETWORK INTRUSION DETECTION SYSTEM")
    print("=" * 65)
    print("Status : Monitoring")
    print("Mode   : Rule-Based Detection")
    print("Press Ctrl+C to stop.")
    print("-" * 65)

    try:
        sniff(iface="lo", prn=analyze_packet, store=False)

    except PermissionError:
        print("\n[ERROR] Root privileges are required.")
        print("Run the program using: sudo python3 nids.py")

    except KeyboardInterrupt:
        print("\n\n[INFO] Monitoring stopped.")

    except Exception as error:
        print(f"\n[ERROR] {error}")


if __name__ == "__main__":
    main()