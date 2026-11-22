import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

base = Path.home() / "Downloads"

df = pd.read_csv(base / "network_security_logs.csv")

df["_time"] = pd.to_datetime(df["_time"], utc=True, errors="coerce")
df["dest_port"] = pd.to_numeric(df["dest_port"], errors="coerce")

df = df.dropna(
    subset=["_time", "src_ip", "dest_ip", "dest_port"]
)

print("=== SOC SECURITY LOG ANALYSIS ===")
print(f"Total events: {len(df)}")
print(f"Unique source IPs: {df['src_ip'].nunique()}")
print(f"Unique destination IPs: {df['dest_ip'].nunique()}")

top_ips = df["src_ip"].value_counts().head(10)
top_ports = df["dest_port"].value_counts().head(10)

print("\n=== TOP 10 SOURCE IPs ===")
print(top_ips)

print("\n=== TOP 10 DESTINATION PORTS ===")
print(top_ports)

scan = (
    df.groupby(["src_ip", "dest_ip"])
    .agg(
        total_events=("dest_port", "size"),
        unique_ports=("dest_port", "nunique")
    )
    .reset_index()
)

suspicious = scan[scan["unique_ports"] >= 5].copy()
suspicious = suspicious.sort_values(
    "unique_ports", ascending=False
)

print("\n=== POTENTIAL PORT SCANNING ===")
print(suspicious.to_string(index=False))

suspicious.to_csv(
    base / "port_scan_report.csv", index=False
)

plt.figure(figsize=(10, 5))
top_ips.plot(kind="bar")
plt.title("Top 10 Source IP Addresses")
plt.xlabel("Source IP")
plt.ylabel("Number of Events")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(base / "top_source_ips.png")
plt.close()

plt.figure(figsize=(10, 5))
top_ports.plot(kind="bar")
plt.title("Top 10 Destination Ports")
plt.xlabel("Destination Port")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig(base / "top_destination_ports.png")
plt.close()

traffic = df.set_index("_time").resample("5min").size()

plt.figure(figsize=(10, 5))
traffic.plot()
plt.title("Network Security Events Over Time")
plt.xlabel("Time (UTC)")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig(base / "network_traffic_timeline.png")
plt.close()

print("\nAnalysis completed successfully!")
print("Reports and charts saved in ~/Downloads")
