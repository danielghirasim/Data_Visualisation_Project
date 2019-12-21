import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'filename.csv'
with open(filename) as f:
    reader = csv.reader(f)
    heading = next(reader)


    highs, lows, dates= [],[],[]
    for row in reader:
        try:
            high = int(row[1])
            low = int(row[3])
            current_time = datetime.strptime(row[0], "%Y-%m-%d")
        except ValueError:
            print("Wrong Format: " , row)
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_time)

fig = plt.figure(dpi=128, figsize=(12,6))
plt.ylabel("Temperatures (F)")
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='gray')
plt.show()

