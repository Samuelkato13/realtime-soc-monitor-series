import csv
import random
import time
from datetime import datetime

LOG_FILE = "security_logs.csv"

users = ["admin","john","lucy","samuel"]
events = ["login_success","login_failed","file_access"]
ips = [
"192.168.1.10",
"192.168.1.15",
"10.0.0.5",
"172.16.0.3",
"45.77.23.12"
]

with open(LOG_FILE,"w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp","event","user","ip"])

print("Starting log generation...\n")

while True:

    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    event=random.choice(events)
    user=random.choice(users)
    ip=random.choice(ips)

    with open(LOG_FILE,"a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([timestamp,event,user,ip])

    print(timestamp,event,user,ip)

    time.sleep(random.randint(1,3))
