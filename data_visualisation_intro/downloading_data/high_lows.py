import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get high temperatures from file.
file_path = 'C:/Users/ghira/Desktop/Programming/Python Projects/Data_Visualisation_Project/data_visualisation_intro/downloading_data/csv_data/sitka_weather_2014.csv'

with open(file_path) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

print(dates)

# Plot data
fig = plt.figure(dpi=126 , figsize=(10,6))
plt.plot(dates, highs, c = 'red')
plt.plot(dates, lows, c = 'blue')
plt.fill_between(dates, highs, lows , facecolor='blue', alpha=0.1)
#Dates

# Format Plot

plt.title("Daily temperatures, July 2014", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()