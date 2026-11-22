## 1. Overview

In this final phase, I exported network security logs from Splunk Enterprise and developed a Python script to analyze firewall traffic, identify potential network scanning activity, and generate security visualizations.

The analysis used pandas for log processing and Matplotlib for data visualization.

## 2. Tools & Technologies

| Tool | Purpose |
|---|---|
| Splunk Enterprise | Export network security events |
| Python 3 | Security log analysis |
| pandas | Data processing and aggregation |
| Matplotlib | Security data visualization |
| CSV | Store security logs and investigation results |

## 3. Export Security Logs from Splunk

Open **Splunk Enterprise → Search & Reporting**.

Run the following SPL query:

```spl
index=pfsense sourcetype="pfsense:filterlog"
| table _time src_ip dest_ip src_port dest_port
```

Select **Export → CSV** and save the file as:

`network_security_logs.csv`

The exported dataset contains network event timestamps, source and destination IP addresses, and port information.

## 4. Set Up Python Environment

On the Ubuntu Splunk VM, create a Python virtual environment:

```bash
python3 -m venv soc-env
source soc-env/bin/activate
```

Install the required libraries:

```bash
pip install pandas matplotlib numpy
```

Verify the exported CSV file:

```bash
cd ~/Downloads
ls -lh network_security_logs.csv
head -n 5 network_security_logs.csv
```

<img width="975" height="304" alt="image" src="https://github.com/user-attachments/assets/1e4587fa-876a-4c63-809f-d0a167371f21" />

## 5. Develop Python Security Analytics Script

Create a Python script:

```bash
nano ~/Downloads/soc_log_analysis.py
```

The script performs the following tasks:

1. Loads exported Splunk firewall logs using pandas.
2. Converts timestamps and destination ports into appropriate data types.
3. Counts total events and unique IP addresses.
4. Identifies the most active source IP addresses.
5. Analyzes frequently observed destination ports.
6. Detects source-destination pairs accessing five or more unique destination ports.
7. Exports potential port scanning findings to CSV.
8. Generates three security visualization charts.

## 6. Execute the Analysis

Run the Python script:

```bash
cd ~/Downloads
source ~/soc-env/bin/activate
python soc_log_analysis.py
```

If the virtual environment was created in another directory, activate it using its actual path.

**Observed Results:**

| Metric | Result |
|---|---:|
| Total Security Events | 2,709 |
| Unique Source IPs | 2 |
| Unique Destination IPs | 276 |
| Potential Port Scan Findings | 1 |

**Detected Network Scanning Activity:**

| Source IP | Destination IP | Events | Unique Ports |
|---|---|---:|---:|
| 10.0.0.2 | 10.6.6.11 | 27 | 6 |

The identified activity was consistent with the authorized Nmap scan performed in Phase 4.

## 7. Security Data Visualizations

The Python script generated three visualizations.

### Top Source IP Addresses

**File:** `top_source_ips.png`

Displays the most active source IP addresses based on event volume.

<img width="975" height="530" alt="image" src="https://github.com/user-attachments/assets/7dae63e3-ec31-4878-b5c5-59cbbd443a0a" />

### Top Destination Ports

**File:** `top_destination_ports.png`

<img width="975" height="527" alt="image" src="https://github.com/user-attachments/assets/98fd63a9-1b7e-4269-bfa5-fa9de2bd63b6" />

Displays the most frequently observed destination ports, including ports 443, 53, 123, and 9997.

### Network Traffic Timeline

**File:** `network_traffic_timeline.png`

<img width="975" height="510" alt="image" src="https://github.com/user-attachments/assets/238e9d12-f789-4632-a746-3f2b88be8f2c" />

Displays network security event volume over time using five-minute intervals.

These visualizations help analysts identify traffic patterns and investigate unusual activity.

## 8. SOC Investigation Findings

The analysis identified 27 firewall events involving six unique destination ports between:

- **Source:** 10.0.0.2
- **Destination:** 10.6.6.11

The activity matched the controlled network scanning exercise.

**MITRE ATT&CK Mapping:**

- Technique: T1046 — Network Service Discovery
- Tactic: Discovery

The five-port detection threshold was applied across the exported dataset. It is a basic analytical heuristic and does not establish malicious intent without additional investigation.


## 9. Skills Learned

- Python security automation
- pandas data analysis
- Firewall log processing
- Network traffic analytics
- Port scanning detection
- Matplotlib data visualization
- SOC investigation and reporting
- Security data interpretation

---

## Project Conclusion

This seven-phase homelab demonstrates an end-to-end security monitoring workflow involving virtual network infrastructure, centralized SIEM log collection, threat detection, security alerts, threat intelligence enrichment, MITRE ATT&CK mapping, and Python-based security analytics.

The project strengthened my practical skills in Security Operations, Network Security Monitoring, Threat Intelligence, and Security Research.
