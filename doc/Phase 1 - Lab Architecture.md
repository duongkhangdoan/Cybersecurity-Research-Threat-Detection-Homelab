# Phase 1 — Lab Architecture & Environment Setup

## 1. Overview

This phase focuses on preparing a virtual cybersecurity lab for network monitoring, threat detection, and security analysis.

Oracle VirtualBox is used to host Kali Linux, Ubuntu Linux, and pfSense, creating an environment for simulating and investigating security events using Splunk Enterprise.

## 2. Lab Requirements

**Recommended Hardware:**
- 16 GB RAM minimum (32 GB recommended)
- 100 GB available storage
- CPU with virtualization support
- Internet connection for software installation

**Software & Tools:**

| Tool | Purpose |
|---|---|
| Oracle VirtualBox | Virtualization platform |
| Kali Linux | Security testing and Nmap scanning |
| Ubuntu Linux | Splunk SIEM and Python analytics |
| pfSense | Firewall and network traffic logging |
| Splunk Enterprise | Security monitoring and detection |
| Python 3 | Security log analysis |

## 3. Lab Architecture

The environment consists of three main virtual machines.

**Kali Linux — Security Testing**
- Perform authorized network scanning using Nmap.
- Simulate failed SSH authentication attempts.
- Generate security events for analysis.

**pfSense — Network Firewall**
- Monitor network traffic.
- Apply firewall rules.
- Forward firewall logs to Splunk.

**Ubuntu Linux — Splunk SIEM**
- Collect and analyze security logs.
- Develop SPL queries and detection alerts.
- Create SOC dashboards.
- Perform Python-based security analytics.

## 4. Network Configuration

The lab uses NAT and Host-Only networking for internet connectivity and controlled security testing.

| Network Interface | IP Address | Purpose |
|---|---|---|
| Kali eth0 | 10.0.0.2/24 | NAT Network |
| Kali eth1 | 192.168.56.105/24 | Host-Only Network |
| Lab Target | 10.6.6.11 | Nmap scanning target |

Network adapter configuration and connectivity testing are covered in Phase 2.

## 5. Environment Setup

1. Install Oracle VirtualBox.
2. Create Kali Linux, Ubuntu Linux, and pfSense virtual machines.
3. Allocate appropriate CPU, RAM, and storage resources.
4. Install Splunk Enterprise on Ubuntu Linux.
5. Start Splunk and access the web interface at `http://localhost:8000`.
6. Verify that all virtual machines boot successfully.

**Basic Verification Commands:**

```bash
# Check network interfaces
ip -br addr

# Check routing table
ip route

# Check Splunk status on Ubuntu
sudo /opt/splunk/bin/splunk status
```

## 6. Expected Results

By the end of Phase 1:

- Virtual machines are installed and operational.
- Splunk Enterprise is accessible.
- Kali Linux is ready for network security testing.
- pfSense is prepared for firewall monitoring.
- The environment is ready for network configuration.

## 7. Skills Learned

- Virtualization and VM management
- Linux system administration
- Basic network architecture
- Firewall infrastructure
- SIEM environment preparation

---

## Next Phase

[Phase 2 — Network Configuration & Connectivity](Phase-2-Network-Configuration.md)
