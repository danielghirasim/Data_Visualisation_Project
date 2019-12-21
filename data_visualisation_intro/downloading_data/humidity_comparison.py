import csv
from datetime import datetime
import matplotlib.pyplot as plt

file = 'downloading_data/csv_data/sitka_weather_2014.csv'

with open(file) as f:
    reader = csv.reader(f)
    headings = next(f)

    dates, precipitations, max_humidity, min_humidity = [], [], [], []
    for row in reader:
        try:
            current_time = datetime.strptime(row[0], "%Y-%m-%d")
            max_hum = int(row[7])
            min_hum = int(row[9])
            precipitation = float(row[19])
        except ValueError:
            print("Value Error in row: ", row)
        else:
            precipitations.append(precipitation)
            dates.append(current_time)
            max_humidity.append(max_hum)
            min_humidity.append(min_hum)

plt.figure(dpi=128, figsize=(10, 8))
plt.ylabel('Humidity (%)')
plt.plot(dates,max_humidity, c='cyan')
plt.plot(dates, min_humidity, c='purple')
plt.show()
