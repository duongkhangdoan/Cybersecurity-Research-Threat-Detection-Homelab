

## 1. Overview

This phase focuses on configuring virtual network interfaces, verifying connectivity between lab systems, and preparing the network for security monitoring and controlled attack simulations.

The environment uses VirtualBox NAT and Host-Only networking, with pfSense providing firewall monitoring and traffic logging.

## 2. Network Configuration

The following IP addresses were observed during the lab.

| System / Interface | IP Address | Purpose |
|---|---|---|
| Kali Linux — eth0 | 10.0.0.2/24 | NAT connectivity |
| Kali Linux — eth1 | 192.168.56.105/24 | Host-Only connectivity |
| Metasploitable 2 | 10.6.6.11 | Vulnerable testing target |
| pfSense | Verify in VM configuration | Firewall and traffic logging |
| Ubuntu / Splunk | Verify in VM configuration | Centralized security monitoring |

The network configuration supports authorized testing, log collection, and security investigations.

## 3. Configure VirtualBox Network Adapters

1. Open Oracle VirtualBox.
2. Select the Kali Linux virtual machine.
3. Navigate to **Settings → Network**.
4. Configure the required adapters:
   - **Adapter 1:** NAT
   - **Adapter 2:** Host-Only Adapter
5. Ensure both adapters are enabled.
6. Start Kali Linux.

The exact adapter types should match the working lab configuration. Other virtual machines may use different network assignments.

## 4. Verify Kali Linux Network Interfaces

Open the Kali Linux terminal.

Check network interfaces:

```bash
ip -br addr
```

Check the routing table:

```bash
ip route
```

Check NetworkManager connections:

```bash
nmcli device status
```

If a configured interface is disconnected, identify its connection profile:

```bash
nmcli connection show
```

Activate the appropriate profile:

```bash
sudo nmcli connection up "<connection-name>"
```

Replace `<connection-name>` with the actual NetworkManager connection name.

**Expected Result:** The required network interfaces are active and have valid IP addresses.

## 5. Test Network Connectivity

### Verify Internet Connectivity

```bash
ping -c 4 1.1.1.1
```

### Verify DNS Resolution

```bash
ping -c 4 google.com
```

### Verify Metasploitable Connectivity

```bash
ping -c 4 10.6.6.11
```

### Verify the Host-Only Network

```bash
ping -c 4 192.168.56.1
```

Successful responses confirm basic IP connectivity to the tested destinations.

Note that ICMP may be blocked by firewall rules, so a failed ping does not always mean the destination is unreachable.

## 6. Network Troubleshooting

During the lab, Kali Linux experienced network connectivity issues involving `eth0` and `eth1`.

The troubleshooting process included:

- Checking IP addresses using `ip addr`.
- Reviewing the routing table with `ip route`.
- Inspecting NetworkManager connection profiles.
- Reactivating disconnected network interfaces.
- Verifying connectivity using `ping`.
- Checking firewall and virtual network dependencies.

**Useful Commands:**

```bash
# Check interface status
ip -br addr

# Check routing
ip route

# Check NetworkManager
nmcli device status

# Test connectivity
ping -c 4 10.6.6.11
```

Network troubleshooting helped ensure that the testing machines could communicate with the intended lab systems.

## 7. Expected Results

By the end of Phase 2:

- Kali Linux network interfaces are configured.
- NAT and Host-Only connectivity are verified.
- Metasploitable 2 is reachable from the testing environment.
- Network routing and connectivity issues are resolved.
- The lab is prepared for security log collection and network monitoring.

## 8. Skills Learned

- TCP/IP networking
- VirtualBox network configuration
- NAT and Host-Only networking
- Linux network interface management
- Network routing and troubleshooting
- Firewall connectivity validation

---
