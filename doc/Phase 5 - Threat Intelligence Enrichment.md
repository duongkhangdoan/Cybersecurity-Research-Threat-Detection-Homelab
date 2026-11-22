## 1. Overview

In this phase, I investigated a public IP address using VirusTotal and AbuseIPDB to evaluate its reputation and potential security risks.

I then created a CSV threat intelligence lookup and integrated it into Splunk Enterprise to enrich firewall events with external reputation data.

## 2. Tools & Technologies

| Tool | Purpose |
|---|---|
| VirusTotal | IP reputation analysis |
| AbuseIPDB | IP abuse reputation checks |
| Splunk Enterprise | Security event enrichment |
| CSV Lookup | Store and correlate threat intelligence data |
| SPL | Match network events with reputation information |

## 3. Investigate IP Reputation

The public IP address `91.189.91.112` was investigated using two threat intelligence platforms.

### Step 1 — VirusTotal

Visit [VirusTotal](https://www.virustotal.com/gui/home/search) and search for:

`91.189.91.112`

<img width="788" height="1350" alt="image" src="https://github.com/user-attachments/assets/2e866569-26f4-460d-a134-8bd2f37f75d2" />

**Observed Result:** 0/92 security vendors flagged the IP address.

### Step 2 — AbuseIPDB

Visit [AbuseIPDB](https://www.abuseipdb.com/) and search for the same IP address.

<img width="940" height="1350" alt="image" src="https://github.com/user-attachments/assets/3c60cb26-6f78-4fe5-8177-9b8fd79efec8" />

**Observed Result:**

- Abuse Confidence Score: 0%
- Reported Abuse: No reports observed
- Assessment: Likely benign based on available reputation information

These results do not guarantee that the IP address is safe.

## 4. Create Threat Intelligence CSV Lookup

Create a file named `threat_intelligence.csv` containing:

<img width="795" height="532" alt="image" src="https://github.com/user-attachments/assets/9bcc3670-b4bb-48da-945d-eab9926b60f8" />

```csv
dest_ip,vt_detection,abuse_score,classification
91.189.91.112,0,0,likely_benign
```

The CSV file stores the investigated IP address and its reputation information.

### Upload the Lookup to Splunk

1. Open **Splunk Enterprise**.
2. Navigate to **Settings → Lookups → Lookup Table Files**.
3. Select **Add New**.
4. Choose the `search` application.
5. Upload `threat_intelligence.csv`.
6. Save the lookup file.

<img width="1531" height="686" alt="image" src="https://github.com/user-attachments/assets/6c647342-f43e-4d9f-9835-7aa2091acce9" />
<img width="975" height="205" alt="image" src="https://github.com/user-attachments/assets/694a9b12-bb2f-45b1-bf15-f0a9e567cc10" />

## 5. Enrich Firewall Logs with Threat Intelligence

Open **Splunk → Search & Reporting**.

Run the following SPL query:

```spl
index=pfsense sourcetype="pfsense:filterlog"
| lookup threat_intelligence.csv dest_ip OUTPUT vt_detection abuse_score classification
| search classification=*
| table _time src_ip dest_ip vt_detection abuse_score classification
```

This query:

- Searches pfSense firewall events.
- Matches destination IP addresses against the CSV lookup.
- Adds VirusTotal and AbuseIPDB reputation information.
- Displays matching enriched security events.

**Expected Result:** Matching firewall events display the reputation classification `likely_benign`, along with the stored detection and abuse scores.

## 6. Investigation Results

| Field | Result |
|---|---|
| Investigated IP | 91.189.91.112 |
| VirusTotal Detections | 0/92 |
| AbuseIPDB Score | 0% |
| Classification | Likely Benign |
| Enrichment Method | Splunk CSV Lookup |

The investigation demonstrated how external threat intelligence can provide additional context during security event analysis.

The reputation assessment was performed manually, and the results were stored in a static CSV lookup rather than retrieved through automated API integration.

## 7. Skills Learned

- Threat intelligence research
- IP reputation investigation
- VirusTotal and AbuseIPDB analysis
- Indicator of Compromise (IOC) enrichment
- Splunk CSV lookups
- SPL-based event correlation
- Security investigation and classification

---
