# Jordan Fitzgerald
# 4/9/2026
# Log File Analyzer Project

logs = [
    "ERROR: Disk full",
    "INFO: User logged in",
    "WARNING: CPU usage high",
    "ERROR: Memory leak detected",
    "INFO: File uploaded",
    "ERROR: Disk full"
]
time_stamps = [
    "2026-04-09 10:00:00",
    "2026-04-09 10:05:00",
    "2026-04-09 10:10:00",
    "2026-04-09 10:15:00",
    "2026-04-09 10:20:00",
    "2026-04-09 10:25:00"
]
type_counts = {}
flag_messages = ["ERROR", "WARNING"]

print("Flagged Logs:")
for time_stamp, log in zip(time_stamps, logs):
    log_type = log.split(":")[0]
    if log_type in flag_messages:
        print(f"{time_stamp} - {log}")

for log in logs:
    log_type = log.split(":")[0]
    if log_type in type_counts:
        type_counts[log_type] += 1
    else:
        type_counts[log_type] = 1

print("Log Type Counts:")
for log_type, count in type_counts.items():
    print(f"{log_type}: {count}")

message_counts = {}

for log in logs:
    if log in message_counts:
        message_counts[log] += 1
    else:
        message_counts[log] = 1

most_common_log = ""
highest_count = 0

top3_logs = sorted(message_counts.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 Most Common Logs:")
for log, count in top3_logs:
    print(f"{log}: {count} occurrences")

for log, count in message_counts.items():
    if count > highest_count:
        most_common_log = log
        highest_count = count

print("\n Most Common Log:")
print(most_common_log)

seen = set()
duplicates = set()

for log in logs:
    if log in seen:
        duplicates.add(log)
    else:
        seen.add(log)

print("\nDuplicate Logs:")
for log in duplicates:
    print(log)

error_count = type_counts.get("ERROR", 0)
total_logs = len(logs)
error_rate = (error_count / total_logs) * 100
print(f"\nError Rate: {error_rate:.1f}%")

if error_rate >= 50:
    status = "Critical"
elif error_rate >= 20:
    status = "WARNING"
else:
    status = "OK"

print(f"System Status: {status}")
