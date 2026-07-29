#-------------------------------------------------------------------------------
###16.1.1解析csv文件头
#from pathlib import Path
#import csv
#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)
#print(header_row)

#print(path.read_text())
#print(lines)

#for row in reader:
#    print(row)


#-------------------------------------------------------------------------------
###16.1.2打印文件头及其位置
#from pathlib import Path
#import csv

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
##print(header_row)

#for index, column_header in enumerate(header_row):      #enumerate()可以同时拿到列的序号和列名
#    print(index, column_header)


#-------------------------------------------------------------------------------
###16.1.3提取并读取数据
#from pathlib import Path
#import csv

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)
##highs = []
##for row in reader:
##    high = int(row[4])
##    highs.append(high)
##列表推导式表达
#highs = [int(row[4]) for row in reader ]
#print(highs)

#-------------------------------------------------------------------------------
###16.1.4绘制温度图
#from pathlib import Path
#import csv
#import matplotlib.pyplot as plt

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#head_row = next(reader)

#highs = [int(row[4]) for row in reader]


#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()

#ax.plot(highs, color = 'red')
#ax.set_title('Daily High Temperatures, July 2021', fontsize = 24)
#ax.set_xlabel('', fontsize = 16)
#ax.set_ylabel('Temperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig =Path('D:\代码\PY_test\第十六章\png/16_1_4.png')
#plt.savefig(path_fig, bbox_inches='tight', dpi=500)
#plt.show()


#-------------------------------------------------------------------------------
###16.1.5 datetime模块
###使用datetime模块中的striptime()方法
#from datetime import datetime
#first_date = datetime.strptime('2021-07-01', '%Y-%m-%d')
#print(first_date)

#-------------------------------------------------------------------------------
###16.1.6在图中添加日期
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#dates, highs = [], []
#for row in reader:
#    current_date = datetime.strptime(row[2], '%Y-%m-%d')
#    dates.append(current_date)
#    high = int(row[4])
#    highs.append(high)

rows = list(reader)                  #使用列表将每一行存下来，然后遍历这个列表
dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
highs = [int(row[4]) for row in rows]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red')

#设置绘图格式
ax.set_title('Daily High Temperatures, July 2021', fontsize = 24)
ax.set_xlabel('', fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel('Tmeperature (F)', fontsize = 16)
ax.tick_params(labelsize = 16)
path_fig = 'D:\代码\PY_test\第十六章\png/16_1_6.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()

print(rows)











