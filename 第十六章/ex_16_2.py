##练习 16.2:比较锡特卡和死亡谷的温度
from pathlib import Path
import csv
from datetime import datetime
import  matplotlib.pyplot as plt

path = Path('D:\代码\PY_test\第十六章\csv\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column in enumerate(header_row):
    print(index, column)

dates, highs, lows = [], [], []
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


path1 = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
lines1 = path1.read_text().splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)

##看看每列的序号，略

rows1= list(reader1)
dates1 = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows1]
highs1 = [int(row[4]) for row in rows1]
lows1 = [int(row[5]) for row in rows1]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'orange', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'orange', alpha = 0.1)

ax.plot(dates1, highs1, color = 'blue', alpha = 0.5)
ax.plot(dates1, lows1, color = 'cyan', alpha = 0.5)
ax.fill_between(dates1, highs1, lows1, facecolor = 'blue', alpha = 0.1)


ax.set_title('Temperature Compare', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
ax.set_yticks(range(0, 141, 10))           # 设置刻度，每隔10一个
path_fig = 'D:\代码\PY_test\第十六章\png/16_2.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()

