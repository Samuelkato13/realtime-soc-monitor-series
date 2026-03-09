import csv
import time
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "..", "day1-log-generator", "security_logs.csv")

failed_attempts = defaultdict(int)

THRESHOLD = 5

print("Threat detection system running...\n")

with open(LOG_FILE, "r") as file:
    reader = csv.reader(file)
    next(reader)
    pointer = sum(1 for row in reader)

while True:

    with open(LOG_FILE, "r") as file:
        reader = list(csv.reader(file))

    new_logs = reader[pointer:]
    pointer = len(reader)

    for log in new_logs:

        timestamp, event, user, ip = log

        if event == "login_failed":

            failed_attempts[ip] += 1

            if failed_attempts[ip] >= THRESHOLD:

                print("\n🚨 ALERT 🚨")
                print("Possible brute force attack detected")
                print("IP:", ip)
                print("Failed Attempts:", failed_attempts[ip])
                print()

    time.sleep(1)
