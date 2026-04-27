log_file = "logs/sample-log.txt"

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "disconnected" in line.lower():
        print("⚠️ Possible connection issue:", line.strip())
    if "interference" in line.lower():
        print("📡 Interference detected:", line.strip())
    if "high load" in line.lower():
        print("👥 High client load detected:", line.strip())
issues = {
    "roaming": 0,
    "latency": 0,
    "packet_loss": 0,
    "retry": 0,
    "timeout": 0
}

for line in logs:
    l = line.lower()

    if "roaming" in l:
        issues["roaming"] += 1
    if "latency" in l:
        issues["latency"] += 1
    if "packet loss" in l:
        issues["packet_loss"] += 1
    if "retry" in l:
        issues["retry"] += 1
    if "timeout" in l:
        issues["timeout"] += 1

print("\n--- Issue Summary ---")
for k, v in issues.items():
    print(f"{k}: {v}")
