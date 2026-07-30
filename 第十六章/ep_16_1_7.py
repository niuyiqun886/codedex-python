###16.1.7涵盖更长时间
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

##需要先看下表头这一行每一列都是什么，以及索引的序号。
#for index, column_header in enumerate(header_row):
#    print(index, column_header) 

rows = list(reader)
dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
highs = [int(row[4]) for row in rows]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red')

ax.set_title('Daily High Temperatures, 2021', fontsize = 24)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/16_1_7.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()