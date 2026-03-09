import csv
import time

LOG_FILE="../day1-log-generator/security_logs.csv"

print("Real-time log monitoring started...\n")

with open(LOG_FILE,"r") as file:
    reader=csv.reader(file)
    next(reader)
    pointer=sum(1 for row in reader)

while True:

    with open(LOG_FILE,"r") as file:
        reader=list(csv.reader(file))

    new_logs=reader[pointer:]
    pointer=len(reader)

    for log in new_logs:
        print("New Log:",log)

    time.sleep(1)
