import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.
    dates, highs1, lows1 = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d'))
        highs1.append(int(row[header_row.index('TMAX')]))
        lows1.append(int(row[header_row.index('TMIN')]))

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high and low temperatures from this file.
    dates, highs2, lows2 = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
        try:
            high = int(row[header_row.index('TMAX')])
            low = int(row[header_row.index('TMIN')])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            highs2.append(high)
            lows2.append(low)

# Plot the high and low temperatures
# Shade the temperature range
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs1, c='red', alpha=0.5, label='Sitka High')
ax.plot(dates, lows1, c='blue', alpha=0.5, label='Stika Low')
ax.fill_between(dates, highs1, lows1, facecolor='blue', alpha=0.1)
ax.legend()
ax.plot(dates, highs2, c='brown', alpha=0.5, label="Death Valley High")
ax.plot(dates, lows2, c='green', alpha=0.5, label="Death Valley Low")
ax.fill_between(dates, highs2, lows2, facecolor='yellow', alpha=0.1)
ax.legend()

# Format plot
ax.set_title("Daily high and low temperatures, 2018", fontsize = 24)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize = 16)
ax.tick_params(axis='both', which='major', labelsize = 16)

plt.show()
