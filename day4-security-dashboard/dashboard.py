import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

LOG_FILE="../day1-log-generator/security_logs.csv"

fig,ax=plt.subplots()

def update(frame):

    attempts=defaultdict(int)

    with open(LOG_FILE,"r") as file:

        reader=csv.DictReader(file)

        for row in reader:

            if row["event"]=="login_failed":

                attempts[row["ip"]]+=1

    ax.clear()

    ips=list(attempts.keys())
    counts=list(attempts.values())

    ax.bar(ips,counts)

    ax.set_title("Failed Login Attempts per IP")
    ax.set_xlabel("IP Address")
    ax.set_ylabel("Failed Attempts")

ani=FuncAnimation(fig,update,interval=2000)

plt.show()
