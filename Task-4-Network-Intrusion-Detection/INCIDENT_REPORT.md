# Network Intrusion Detection Incident Report

## 1. Incident Overview

This report documents the detection and analysis workflow of the Network Intrusion Detection System (NIDS) developed for the HorizonTechX Cybersecurity Internship.

The system monitors network traffic and generates alerts when traffic matches predefined rules associated with commonly targeted network services.

---

## 2. Detection Type

**Rule-Based Network Traffic Detection**

The NIDS analyzes network packets and checks TCP destination ports against configured detection rules.

---

## 3. Monitored Services

| Service | Port | Monitoring Purpose |
|---|---:|---|
| FTP | 21 | File transfer traffic |
| SSH | 22 | Remote administration |
| Telnet | 23 | Insecure remote access |
| RDP | 3389 | Remote desktop access |

---

## 4. Detection Process

The system follows this workflow:

```text
Packet Capture
      ↓
Source/Destination IP Extraction
      ↓
Protocol Identification
      ↓
TCP Port Inspection
      ↓
Rule Comparison
      ↓
Alert Generation
      ↓
Security Event Logging