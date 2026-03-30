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
