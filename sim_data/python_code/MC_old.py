from pathlib import Path
import csv
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FormatStrFormatter

path = Path(r'D:\代码\PY_test\sim_data\csv_data\MonteCarlo.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index,column in enumerate(header_row):
    print(index,column)

rows = list(reader)
point= [float(row[0]) for row in rows]            #一般情况下都是使用float浮点数的。
mc_data= [float(row[8]) for row in rows]
mc_data = [v * 1e9 for v in mc_data]              #原始单位是 V，量级在 1e-7，换算成 n(纳) 横轴才好看



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
ax.set_xlim(-560.4, 560.4)
ax.set_ylim(0, 180)

#直方图：只给样本，柱高（每个区间里有几个点）由它自己数出来，不用你给
#bins 是柱子个数，range 是统计区间，两个一配柱宽就是 1120.8/12 = 93.4，正好和 xlim 对齐
#返回值：counts 是每根柱子的高度，bin_edges 是13个区间边界
counts, bin_edges, patches = ax.hist(mc_data, bins = 12, range = (-560.4, 560.4),
                                     color = '#FBD0D0', edgecolor = 'red', linewidth = 1)   #浅粉填充 + 红色描边

#正态拟合曲线
mu = np.mean(mc_data)
sigma = np.std(mc_data, ddof = 1)                    #ddof=1 是样本标准差，Cadence 报的就是这个
x_fit = np.linspace(-560.4, 560.4, 500)              #曲线的采样点，500个够平滑了
#Cadence 的曲线不做面积归一化，是把峰值直接对齐到最高的那根柱子，所以前面乘 counts.max()
#形状仍是标准高斯：1σ 处降到峰值的 e^-0.5≈61%，2σ 处 e^-2≈14%
y_fit = counts.max() * np.exp(-(x_fit - mu)**2 / (2 * sigma**2))
ax.plot(x_fit, y_fit, color = 'red', linewidth = 2.5, zorder = 3)   #zorder 抬高，别被柱子压住

#散点：每个样本一个空心圈，和直方图共用纵轴，点是填在柱子里面的
#横坐标 = 样本的真实值，纵坐标 = 它在自己所属那根柱子里排第几个，所以柱子多高里面就有多少个圈
mc_arr = np.array(mc_data)
bin_idx = np.digitize(mc_arr, bin_edges) - 1              #每个样本落在第几根柱子里，digitize 从1开始所以要减1
bin_idx = np.clip(bin_idx, 0, len(counts) - 1)            #正好压在最右边界上的样本会溢出一格，夹回来

#CSV 里的数据是按数值从大到小排好序的，直接拿"第几个"当纵坐标的话，
#y 就和数值大小同步了，每根柱子里的点会连成一条斜线。所以要在柱子内部打乱顺序
rng = np.random.default_rng(0)                            #固定种子，每次跑出来的图一样
y_scatter = np.zeros(len(mc_arr))
for b in range(len(counts)):
    mask = (bin_idx == b)                                 #挑出落在这根柱子里的所有样本
    ranks = np.arange(1, mask.sum() + 1)                  #1,2,...,柱高，正好填满不重叠
    rng.shuffle(ranks)                                    #打乱，让 y 和数值大小无关
    y_scatter[mask] = ranks

#空心圈：实心的话点多了会糊成一团。zorder 要比柱子和曲线都高
ax.scatter(mc_arr, y_scatter, s = 25, facecolors = 'none', edgecolors = 'red',
           linewidths = 0.8, zorder = 4)



#主刻度：写数字的那一档，横纵轴都显式给间隔
ax.xaxis.set_major_locator(MultipleLocator(186.8))         #每 186.8 一个，正好隔两根柱子
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))   #刻度数字保留一位小数
ax.yaxis.set_major_locator(MultipleLocator(20))            #0~180 每 20 一个

#次刻度：主刻度间隔÷10，两个数值之间就夹9条短刻度
#MultipleLocator 直接给间隔，不像 AutoMinorLocator 那样要靠反推主刻度间隔
ax.xaxis.set_minor_locator(MultipleLocator(18.68))         #186.8 ÷ 10
ax.yaxis.set_minor_locator(MultipleLocator(4))             #20 ÷ 10

#刻度线本身画出来（长短、朝向）：主刻度长、次刻度短，横纵轴用同一套
ax.tick_params(axis = 'both', which = 'major', direction = 'in', length = 7, width = 1.2, top = False, right = False)
ax.tick_params(axis = 'both', which = 'minor', direction = 'in', length = 3.5, width = 1, top = False, right = False)

#网格
ax.grid(True, which = 'major', linestyle = '-',  linewidth = 0.35, alpha = 0.6, color = 'dimgrey')  #贯穿的实线
ax.grid(True, axis = 'y', which = 'minor', dashes = (4, 4),  linewidth = 0.3, alpha = 0.3, color = 'grey')   #只画横向的，(线长, 间隔)。横轴小刻度有9条，再画竖网格整张图会糊
ax.set_axisbelow(False)         #整根坐标轴（网格+刻度线）画在柱子上面，否则朝内的刻度会被柱子盖住


#设置绘图格式
ax.set_title('', fontsize = 24)
ax.set_xlabel('Values(n)', fontsize = 18, fontweight = 'bold')      #n = nano，对应上面的 ×1e9

ax.set_ylabel('No.of Samples', fontsize = 18, fontweight = 'bold')  #纵轴是落在每个区间里的样本个数
ax.tick_params(labelsize = 18)
ax.tick_params(axis = 'x', which = 'major', pad = 8)    #横轴刻度数字向下移，数值越大离轴越远

#μ 和 ±1σ/±2σ/±3σ 的竖线：axvline 只给 x，线自动从图底贯穿到图顶
#zorder=2 夹在柱子(1)和拟合曲线(3)之间
for k in (-3, -2, -1, 0, 1, 2, 3):
    ax.axvline(mu + k * sigma, color = 'blue', linestyle = ':', linewidth = 1, zorder = 2)

    if k == 0:
        s = r'$\mu$'                    #前面的 r 不能少，否则 \m 会被当转义字符
    elif k == 1:
        s = r'$\sigma$'
    elif k == -1:
        s = r'$-\sigma$'
    else:
        s = rf'${k}\sigma$'
    #标签的 x 要跟着 σ 走(数据坐标)，y 要固定在图中间高度(轴比例坐标)，两个方向坐标系不同
    #get_xaxis_transform() 就是"x走数据、y走0~1比例"的混合坐标系
    ax.text(mu + k * sigma - 10, 0.47, s,
            transform = ax.get_xaxis_transform(),
            fontsize = 13, color = 'grey',
            ha = 'right', va = 'center')    #-10 配 ha='right'，把标签贴在竖线左边躲开线

#添加文字：坐标用 transform=ax.transAxes，(0,0)是左下角，(1,1)是右上角
#右上角的 μ/σ 标注框，数值从数据实时算，mu/sigma 是 n 单位，乘 1e-9 变回 V
ax.text(0.99, 0.99, f'μ:{mu*1e-9:.5E}\nσ:{sigma*1e-9:.5E}'.replace('E-0', 'E-'),
        transform = ax.transAxes,
        fontsize = 24, fontweight = 'bold', color = 'black',
        ha = 'right', va = 'top',       #ha/va 是对齐方式，右上角要用 right/top
        multialignment = 'left',        #两行之间左对齐，整块再靠右
        linespacing = 1.5)              #行距，默认1.2偏挤


path_fig = r'D:\代码\PY_test\sim_data\png\mc.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()
