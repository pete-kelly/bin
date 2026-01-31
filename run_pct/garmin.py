"""
garmin.py
The Garmin Forerunner 55 sports watch records time spent running, walking, and idle. This script takes in these times and produces percentages. 
Author: Pete Kelly 
"""

from datetime import datetime

run = input("Enter time running: ")
walk = input("Enter time walking: ")
idle = input("Enter idle time: ")

today = datetime.today().strftime("%Y-%m-%d")


def to_mins(colon_time):
    if ":" in colon_time:
        m, s = colon_time.split(":")
        return int(m) + int(s) / 60
    else:
        return(int(colon_time))  # for case when a time is an integer or zero


r, w, i = to_mins(run), to_mins(walk), to_mins(idle)

pct_running = round(100 * r / (r + w + i))
print(f"Percent running: {pct_running}")

out_str = f"{today},{pct_running}\n"

with open("run.txt", "a") as f:
    f.write(out_str)
