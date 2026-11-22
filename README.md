### Security Monitoring | Threat Detection | MITRE ATT&CK | Python Security Analytics

## Project Overview

This project demonstrates the design and implementation of a virtual cybersecurity homelab focused on network security monitoring, threat detection, threat intelligence analysis, and security log analytics.

The lab simulates common security activities, including SSH brute-force attempts and network port scanning, within an authorized virtual environment.

Using Splunk Enterprise, pfSense, Kali Linux, Nmap, and Python, the project demonstrates how security analysts collect, investigate, and correlate security events to identify potentially suspicious activities.

The project also incorporates threat intelligence enrichment using VirusTotal and AbuseIPDB, along with MITRE ATT&CK mapping to classify detected behaviors.

**Project Objectives**

- Build a virtual network environment for security monitoring and analysis.
- Collect and analyze firewall and Linux authentication logs using Splunk SIEM.
- Simulate and investigate SSH brute-force attempts and network port scanning.
- Develop SPL searches and scheduled alerts for suspicious activities.
- Investigate public IP addresses using VirusTotal and AbuseIPDB.
- Enrich Splunk events with threat intelligence using CSV lookups.
- Map security detections to MITRE ATT&CK techniques.
- Develop security dashboards for monitoring and investigation.
- Analyze exported security logs using Python, pandas, and Matplotlib.
- Document findings through a SOC investigation report.

---

## Technologies & Tools

| Category | Technologies |
|---|---|
| Virtualization | Oracle VirtualBox |
| Operating Systems | Kali Linux, Ubuntu Linux |
| Firewall & Networking | pfSense, TCP/IP, Virtual Networks |
| SIEM | Splunk Enterprise |
| Network Security Testing | Nmap, SSH |
| Threat Intelligence | VirusTotal, AbuseIPDB |
| Threat Detection | SPL, Scheduled Alerts |
| Security Framework | MITRE ATT&CK |
| Programming & Analytics | Python, pandas, Matplotlib |
| Reporting | CSV, Markdown, Security Visualizations |

---

## Lab Architecture

The homelab uses virtual machines connected through an isolated lab network, with pfSense providing firewall functionality and network traffic logging.

**Main Components**

**Kali Linux**

- Generates authorized network scanning activity using Nmap.
- Provides a controlled environment for security testing.
- Connects to the virtual lab network.

**Linux SSH Target**

- Provides SSH authentication events for detection exercises.
- Generates failed login records for security investigation.

**pfSense Firewall**

- Monitors and logs network traffic.
- Records connections between source and destination IP addresses.
- Provides firewall logs for network security analysis.

**Splunk Enterprise**

- Centralizes security events from the lab.
- Supports SPL-based security searches and detection rules.
- Generates scheduled security alerts.
- Provides dashboards for SOC investigation.

**Python Analytics Environment**

- Processes exported Splunk security logs.
- Analyzes source IP addresses, destination IP addresses, and destination ports.
- Identifies potential network scanning activity.
- Generates security visualizations and reports.

---

## Project Implementation — 7 Phases

### Phase 1 — Lab Architecture & Environment Setup

Set up the virtual machines and identify the network architecture, security monitoring components, and required tools.

**Skills:** Virtualization, Linux Administration, Network Architecture



### Phase 2 — Network Configuration & Connectivity

Configure the Kali Linux network interfaces, virtual networks, and communication between lab systems.

Validate connectivity and routing before beginning security testing.

**Skills:** TCP/IP, Routing, Network Troubleshooting



### Phase 3 — Security Log Collection

Collect Linux SSH authentication logs and pfSense firewall events in Splunk Enterprise.

Validate that security events are searchable and contain the information needed for investigation.

**Skills:** SIEM, Log Collection, Security Event Analysis



### Phase 4 — Threat Detection & Security Alerts

Simulate authorized SSH authentication failures and network port scanning.

Use SPL searches to identify suspicious activity and configure scheduled alerts.

**Skills:** Threat Detection, SPL, SOC Monitoring, Network Reconnaissance


### Phase 5 — Threat Intelligence Enrichment

Investigate public IP addresses using VirusTotal and AbuseIPDB.

Create a CSV threat intelligence lookup and correlate reputation data with network security events in Splunk.

**Skills:** Threat Intelligence, IOC Analysis, Security Enrichment



### Phase 6 — MITRE ATT&CK Mapping & SOC Dashboard

Classify detected security behaviors using MITRE ATT&CK techniques.

Create a Splunk dashboard displaying SSH brute-force and network port scan detection results.

**Skills:** MITRE ATT&CK, Security Dashboards, Detection Engineering



### Phase 7 — Python Security Log Analytics & Reporting

Export network security events from Splunk and analyze them using Python.

Use pandas to summarize traffic activity and Matplotlib to generate visualizations.

Document investigation findings in a SOC security report.

**Skills:** Python, pandas, Data Analytics, Security Reporting



---

## Security Detection Results

### SSH Brute-Force Detection

A controlled SSH authentication test generated multiple failed login events.

Splunk detected repeated authentication failures and produced a scheduled security alert.

**Detection Summary**

- Detection: SSH Brute Force
- Failed Attempts: 28
- Source IP: 192.168.56.1
- MITRE ATT&CK: T1110 — Brute Force
- Tactic: Credential Access
- Severity: High

### Network Port Scan Detection

An authorized Nmap scan was conducted against a virtual lab target.

The scan generated firewall events that were collected and analyzed using Splunk.

**Detection Summary**

- Detection: Network Port Scan
- Source IP: 10.0.0.2
- Destination IP: 10.6.6.11
- Unique Destination Ports: 6
- Total Matching Events: 27
- MITRE ATT&CK: T1046 — Network Service Discovery
- Tactic: Discovery
- Severity: Medium

### Threat Intelligence Investigation

A public IP address was investigated using VirusTotal and AbuseIPDB.

**Investigated IP:** 91.189.91.112

| Threat Intelligence Source | Result |
|---|---|
| VirusTotal | 0/92 detections |
| AbuseIPDB | 0% abuse confidence |
| Assessment | Likely benign based on available reputation data |

The results were recorded in a CSV lookup and integrated into Splunk for event enrichment.

The reputation results represent a point-in-time assessment and do not guarantee that the IP address is safe.

---

## Python Security Analytics Results

A Python script was developed to analyze exported network security logs.

**Analysis Results**

| Metric | Result |
|---|---:|
| Total Security Events | 2,709 |
| Unique Source IPs | 2 |
| Unique Destination IPs | 276 |
| Potential Port Scan Findings | 1 |
| Destination Ports in Scan | 6 |

The analysis generated visualizations for:

- Top source IP addresses by event volume.
- Most frequently observed destination ports.
- Network traffic activity over time.

The detection is based on a unique-port threshold within the exported dataset, rather than a production-grade time-window correlation rule.

---

## Key Skills Developed

This project provided hands-on experience in:

- SIEM deployment and security event monitoring.
- Linux authentication and firewall log investigation.
- Network traffic analysis and port scan detection.
- Writing SPL queries and configuring security alerts.
- Threat intelligence research and IOC enrichment.
- MITRE ATT&CK technique mapping.
- Security dashboard development.
- Python-based security data analytics.
- SOC investigation and technical documentation.

---

## Security & Ethical Considerations

All simulated security testing was performed within an authorized virtual lab environment.

The project is intended for cybersecurity education, defensive security monitoring, and controlled security research.

No unauthorized systems were intentionally targeted.

---

## Future Improvements

Potential future enhancements include:

- Time-window-based detection and correlation.
- Automated threat intelligence API integration.
- Additional network traffic analysis using Wireshark.
- Improved alert tuning to reduce false positives.
- Automated incident reporting and security analytics.

---

