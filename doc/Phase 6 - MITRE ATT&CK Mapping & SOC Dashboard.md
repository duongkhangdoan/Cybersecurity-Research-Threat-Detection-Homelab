## 1. Overview

In this phase, I mapped simulated security activities to the MITRE ATT&CK framework and developed a SOC monitoring dashboard using Splunk Enterprise.

The dashboard provides visibility into SSH brute-force attempts and network port scanning activity, including source IP addresses, event counts, MITRE ATT&CK techniques, and severity levels.

## 2. MITRE ATT&CK Mapping

| Detection | MITRE Technique | Tactic | Severity |
|---|---|---|---|
| SSH Brute Force | T1110 — Brute Force | Credential Access | High |
| Network Port Scan | T1046 — Network Service Discovery | Discovery | Medium |

The severity levels were assigned for this educational lab and do not represent production risk ratings.

## 3. Detection 1 — SSH Brute Force

Open **Splunk Enterprise → Search & Reporting**.

Run the following SPL query:

```spl
index=linux_security host=kali "Failed password"
| rex field=_raw "from (?<src_ip>\d+\.\d+\.\d+\.\d+)"
| stats count as failed_attempts by src_ip
| where failed_attempts >= 5
| eval detection="SSH Brute Force"
| eval mitre_technique="T1110"
| eval mitre_tactic="Credential Access"
| eval severity="High"
| table detection src_ip failed_attempts mitre_technique mitre_tactic severity
```

<img width="975" height="272" alt="image" src="https://github.com/user-attachments/assets/6b1fb8a3-a8a4-4090-917a-577aef9be8f1" />

**Observed Result:**

- Source IP: `192.168.56.1`
- Failed Attempts: 28
- MITRE ATT&CK: T1110
- Severity: High

The query identifies repeated SSH authentication failures and assigns MITRE ATT&CK classification fields.

## 4. Detection 2 — Network Port Scan

Run the following SPL query:

```spl
index=pfsense sourcetype="pfsense:filterlog"
| stats count as total_events dc(dest_port) as unique_ports by src_ip dest_ip
| where unique_ports >= 5
| eval detection="Network Port Scan"
| eval mitre_technique="T1046"
| eval mitre_tactic="Discovery"
| eval severity="Medium"
| table detection src_ip dest_ip total_events unique_ports mitre_technique mitre_tactic severity
```

<img width="975" height="346" alt="image" src="https://github.com/user-attachments/assets/b38bde87-5fdf-4e2e-92eb-c48584a5bbb2" />

**Observed Result:**

- Source IP: `10.0.0.2`
- Destination IP: `10.6.6.11`
- Total Events: 27
- Unique Ports: 6
- MITRE ATT&CK: T1046
- Severity: Medium

The query identifies network connections involving multiple destination ports and maps the activity to Network Service Discovery.

## 5. Create the SOC Dashboard

### Step 1 — Create Dashboard

1. Open **Splunk Enterprise → Dashboards**.
2. Select **Create New Dashboard**.
3. Enter the dashboard name:

   `SOC Threat Detection & MITRE ATT&CK`

4. Select **Classic Dashboard**.
5. Save the dashboard.

### Step 2 — Add SSH Brute Force Panel

1. Open **Search & Reporting**.
2. Run the SSH Brute Force SPL query from Section 3.
3. Select **Save As → Dashboard Panel**.
4. Choose the existing SOC dashboard.
5. Set the panel title to `SSH Brute Force Detection`.
6. Select **Statistics Table** as the visualization.
7. Save.

### Step 3 — Add Network Port Scan Panel

1. Run the Network Port Scan SPL query from Section 4.
2. Select **Save As → Dashboard Panel**.
3. Choose the existing SOC dashboard.
4. Set the panel title to `Network Port Scan Detection`.
5. Select **Statistics Table**.
6. Save.

## 6. Dashboard Results

The completed dashboard displays two security detection panels.

| Panel | Information Displayed |
|---|---|
| SSH Brute Force Detection | Source IP, failed attempts, T1110, severity |
| Network Port Scan Detection | Source IP, destination IP, event count, unique ports, T1046, severity |

The dashboard allows security analysts to review simulated threats and their MITRE ATT&CK classifications in a centralized interface.


<img width="975" height="406" alt="image" src="https://github.com/user-attachments/assets/ecd7d88d-008b-4dfe-8473-62880bfe4d14" />

## 7. Skills Learned

- MITRE ATT&CK mapping
- SPL detection engineering
- SOC dashboard development
- Security event correlation
- Threat classification
- Security monitoring and visualization

---
