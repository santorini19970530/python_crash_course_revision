# Python Crash Course, 2Ed, writtern by Eric Matthes

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates1, rainfalls1 = [], []
    for row in reader:
        dates1.append(datetime.strptime(row[2], '%Y-%m-%d'))
        rainfalls1.append(float(row[3]))

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates2, rainfalls2 = [], []
    for row in reader:
        dates2.append(datetime.strptime(row[2], '%Y-%m-%d'))
        rainfalls2.append(float(row[3]))

# Plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates1, rainfalls1, c='blue', label="Sitka")
ax.legend()
ax.plot(dates2, rainfalls2, c='green', label="Death Valley")
ax.legend()

# Format plot
ax.set_title("Daily rainfalls, 2018", fontsize = 20)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Minimeters", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize = 16)

plt.show()
