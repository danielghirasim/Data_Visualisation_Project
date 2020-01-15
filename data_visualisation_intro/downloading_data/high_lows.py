import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get high temperatures from file.
file_path = 'csv_data/death_valley_2014.csv'

with open(file_path) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

print(dates)

# Plot data
fig = plt.figure(dpi=126 , figsize=(10,6))
plt.plot(dates, highs, c = 'red')
plt.plot(dates, lows, c = 'blue')
plt.fill_between(dates, highs, lows , facecolor='gray', alpha=0.6)
#Dates

# Format Plot

plt.title("Daily high and low temperatures\nDeath Valley, CA", fontsize=18)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()