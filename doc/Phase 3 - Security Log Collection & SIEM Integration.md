## 1. Overview

This phase focuses on centralizing security logs from Linux systems and the pfSense firewall into Splunk Enterprise.

The objective is to establish a security monitoring pipeline that allows SOC analysts to search, investigate, and correlate authentication and network events.

## 2. Tools & Technologies

| Tool | Purpose |
|---|---|
| Splunk Enterprise | Centralized SIEM and log analysis |
| Splunk Universal Forwarder | Forward Linux security logs |
| rsyslog / Syslog | Collect and transport syslog events |
| pfSense | Generate network firewall logs |
| Kali Linux | Generate SSH authentication events |
| Ubuntu Linux | Host Splunk Enterprise |

## 3. Log Collection Architecture

The environment uses two main security data sources.

**Linux Authentication Logs**

`Kali Linux → Linux Log Forwarding → Splunk Enterprise`

Used to monitor:
- Failed SSH authentication attempts.
- Source IP addresses.
- Target usernames.
- Authentication event frequency.

**pfSense Firewall Logs**

`pfSense → Syslog Collection → Splunk Enterprise`


Used to monitor:
- Source and destination IP addresses.
- Network connection attempts.
- Destination ports.
- Firewall traffic events.

## 4. Configure Linux Security Log Collection

### Step 1 — Verify SSH Logging

On Kali Linux, check the SSH service:

```bash
sudo systemctl status ssh
```

Inspect authentication events:

```bash
sudo journalctl -u ssh --no-pager -n 30
```

Depending on the Linux logging configuration, authentication events may also be stored in `/var/log/auth.log`.

<img width="734" height="399" alt="image" src="https://github.com/user-attachments/assets/3df27b24-7ff4-4468-b65c-930e55e2ab8d" />

### Step 2 — Forward Linux Logs to Splunk

Configure the existing Linux log forwarding mechanism to send authentication events to Splunk Enterprise.

If using Splunk Universal Forwarder, an example monitored file configuration is:

```ini
[monitor:///var/log/auth.log]
disabled = false
index = linux_security
sourcetype = linux_secure
```

The monitored path, sourcetype, receiving address, and forwarding permissions must match the actual deployment.

### Step 3 — Verify Events in Splunk

Open **Splunk Enterprise → Search & Reporting**.

Run:

```spl
index=linux_security host=kali
```

<img width="1294" height="928" alt="image" src="https://github.com/user-attachments/assets/2b6a4165-57fc-4d27-8742-ee213d4885fd" />


Filter failed SSH authentication attempts:

```spl
index=linux_security host=kali "Failed password"
```

<img width="1276" height="739" alt="image" src="https://github.com/user-attachments/assets/da5c553c-e01f-4384-8765-fcafcbdce0f4" />


**Expected Result:** Splunk displays Linux authentication events, including failed SSH login attempts.

## 5. Configure pfSense Firewall Log Collection

### Step 1 — Enable Remote Logging

In the pfSense web interface:

1. Navigate to **Status → System Logs → Settings**.
2. Locate the remote logging configuration.
3. Enable remote syslog forwarding.
4. Enter the configured syslog collector address and port.
5. Select firewall events for forwarding.
6. Save the configuration.

### Step 2 — Verify Firewall Logs in Splunk

Open Splunk Search & Reporting.

Run:

```spl
index=pfsense sourcetype="pfsense:filterlog"
```

<img width="1291" height="922" alt="image" src="https://github.com/user-attachments/assets/eb935d71-244a-463b-a516-d1f4df79f03c" />


Review network traffic fields:

```spl
index=pfsense sourcetype="pfsense:filterlog"
| table _time src_ip dest_ip src_port dest_port
```

<img width="1286" height="918" alt="image" src="https://github.com/user-attachments/assets/d777f2a2-7cd4-4595-83b7-e8c9e9816527" />


**Expected Result:** Splunk displays pfSense firewall events with source and destination information.

## 6. Validate Security Log Collection

### Linux Authentication Events

```spl
index=linux_security host=kali "Failed password"
| stats count by host
```

<img width="1288" height="329" alt="image" src="https://github.com/user-attachments/assets/8a0b624e-f01f-411b-94ef-2aa543f0c24e" />


### Network Firewall Events

```spl
index=pfsense sourcetype="pfsense:filterlog"
| stats count by src_ip dest_ip
| sort - count
```

<img width="1286" height="915" alt="image" src="https://github.com/user-attachments/assets/b4554f7f-98b1-4ba4-b43c-a7e90f7271a3" />


These searches confirm that Splunk can retrieve and summarize events from both security data sources.

## 7. Results

The lab successfully centralized:

- Linux SSH authentication logs in the `linux_security` index.
- pfSense firewall events in the `pfsense` index.
- Network traffic fields including `src_ip`, `dest_ip`, and `dest_port`.
- Security events for further detection and investigation.

These logs provided the foundation for SSH brute-force detection, network port scanning analysis, and SOC dashboard development.

## 8. Skills Learned

- SIEM log ingestion
- Linux authentication log monitoring
- Syslog forwarding
- Firewall log collection
- Splunk indexing and searching
- Security event analysis

---
