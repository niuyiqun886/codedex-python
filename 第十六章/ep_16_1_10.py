###16.1.10错误检查
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('D:\代码\PY_test\第十六章\csv\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column in enumerate(header_row):
    print(index, column)

dates, highs, lows = [], [], []
#for row in reader:
#    date = datetime.strptime(row[2], '%Y-%m-%d')
#    dates.append(date)
#    high = int(row[3])
#    highs.append(high)
#    low = int(row[4])
#    lows.append(low)

for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        #dates.append(date)
        #highs.append(None)   # None会让折线在此处断开
        #lows.append(None)
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.plot(dates, highs, color = 'red', alpha = 0.5)
plt.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/16_1_10.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()
