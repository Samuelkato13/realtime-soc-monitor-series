import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

BASE_DIR = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_DIR, "..", "day1-log-generator", "security_logs.csv")

fig, axes = plt.subplots(3, 1, figsize=(10, 10))

def update(frame):

    failed_attempts = defaultdict(int)
    events = defaultdict(int)
    timestamps = []

    with open(LOG_FILE, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            event = row["event"]
            ip = row["ip"]
            timestamp = row["timestamp"]

            events[event] += 1

            if event == "login_failed":
                failed_attempts[ip] += 1
                timestamps.append(timestamp)

    # Clear charts
    for ax in axes:
        ax.clear()

    # 1️⃣ BAR CHART — Failed logins per IP
    ips = list(failed_attempts.keys())
    counts = list(failed_attempts.values())

    axes[0].bar(ips, counts)
    axes[0].set_title("Failed Login Attempts per IP")
    axes[0].set_xlabel("IP Address")
    axes[0].set_ylabel("Attempts")

    # 2️⃣ LINE GRAPH — Failed logins over time
    axes[1].plot(range(len(timestamps)), range(len(timestamps)))
    axes[1].set_title("Failed Login Activity Over Time")
    axes[1].set_xlabel("Events")
    axes[1].set_ylabel("Failed Logins")

    # 3️⃣ PIE CHART — Event distribution
    labels = list(events.keys())
    values = list(events.values())

    axes[2].pie(values, labels=labels, autopct="%1.1f%%")
    axes[2].set_title("Security Event Distribution")

ani = FuncAnimation(fig, update, interval=2000)

plt.tight_layout()
plt.show()
