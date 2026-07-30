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
#from pathlib import Path
#import csv
#from datetime import datetime
#import matplotlib.pyplot as plt

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_07-2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)

##dates, highs = [], []
##for row in reader:
##    current_date = datetime.strptime(row[2], '%Y-%m-%d')
##    dates.append(current_date)
##    high = int(row[4])
##    highs.append(high)

#rows = list(reader)                  #使用列表将每一行存下来，然后遍历这个列表
#dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
#highs = [int(row[4]) for row in rows]

#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, color = 'red')

##设置绘图格式
#ax.set_title('Daily High Temperatures, July 2021', fontsize = 24)
#ax.set_xlabel('', fontsize = 16)
#fig.autofmt_xdate()

#ax.set_ylabel('Tmeperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig = 'D:\代码\PY_test\第十六章\png/16_1_6.png'
#plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
#plt.show()

#print(rows)


#-------------------------------------------------------------------------------
###16.1.7涵盖更长时间
#from pathlib import Path
#import csv
#import matplotlib.pyplot as plt
#from datetime import datetime

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)

###需要先看下表头这一行每一列都是什么，以及索引的序号。
##for index, column_header in enumerate(header_row):
##    print(index, column_header) 

#rows = list(reader)
#dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
#highs = [int(row[4]) for row in rows]

#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, color = 'red')

#ax.set_title('Daily High Temperatures, 2021', fontsize = 24)
#ax.set_xlabel('',fontsize = 16)
#fig.autofmt_xdate()

#ax.set_ylabel('Temperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig = 'D:\代码\PY_test\第十六章\png/16_1_7.png'
#plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
#plt.show()

#-------------------------------------------------------------------------------
###16.1.8再绘制一个数系列
#from pathlib import Path
#import csv
#import matplotlib.pyplot as plt
#from datetime import datetime

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#rows = list(reader)
#dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
#highs = [int(row[4]) for row in rows]
#lows = [int(row[5]) for row in rows]

#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, color = 'red')
#ax.plot(dates, lows, color = 'blue')

#ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
#ax.set_xlabel('', fontsize = 16)
#fig.autofmt_xdate()

#ax.set_ylabel('Temperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig = 'D:\代码\PY_test\第十六章\png/16_1_8.png'
#plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
#plt.show()


#-------------------------------------------------------------------------------
###16.1.9给图形区域着色
#from pathlib import Path
#import csv
#from datetime import datetime
#import  matplotlib.pyplot as plt

#path = Path('D:\代码\PY_test\第十六章\csv\sitka_weather_2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)

###看看每列的序号，略

#rows= list(reader)
#dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
#highs = [int(row[4]) for row in rows]
#lows = [int(row[5]) for row in rows]

#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.plot(dates, highs, color = 'red', alpha = 0.5)
#ax.plot(dates, lows, color = 'blue', alpha = 0.5)
#ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

#ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
#ax.set_xlabel('', fontsize = 16)
#fig.autofmt_xdate()

#ax.set_ylabel('Temperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig = 'D:\代码\PY_test\第十六章\png/16_1_9.png'
#plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
#plt.show()


#-------------------------------------------------------------------------------
###16.1.10错误检查
#from pathlib import Path
#import csv
#from datetime import datetime
#import matplotlib.pyplot as plt

#path = Path('D:\代码\PY_test\第十六章\csv\death_valley_2021_simple.csv')
#lines = path.read_text().splitlines()

#reader = csv.reader(lines)
#header_row = next(reader)

#for index, column in enumerate(header_row):
#    print(index, column)

#dates, highs, lows = [], [], []
##for row in reader:
##    date = datetime.strptime(row[2], '%Y-%m-%d')
##    dates.append(date)
##    high = int(row[3])
##    highs.append(high)
##    low = int(row[4])
##    lows.append(low)

#or row in reader:
#    date = datetime.strptime(row[2], '%Y-%m-%d')
#    try:
#        high = int(row[3])
#        low = int(row[4])
#    except ValueError:
#        #dates.append(date)
#        #highs.append(None)   # None会让折线在此处断开
#        #lows.append(None)
#        print(f"Missing data for {date}")
#    else:
#        dates.append(date)
#        highs.append(high)
#        lows.append(low)

#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#plt.plot(dates, highs, color = 'red', alpha = 0.5)
#plt.plot(dates, lows, color = 'blue', alpha = 0.5)
#ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

#ax.set_title('Daily High and Low Temperatures, 2021', fontsize = 24)
#ax.set_xlabel('', fontsize = 16)
#fig.autofmt_xdate()

#ax.set_ylabel('Temperature (F)', fontsize = 16)
#ax.tick_params(labelsize = 16)
#path_fig = 'D:\代码\PY_test\第十六章\png/16_1_10.png'
#plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
#plt.show()




























