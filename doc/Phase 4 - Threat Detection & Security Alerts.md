## 1. Overview

In this phase, I simulated controlled security activities and developed detection searches in Splunk Enterprise to identify suspicious authentication attempts and network reconnaissance.

Two detection scenarios were implemented:

- SSH Brute Force Detection
- Network Port Scan Detection

Both scenarios were investigated using Splunk Search Processing Language (SPL), and scheduled alerts were configured to detect matching security events.

## 2. Tools & Technologies

| Tool | Purpose |
|---|---|
| Kali Linux | Security testing and traffic generation |
| Nmap | Network port scanning |
| pfSense | Firewall traffic logging |
| Splunk Enterprise | Threat detection and security alerts |
| SPL | Security event analysis |

## 3. Detection 1 — SSH Brute Force

### Step 1 — Generate Failed SSH Authentication Events

Repeated failed SSH authentication attempts were generated in the authorized lab environment.

The events were collected in Splunk under the `linux_security` index.

### Step 2 — Search Failed SSH Logins

Open Splunk Enterprise → Search & Reporting.

Run:

```spl
index=linux_security host=kali "Failed password"
```

### Step 3 — Analyze Failed Login Attempts

```spl
index=linux_security host=kali "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count as failed_attempts by src_ip
| where failed_attempts >= 5
| sort - failed_attempts
```

<img width="1297" height="407" alt="image" src="https://github.com/user-attachments/assets/29024432-763d-4473-b6fb-1f961969620b" />


**Observed Results:**

| Source IP | Failed Attempts |
|---|---:|
| 192.168.56.1 | 11 |

The search identified repeated failed SSH authentication attempts originating from the same source IP.

### Step 4 — Configure SSH Brute Force Alert

In Splunk:

1. Run the SSH detection search.
2. Select **Save As → Alert**.
3. Name the alert `SSH Brute Force Detection`.
4. Set the alert type to **Scheduled**.
5. Configure the alert to trigger when matching results are returned.
6. Save the alert.

<img width="975" height="272" alt="image" src="https://github.com/user-attachments/assets/a16ab27b-14db-4d8e-8083-6ff5b10720de" />
<img width="975" height="441" alt="image" src="https://github.com/user-attachments/assets/8e9d9234-6c75-401e-8c0a-2e164370cb88" />
<img width="975" height="161" alt="image" src="https://github.com/user-attachments/assets/d6ad8563-7a88-4db3-a7cb-50a5e493a2ef" />


**Result:** The SSH Brute Force alert successfully triggered during the lab.

## 4. Detection 2 — Network Port Scanning

### Step 1 — Perform an Authorized Nmap Scan

From Kali Linux, run:

```bash
sudo nmap -sS -Pn -p 21,22,23,80,445,3306 10.6.6.11
```

<img width="975" height="581" alt="image" src="https://github.com/user-attachments/assets/52fc266f-593a-44cd-97c0-7c1b01d95b0f" />


The scan targeted six TCP ports on the authorized lab system.

**Observed Results:** All six tested ports were reported as open by Nmap.

### Step 2 — Search pfSense Firewall Logs

Open Splunk Search & Reporting.

```spl
index=pfsense sourcetype="pfsense:filterlog"
```

### Step 3 — Detect Multiple Destination Ports

```spl
index=pfsense sourcetype="pfsense:filterlog"
| stats count as total_events dc(dest_port) as unique_ports by src_ip dest_ip
| where unique_ports >= 5
| sort - unique_ports
```

<img width="1268" height="920" alt="image" src="https://github.com/user-attachments/assets/44149379-aeee-4099-801a-fe2d7a65448e" />


This detection identifies source-destination pairs communicating across five or more unique destination ports within the selected search time range.

### Step 4 — Investigate the Scan

```spl
index=pfsense sourcetype="pfsense:filterlog" src_ip="10.0.0.2" dest_ip="10.6.6.11"
| stats count as total_events dc(dest_port) as unique_ports by src_ip dest_ip
```

**Observed Results:**

| Source IP | Destination IP | Total Events | Unique Ports |
|---|---|---:|---:|
| 10.0.0.2 | 10.6.6.11 | 27 | 6 |

<img width="975" height="337" alt="image" src="https://github.com/user-attachments/assets/2524bb7e-eefd-4ded-9147-7589fddd5516" />

The firewall events were consistent with the controlled Nmap scanning activity.

### Step 5 — Configure Network Port Scan Alert

In Splunk:

1. Run the network port scan detection query.
2. Select **Save As → Alert**.
3. Name the alert `Network Port Scan Detection`.
4. Select **Scheduled**.
5. Configure the alert to trigger when results are returned.
6. Save the alert.

<img width="975" height="348" alt="image" src="https://github.com/user-attachments/assets/9b9b4250-cad0-475b-bc39-a3015b4bcb2c" />


**Result:** The Network Port Scan alert successfully triggered during the lab.

## 5. Detection Results

| Detection | Source IP | Result | Status |
|---|---|---|---|
| SSH Brute Force | 192.168.56.1 | 28 failed attempts | Alert Triggered |
| Network Port Scan | 10.0.0.2 | 6 destination ports, 27 events | Alert Triggered |

Both detections were generated through controlled security testing within the lab.

**Detection Limitations:** The example searches use count-based thresholds across the selected Splunk time range. Production detections should include appropriate time windows, baselines, and false-positive tuning.

<img width="975" height="160" alt="image" src="https://github.com/user-attachments/assets/2b2fa1fd-4334-4db1-a659-b130c5974265" />


## 6. Skills Learned

- SSH authentication monitoring
- Network reconnaissance detection
- Nmap security testing
- Splunk Search Processing Language (SPL)
- Scheduled security alerts
- Security event investigation
- Detection rule development

---


