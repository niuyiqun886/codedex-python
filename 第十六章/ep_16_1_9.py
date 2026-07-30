##16.1.9给图形区域着色
from pathlib import Path
import csv
from datetime import datetime
import  matplotlib.pyplot as plt

path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

##看看每列的序号，略

rows= list(reader)
dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
highs = [int(row[4]) for row in rows]
lows = [int(row[5]) for row in rows]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/16_1_9.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()
