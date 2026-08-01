from pathlib import Path
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, LogFormatterSciNotation, NullFormatter, AutoMinorLocator

path = Path(r'D:\代码\PY_test\sim_data\csv_data\gain.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index,column in enumerate(header_row):
    print(index,column)


rows = list(reader)
time = [float(row[0]) for row in rows]              #一般情况下都是使用float浮点数的。
gain_1= [float(row[1]) for row in rows]
gain_2= [float(row[2]) for row in rows]
gain_3= [float(row[3]) for row in rows]
gain_4= [float(row[4]) for row in rows]





#plt.style.use('seaborn-v0_8-whitegrid')               #白色底的
plt.style.use('seaborn-v0_8-ticks')


#字体：Arial 粗体（Origin 风格）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.weight'] = 'bold'                  #正文/刻度数字加粗
plt.rcParams['axes.labelweight'] = 'bold'             #坐标轴标题加粗
plt.rcParams['mathtext.fontset'] = 'custom'           #让 10^3 这类指数也用 Arial 粗体
plt.rcParams['mathtext.rm'] = 'Arial:bold'
plt.rcParams['mathtext.it'] = 'Arial:bold'
plt.rcParams['mathtext.bf'] = 'Arial:bold'

fig, ax = plt.subplots(figsize=(9, 7))   # 图形比例
#x轴和y轴的范围
ax.set_xlim(1e-3, 1e7)
ax.set_ylim(-20, 55)

#marker 为标记形状，markersize 大小，markevery 每隔几个点画一个
ax.plot(time, gain_1, color = 'red',    marker = 's', markersize = 3, markevery = 1)   #方形
ax.plot(time, gain_2, color = 'green',  marker = 'D', markersize = 3, markevery = 1)   #菱形
ax.plot(time, gain_3, color = 'blue',   marker = 'o', markersize = 3, markevery = 1)   #圆形
ax.plot(time, gain_4, color = 'orange', marker = '^', markersize = 3, markevery = 1)   #三角形
ax.set_xscale('log')            #横轴改为对数坐标（频率为0的点会被自动忽略）

#横轴刻度：主刻度每十倍频一个，次刻度 2~9 倍
ax.xaxis.set_major_locator(LogLocator(base = 10.0, subs = (1.0,), numticks = 100))   #每十倍频一个主刻度，一个都不省略
ax.xaxis.set_major_formatter(LogFormatterSciNotation(base = 10.0))
ax.xaxis.set_minor_locator(LogLocator(base = 10.0, subs = tuple(range(2, 10)), numticks = 100))
ax.xaxis.set_minor_formatter(NullFormatter())       #次刻度只画线，不写数字

#纵轴次刻度
ax.yaxis.set_minor_locator(AutoMinorLocator(5))     #参数是分成几段，5段 = 两个主刻度间插4个次刻度

#刻度线本身画出来（长短、朝向）
ax.tick_params(axis = 'both', which = 'major', direction = 'in', length = 5, width = 1, top = False, right = False)
ax.tick_params(axis = 'both', which = 'minor', direction = 'in', length = 2.5, width = 1, top = False, right = False)

#四周边框：黑色实线，上面换成了 seaborn-v0_8-ticks
#for spine in ax.spines.values():
#    spine.set_visible(True)
#    spine.set_color('black')
#    spine.set_linewidth(1.2)

#刻度线也改成黑色
ax.tick_params(axis = 'both', which = 'both', color = 'black', labelcolor = 'black')

#网格
ax.grid(True, which = 'major', linestyle = '-',  linewidth = 0.35, alpha = 0.6, color = 'dimgrey')  #贯穿的实线
ax.grid(True, which = 'minor', dashes = (4, 4),  linewidth = 0.3, alpha = 0.3, color = 'grey')   #贯穿的虚线，(线长, 间隔)


#设置绘图格式
ax.set_title('', fontsize = 24)
ax.set_xlabel('Frequency (Hz)', fontsize = 18, fontweight = 'bold')
#fig.autofmt_xdate()

ax.set_ylabel('Gain (dB)', fontsize = 18, fontweight = 'bold')
ax.tick_params(labelsize = 18)
ax.tick_params(axis = 'x', which = 'major', pad = 8)    #横轴刻度数字向下移，数值越大离轴越远

#让网格变成正方形：1个十倍频(x) 的宽度 = 10 dB(y) 的高度
#log轴下 x 的1个单位就是1个十倍频，所以 aspect = 10dB分之1 = 0.1
ax.set_aspect(1 / 10, adjustable = 'box')

#添加文字：坐标用 transform=ax.transAxes，(0,0)是左下角，(1,1)是右上角
ax.text(0.99, 0.99, 'Gain',
        transform = ax.transAxes,
        fontsize = 24, fontweight = 'bold', fontstyle = 'italic', color = 'black',
        ha = 'right', va = 'top')       #ha/va 是对齐方式，右上角要用 right/top

ax.text(2e5, 30.3, '30.1030dB', fontsize=14, color='red', va='center')



path_fig = r'D:\代码\PY_test\sim_data\png\gain.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 1200)
plt.show()










