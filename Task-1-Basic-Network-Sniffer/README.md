Basic Network Sniffer

A Python-based network traffic analyzer built using Scapy. The tool captures live IP packets, identifies common network protocols, displays packet information, and records captured traffic into a CSV log for further analysis.

Project Overview

This project demonstrates practical network traffic monitoring and packet-level analysis using Python and Scapy.

The analyzer can monitor TCP, UDP, and ICMP traffic, filter packets by protocol, control the number of packets captured, and maintain a structured CSV log of captured network activity.

Features
Capture live network packets
Display source and destination IP addresses
Detect TCP, UDP, and ICMP protocols
Display source and destination ports
Filter traffic by protocol
Configure the number of packets to capture
Display timestamps for captured packets
Generate protocol statistics
Store captured traffic in CSV format
Gracefully handle capture interruption and errors
Provide command-line help and usage information
Technologies Used
Python 3
Scapy
Kali Linux
Visual Studio Code
CSV
Git & GitHub
Project Structure
Task-1-Basic-Network-Sniffer/
│
├── network_sniffer.py
├── README.md
├── requirements.txt
│
├── logs/
│   └── network_traffic.csv
│
└── screenshots/
    ├── traffic-analysis.png
    ├── tcp-filter.png
    └── udp-filter.png
Installation

Clone the repository and navigate to the project directory.

Install the required Python dependency:

pip install -r requirements.txt
Usage
Capture all supported traffic
sudo python3 network_sniffer.py --protocol ALL --count 10
Capture TCP traffic
sudo python3 network_sniffer.py --protocol TCP --count 10
Capture UDP traffic
sudo python3 network_sniffer.py --protocol UDP --count 10
Capture ICMP traffic
sudo python3 network_sniffer.py --protocol ICMP --count 5
Logging

Captured packet information is stored in:

logs/network_traffic.csv

The CSV file contains:

Timestamp
Source IP
Destination IP
Protocol
Source Port
Destination Port

This provides a persistent record that can be used for basic network traffic analysis.

Example Output
===============================================================
              NETWORK TRAFFIC ANALYZER
===============================================================


Protocol : TCP


Packets  : Capturing 10 matching packets


-----------------------------------------------------------------


Timestamp        : 2026-08-21 06:27:42


Packet            : #1


Source IP         : 10.0.2.15


Destination IP    : example.server


Protocol          : TCP


Source Port       : 58532


Destination Port  : 443
Testing

The project was tested by generating controlled network traffic and verifying:

TCP packet detection
UDP packet detection
Protocol filtering
Packet counting
Timestamp generation
CSV logging
Protocol statistics

Screenshots of successful tests are available in the screenshots/ directory.

Limitations
The tool is intended for basic educational network monitoring.
Packet visibility depends on the network interface and capture permissions.
Encrypted application payloads are not decrypted or inspected.
Some traffic, including loopback traffic, may require selecting the appropriate network interface.
Security & Ethical Use

This project is intended for educational and authorized network monitoring purposes only.

Do not capture or analyze network traffic without proper authorization. Use the tool only on systems and networks where you have permission to perform monitoring.

Author

Arya Girishkumar

B.Sc. Computer Science with Cyber Security

Aspiring SOC Analyst | Cybersecurity Professional