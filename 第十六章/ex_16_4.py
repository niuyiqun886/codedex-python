###练习16.4自动索引
from pathlib import Path
import csv
from datetime import datetime
import  matplotlib.pyplot as plt

path = Path('D:\代码\PY_test\第十六章\csv\death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, column in enumerate(header_row):
#    if column == 'TMAX':
#        column_TMAX = index
#        print(column_TMAX)
#    if column == 'TMIN':
#        column_TMIN = index
#        print(column_TMIN)
#   if column == 'DATE':
#        column_date = index
#        print(column_date)
#    if column == 'NAME':
#        column_name = index
#        print(column_name)

##简化
column_TMAX = header_row.index('TMAX')
column_TMIN = header_row.index('TMIN')
column_date = header_row.index('DATE')
column_name = header_row.index('NAME')

rows = list(reader)
station_name = rows[0][column_name]     #先取rows的第一行，然后再取 `[column]` 这个位置的内容。
print(station_name)

dates, highs, lows = [], [], []
for row in rows:                #上面将reader变为了rows了，所以要遍历rows
    date = datetime.strptime(row[column_date], '%Y-%m-%d')
    try:
        high = int(row[column_TMAX])
        low = int(row[column_TMIN])
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
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title(f"{station_name}", fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/ex_16_4.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()
