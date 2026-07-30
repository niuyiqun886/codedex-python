##练习16.1：锡特卡的降雨量
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index,column in enumerate(header_row):
    print(index,column)

dates, prcps = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        #prcp = int(row[5])          #写之前先看是什么数int()是整数，这里的降雨量是小数
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        prcps.append(prcp)
        dates.append(date)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.plot(dates, prcps, color = 'red')

ax.set_title('Daily Precipitation', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Precipitation', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/ex_16_1.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()