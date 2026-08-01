"""蒙特卡洛仿真结果作图：直方图 + 正态拟合曲线 + 散点 + σ 竖线，复现 Cadence 的 MC 结果图。"""

from pathlib import Path
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


# ==================== 可调参数 ====================
# 集中放在这，改图形只动这一块，下面的代码都跟着走

X_LIM    = 560.4                 #横轴范围 ±560.4 (单位 n)
Y_MAX    = 180                   #纵轴上限，要比最高的柱子高一点
N_BINS   = 12                    #柱子个数
X_MAJOR  = X_LIM / 3             #横轴主刻度间隔 186.8，正好把半轴分成3段
Y_MAJOR  = 20                    #纵轴主刻度间隔
SEED     = 0                     #散点随机排布的种子，固定住每次出图才一样

#σ 竖线上的标签，前面的 r 不能少，否则 \m \s 会被当转义字符
SIGMA_LABELS = {-3: r'$-3\sigma$', -2: r'$-2\sigma$', -1: r'$-\sigma$',
                 0: r'$\mu$',
                 1: r'$\sigma$',   2: r'$2\sigma$',   3: r'$3\sigma$'}


# ==================== 1. 读数据 ====================

path = Path(r'D:\代码\PY_test\sim_data\csv_data\MonteCarlo.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index,column in enumerate(header_row):
    print(index,column)

rows = list(reader)
point= [float(row[0]) for row in rows]            #仿真序号，这张图没用到，留着方便查列
mc_data= [float(row[8]) for row in rows]          #一般情况下都是使用float浮点数的。
mc_data = np.array(mc_data) * 1e9                 #原始单位是 V，量级在 1e-7，换算成 n(纳) 横轴才好看


# ==================== 2. 统计量 ====================

mu = np.mean(mc_data)
sigma = np.std(mc_data, ddof = 1)                 #ddof=1 是样本标准差(分母N-1)，Cadence 报的就是这个


# ==================== 3. 画布与全局样式 ====================

plt.style.use('seaborn-v0_8-ticks')

#字体：Arial 粗体（Origin 风格）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.weight'] = 'bold'                  #正文/刻度数字加粗
plt.rcParams['axes.labelweight'] = 'bold'             #坐标轴标题加粗
plt.rcParams['mathtext.fontset'] = 'custom'           #让 μ σ 这类数学符号也用 Arial 粗体
plt.rcParams['mathtext.rm'] = 'Arial:bold'
plt.rcParams['mathtext.it'] = 'Arial:bold'
plt.rcParams['mathtext.bf'] = 'Arial:bold'

fig, ax = plt.subplots(figsize = (9, 7))              #图形比例
ax.set_xlim(-X_LIM, X_LIM)
ax.set_ylim(0, Y_MAX)


# ==================== 4. 直方图 ====================
# 只给样本，柱高（每个区间里落了几个点）由它自己数出来，不用你给
# bins 是柱子个数，range 是统计区间，两个一配柱宽就是 1120.8/12 = 93.4，正好和 xlim 对齐
# 返回值：counts 是每根柱子的高度，bin_edges 是 13 个区间边界

counts, bin_edges, patches = ax.hist(mc_data, bins = N_BINS, range = (-X_LIM, X_LIM),
                                     color = '#FBD0D0', edgecolor = 'red', linewidth = 1)


# ==================== 5. 正态拟合曲线 ====================
# Cadence 的曲线不做面积归一化，是把峰值直接对齐到最高的那根柱子，所以前面乘 counts.max()
# 形状仍是标准高斯：1σ 处降到峰值的 e^-0.5≈61%，2σ 处 e^-2≈14%

x_fit = np.linspace(-X_LIM, X_LIM, 500)           #曲线的采样点，500个够平滑了
y_fit = counts.max() * np.exp(-(x_fit - mu)**2 / (2 * sigma**2))
ax.plot(x_fit, y_fit, color = 'red', linewidth = 2.5, zorder = 3)


# ==================== 6. 散点 ====================
# 每个样本一个空心圈，和直方图共用纵轴，点是填在柱子里面的
# 横坐标 = 样本的真实值，纵坐标 = 它在自己所属那根柱子里排第几个，所以柱子多高里面就有多少个圈

bin_idx = np.digitize(mc_data, bin_edges) - 1     #每个样本落在第几根柱子里，digitize 从1开始所以要减1
bin_idx = np.clip(bin_idx, 0, len(counts) - 1)    #正好压在最右边界上的样本会溢出一格，夹回来

#CSV 里的数据是按数值从大到小排好序的，直接拿"第几个"当纵坐标的话，
#y 就和数值大小同步了，每根柱子里的点会连成一条斜线。所以要在柱子内部打乱顺序
rng = np.random.default_rng(SEED)
y_scatter = np.zeros(len(mc_data))
for b in range(len(counts)):
    mask = (bin_idx == b)                         #挑出落在这根柱子里的所有样本
    ranks = np.arange(1, mask.sum() + 1)          #1,2,...,柱高，正好填满不重叠
    rng.shuffle(ranks)                            #打乱，让 y 和数值大小无关
    y_scatter[mask] = ranks

#空心圈：实心的话点多了会糊成一团。zorder 要比柱子和曲线都高
ax.scatter(mc_data, y_scatter, s = 25, facecolors = 'none', edgecolors = 'red',
           linewidths = 0.8, zorder = 4)


# ==================== 7. μ 和 ±1σ/±2σ/±3σ 竖线 ====================
# axvline 只给 x，线自动从图底贯穿到图顶，图的上下界怎么变都不用管
# zorder=2 夹在柱子(1)和拟合曲线(3)之间

for k, label in SIGMA_LABELS.items():
    ax.axvline(mu + k * sigma, color = 'blue', linestyle = ':', linewidth = 1, zorder = 2)
    #标签的 x 要跟着 σ 走(数据坐标)，y 要固定在图中间高度(轴比例坐标)，两个方向坐标系不同
    #get_xaxis_transform() 就是"x走数据、y走0~1比例"的混合坐标系
    ax.text(mu + k * sigma - 10, 0.47, label,
            transform = ax.get_xaxis_transform(),
            fontsize = 13, color = 'grey',
            ha = 'right', va = 'center')          #-10 配 ha='right'，把标签贴在竖线左边躲开线


# ==================== 8. 坐标轴刻度 ====================

#主刻度：写数字的那一档，横纵轴都显式给间隔
ax.xaxis.set_major_locator(MultipleLocator(X_MAJOR))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))   #刻度数字保留一位小数
ax.yaxis.set_major_locator(MultipleLocator(Y_MAJOR))

#次刻度：MultipleLocator 直接给间隔，不像 AutoMinorLocator 那样要靠反推主刻度间隔
ax.xaxis.set_minor_locator(MultipleLocator(X_MAJOR / 10))  #÷10，两个数值之间夹9条短刻度
ax.yaxis.set_minor_locator(MultipleLocator(Y_MAJOR / 5))   #÷5，纵轴稀疏一点更清爽

#刻度线本身画出来（长短、朝向）：主刻度长、次刻度短，横纵轴用同一套
ax.tick_params(axis = 'both', which = 'major', direction = 'in', length = 7, width = 1.2, top = False, right = False)
ax.tick_params(axis = 'both', which = 'minor', direction = 'in', length = 3.5, width = 1, top = False, right = False)
ax.tick_params(labelsize = 18)
ax.tick_params(axis = 'x', which = 'major', pad = 8)       #横轴刻度数字向下移，数值越大离轴越远


# ==================== 9. 网格 ====================

ax.grid(True, which = 'major', linestyle = '-', linewidth = 0.35, alpha = 0.6, color = 'dimgrey')   #贯穿的实线
ax.grid(True, axis = 'y', which = 'minor', dashes = (4, 4), linewidth = 0.3, alpha = 0.3, color = 'grey')
#↑ 次网格只画横向的，(线长, 间隔)。横轴小刻度有9条，再画竖网格整张图会糊
ax.set_axisbelow(False)     #整根坐标轴（网格+刻度线）画在柱子上面，否则朝内的刻度会被柱子盖住


# ==================== 10. 标签与文字 ====================

ax.set_xlabel('Values(n)', fontsize = 18, fontweight = 'bold')      #n = nano，对应上面的 ×1e9
ax.set_ylabel('No.of Samples', fontsize = 18, fontweight = 'bold')  #纵轴是落在每个区间里的样本个数

#右上角的 μ/σ 标注框：坐标用 transform=ax.transAxes，(0,0)是左下角，(1,1)是右上角
#数值从数据实时算，mu/sigma 是 n 单位，乘 1e-9 变回 V
#.replace 是把 Python 的两位指数 E-09 改成 Cadence 的 E-9
ax.text(0.99, 0.99, f'μ:{mu*1e-9:.5E}\nσ:{sigma*1e-9:.5E}'.replace('E-0', 'E-'),
        transform = ax.transAxes,
        fontsize = 24, fontweight = 'bold', color = 'black',
        ha = 'right', va = 'top',           #ha/va 是对齐方式，右上角要用 right/top
        multialignment = 'left',            #两行之间左对齐，整块再靠右
        linespacing = 1.5)                  #行距，默认1.2偏挤


# ==================== 11. 保存 ====================

path_fig = r'D:\代码\PY_test\sim_data\png\mc.png'
plt.savefig(path_fig, bbox_inches = 'tight', dpi = 500)
plt.show()


# ==================== 下次换一份数据要改哪些地方 ====================
#
# 这个脚本没做通用化，是故意的：绘图脚本每张图都要按内容微调（刻度间隔、标注位置、
# 配色），做成参数化以后还是得进来改，只是要先读懂抽象层。下次直接复制一份改几个数
# 更省事。下面列出要动的地方，按顺序改。
#
# 【必改】
#   1. CSV_PATH / PNG_PATH ------ 第1段的 path、第11段的 path_fig
#   2. 数据列号 ----------------- 第1段 [float(row[8]) ...] 里的 8
#                                 脚本开头会打印表头和列号，跑一次就知道该填几
#
# 【单位：三处必须同时改，改一漏二是最容易犯的错】
#   3. 第1段  raw * 1e9              ← 换算倍率
#   4. 第10段 set_xlabel('Values(n)') ← 括号里的前缀
#   5. 第10段 标注框的 mu*1e-9        ← 倍率的倒数，把 μ/σ 换回原始单位
#      例：数据是 f(飞)量级 → 分别改成 *1e15、'Values(f)'、*1e-15
#
# 【看图后再调】
#   6. X_LIM --- 先跑一次，确认 min/max 都在 ±X_LIM 内。超出范围的样本会被 hist
#                直接丢掉，不报错也不进任何柱子，只能自己核对 sum(counts)==样本数
#   7. Y_MAX --- 比最高的柱子高 15% 左右，给右上角标注框留位置
#   8. Y_MAJOR - 纵轴主刻度间隔，挑一个能分出 6~10 格的整数
#      X_MAJOR 是 X_LIM/3 自动派生的，一般不用管
#
# 【踩过的坑，别再踩】
#   - CSV 用 Excel 编辑过的话，末尾容易留一行空的（全是逗号），float('') 会崩。
#     报错就在第1段加一句过滤：
#         rows = [row for row in reader if row and row[8].strip()]
#   - 散点的纵坐标必须在柱子内部打乱（第6段的 rng.shuffle）。Cadence 导出的 CSV
#     是按数值排过序的，不打乱的话每根柱子里的点会连成一条斜线
