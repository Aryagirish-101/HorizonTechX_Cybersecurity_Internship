# Network Intrusion Detection System (NIDS)

> A Python-based network security monitoring tool that captures network traffic, analyzes protocols and ports, detects potentially suspicious activity, and generates timestamped security events.

## Overview

The **Network Intrusion Detection System (NIDS)** is a lightweight security monitoring project developed as part of the HorizonTechX Cybersecurity Internship.

The system uses **Scapy** to inspect network packets and applies rule-based detection to identify traffic associated with commonly targeted network services.

The project demonstrates a basic **SOC-style monitoring workflow** from packet capture and analysis to alert generation and security event logging.

## Objectives

- Monitor network traffic in real time
- Analyze source and destination IP addresses
- Identify network protocols
- Inspect TCP destination ports
- Detect potentially suspicious service traffic
- Generate timestamped security alerts
- Maintain security event logs
- Document detected security events

## Key Features

### 🔍 Real-Time Packet Monitoring
Captures live network packets using Scapy without storing the complete packet capture in memory.

### 🌐 Network Traffic Analysis
Extracts:

- Source IP address
- Destination IP address
- Network protocol
- TCP destination port

### 🚨 Rule-Based Detection
The system checks traffic against predefined service-port rules.

| Service | Port | Risk Context |
|---|---:|---|
| FTP | 21 | Unencrypted file transfer |
| SSH | 22 | Remote administration |
| Telnet | 23 | Insecure remote access |
| RDP | 3389 | Remote desktop access |

> Detection of a monitored port does not automatically mean an attack has occurred. Alerts require further investigation and validation.

### 📝 Security Event Logging

Detected events are recorded with timestamps in:

```text
logs/security_events.log
```

## Detection Workflow

```text
Network Traffic
       ↓
Packet Capture
       ↓
IP & Protocol Analysis
       ↓
Port Inspection
       ↓
Detection Rules
       ↓
Security Alert
       ↓
Event Logging
       ↓
Further Investigation
```

## Project Structure

```text
Task-4-Network-Intrusion-Detection/
│
├── nids.py
├── README.md
├── INCIDENT_REPORT.md
├── requirements.txt
│
├── logs/
│   └── security_events.log
│
└── screenshots/
    ├── nids-running.png
    └── detection-alert.png
```

## Technologies

- **Python 3**
- **Scapy**
- **Kali Linux**
- **VS Code**
- **Git**
- **GitHub**

## Security Concepts Demonstrated

- Network Traffic Analysis
- Packet Inspection
- TCP/IP Fundamentals
- Port-Based Detection
- Rule-Based Intrusion Detection
- Security Event Logging
- Incident Documentation
- Basic SOC Monitoring Workflow

## Example Detection

When monitored traffic is detected, the system generates an alert similar to:

```text
[ALERT] Suspicious SSH traffic detected |
10.0.2.15 -> 10.0.2.20:22
```

The event is also recorded with a timestamp in the security log.

## Incident Response Approach

When an alert is generated:

1. Validate the source and destination systems.
2. Determine whether the traffic is authorized.
3. Review related logs and network activity.
4. Check for repeated or abnormal connection attempts.
5. Assess the potential security impact.
6. Apply appropriate defensive controls if malicious activity is confirmed.
7. Document the investigation and response.

## Limitations

This project is intentionally lightweight and rule-based. It does not replace an enterprise IDS/IPS or SIEM platform.

Future improvements could include:

- Signature-based detection
- IP reputation checks
- Port-scan detection
- Threshold-based alerts
- JSON/CSV event reporting
- Dashboard integration
- SIEM integration
- Machine-learning-based anomaly detection

## Learning Outcomes

This project provided practical experience with:

- Python-based security automation
- Scapy packet processing
- Network traffic analysis
- Detection rule development
- Security alert generation
- Event logging
- Incident documentation
- Git/GitHub project management

## Disclaimer

This project is developed **strictly for educational purposes and authorized cybersecurity testing**.

Only monitor networks and systems for which you have explicit permission.

## Author

**Arya Girishkumar**

B.Sc. Computer Science with Cyber Security  
Cybersecurity Enthusiast