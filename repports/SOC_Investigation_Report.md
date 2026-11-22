# SOC Investigation Report

**Project:** Threat Intelligence & Network Detection Homelab  
**Investigation Type:** SSH Brute Force & Network Port Scanning  
**Environment:** VirtualBox Cybersecurity Homelab  
**Tools:** Splunk Enterprise, pfSense, Kali Linux, Nmap, VirusTotal, AbuseIPDB, Python  
**Status:** Completed — Authorized Lab Simulation

---

## 1. Executive Summary

This investigation analyzed simulated cybersecurity threats within an isolated virtual lab environment using Splunk Enterprise and Python.

Two security activities were investigated:

- Repeated SSH authentication failures.
- Network port scanning using Nmap.

Security events were collected from Linux authentication logs and pfSense firewall logs, analyzed using Splunk Search Processing Language (SPL), and mapped to the MITRE ATT&CK framework.

Threat intelligence enrichment and Python-based analytics were also performed to support the investigation.

**Outcome:** Both simulated activities were successfully detected, investigated, and documented.

## 2. Security Detection Findings

### Finding 1 — SSH Brute Force

| Field | Finding |
|---|---|
| Detection | SSH Brute Force |
| Source IP | 192.168.56.1 |
| Failed Login Attempts | 28 |
| Log Source | Kali Linux SSH Authentication |
| Splunk Index | `linux_security` |
| MITRE ATT&CK | T1110 — Brute Force |
| Tactic | Credential Access |
| Lab Severity | High |

**Investigation:**

Splunk identified 28 failed SSH authentication attempts originating from the same source IP address.

An SPL detection search was used to aggregate failed login events, and a scheduled security alert was successfully triggered.

The activity was generated intentionally to validate the detection mechanism.

**Conclusion:** The SSH brute-force detection successfully identified repeated authentication failures. The observed failures alone do not establish that an account was compromised.

### Finding 2 — Network Port Scanning

| Field | Finding |
|---|---|
| Detection | Network Port Scan |
| Source IP | 10.0.0.2 |
| Destination IP | 10.6.6.11 |
| Total Firewall Events | 27 |
| Unique Destination Ports | 6 |
| Ports Scanned | 21, 22, 23, 80, 445, 3306 |
| MITRE ATT&CK | T1046 — Network Service Discovery |
| Tactic | Discovery |
| Lab Severity | Medium |

**Investigation:**

An authorized Nmap TCP SYN scan was performed against the lab target.

```bash
sudo nmap -sS -Pn -p 21,22,23,80,445,3306 10.6.6.11
```

pfSense firewall events were collected and analyzed in Splunk.

The investigation identified 27 events involving six unique destination ports between the source and destination IP addresses.

A scheduled Network Port Scan alert was successfully triggered.

**Conclusion:** The network activity was consistent with the controlled Nmap scanning exercise. No unauthorized activity was established.

## 3. Threat Intelligence Analysis

The public IP address `91.189.91.112` was investigated using VirusTotal and AbuseIPDB.

| Source | Result |
|---|---|
| VirusTotal | 0/92 detections |
| AbuseIPDB | 0% abuse confidence score |
| Classification | Likely Benign |

A CSV lookup was created to enrich matching pfSense firewall events with threat intelligence information.

```csv
dest_ip,vt_detection,abuse_score,classification
91.189.91.112,0,0,likely_benign
```

**Assessment:** The available reputation results did not indicate known malicious activity at the time of investigation. However, a clean reputation result does not guarantee that an IP address is safe.

This IP reputation check was a separate enrichment exercise and did not establish that the IP participated in either simulated detection scenario.

## 4. Python Security Log Analysis

Security events were exported from Splunk and analyzed using Python, pandas, and Matplotlib.

**Analysis Results:**

| Metric | Result |
|---|---:|
| Total Events Analyzed | 2,709 |
| Unique Source IPs | 2 |
| Unique Destination IPs | 276 |
| Potential Port Scan Findings | 1 |

The Python script identified the following source-destination pair:

| Source IP | Destination IP | Events | Unique Ports |
|---|---|---:|---:|
| 10.0.0.2 | 10.6.6.11 | 27 | 6 |

The script also generated three visualizations:

- Top Source IP Addresses
- Top Destination Ports
- Network Security Events Over Time

The port scanning detection used a threshold of five unique destination ports across the exported dataset. This is an initial detection heuristic rather than a production-ready correlation rule.

## 5. MITRE ATT&CK Mapping

| Detection | Technique | Tactic |
|---|---|---|
| SSH Brute Force | T1110 — Brute Force | Credential Access |
| Network Port Scan | T1046 — Network Service Discovery | Discovery |

MITRE ATT&CK mapping provided a standardized way to classify the simulated security behaviors and communicate investigation findings.

## 6. Response & Recommendations

Because both activities were authorized lab simulations, no production containment or remediation was required.

Recommended improvements for future detection engineering include:

- Implement time-window-based detection thresholds.
- Tune alerts to reduce false positives.
- Add automated threat intelligence API enrichment.
- Correlate network scanning with additional endpoint and firewall evidence.
- Improve investigation reporting and detection validation.

## 7. Final Conclusion

The investigation successfully demonstrated a cybersecurity monitoring and analysis workflow involving:

- Centralized security log collection using Splunk Enterprise.
- SSH brute-force and network port scan detection.
- Scheduled security alerts.
- Threat intelligence enrichment.
- MITRE ATT&CK mapping.
- Python-based security log analysis and visualization.

This project strengthened practical skills in SOC monitoring, threat detection, network security investigation, security analytics, and technical reporting.

**Final Assessment:** Both simulated detection scenarios were successfully identified and documented. The observed activity was authorized and generated within the cybersecurity homelab.

---
