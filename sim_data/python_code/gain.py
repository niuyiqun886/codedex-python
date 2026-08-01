"""绘制增益波特图：对数横轴 + Origin 风格外观。

数据来源：sim_csv/gain.csv，第0列为频率，第1~4列为四条增益曲线。
参数含义见 matplotlib绘图参数速查.md
"""

from pathlib import Path
import csv

import matplotlib.pyplot as plt
from matplotlib.ticker import (LogLocator, LogFormatterSciNotation,
                               NullFormatter, AutoMinorLocator)


# ============================================================
# 配置
# ============================================================
PATH_CSV = Path(r'D:\代码\PY_test\sim_data\csv_data\gain.csv')
PATH_PNG = Path(r'D:\代码\PY_test\sim_data\png\gain.png')

X_LIM = (1e-3, 1e7)             #横轴范围（Hz）
Y_LIM = (-20, 55)               #纵轴范围（dB）

#四条曲线的 (颜色, 标记形状)
CURVES = [('red',    's'),      #方形
          ('green',  'D'),      #菱形
          ('blue',   'o'),      #圆形
          ('orange', '^')]      #三角形


# ============================================================
# 读取数据
# ============================================================
lines = PATH_CSV.read_text().splitlines()
reader = csv.reader(lines)

header_row = next(reader)
for index, column in enumerate(header_row):
    print(index, column)

rows = list(reader)
freq = [float(row[0]) for row in rows]                          #频率
gains = [[float(row[i]) for row in rows] for i in range(1, 5)]  #四条增益曲线


# ============================================================
# 全局样式（必须在 subplots 之前）
# ============================================================
plt.style.use('seaborn-v0_8-whitegrid')               #白底 + 灰网格

#字体：Arial 粗体（Origin 风格）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['font.weight'] = 'bold'                  #正文/刻度数字加粗
plt.rcParams['axes.labelweight'] = 'bold'             #坐标轴标题加粗
plt.rcParams['mathtext.fontset'] = 'custom'           #让 10³ 这类指数也用 Arial 粗体
plt.rcParams['mathtext.rm'] = 'Arial:bold'
plt.rcParams['mathtext.it'] = 'Arial:bold'
plt.rcParams['mathtext.bf'] = 'Arial:bold'


# ============================================================
# 画曲线
# ============================================================
fig, ax = plt.subplots(figsize = (9, 7))

for gain, (color, marker) in zip(gains, CURVES):
    ax.plot(freq, gain, color = color,
            marker = marker, markersize = 3, markevery = 1)


# ============================================================
# 坐标轴：范围、类型、刻度位置
# ============================================================
ax.set_xscale('log')            #对数横轴（频率为0的点会被自动忽略）
ax.set_xlim(*X_LIM)
ax.set_ylim(*Y_LIM)

#横轴：主刻度每十倍频一个，次刻度落在 2~9 倍处
ax.xaxis.set_major_locator(LogLocator(base = 10.0, subs = (1.0,), numticks = 100))
ax.xaxis.set_major_formatter(LogFormatterSciNotation(base = 10.0))
ax.xaxis.set_minor_locator(LogLocator(base = 10.0, subs = tuple(range(2, 10)), numticks = 100))
ax.xaxis.set_minor_formatter(NullFormatter())       #次刻度只画线，不写数字

#纵轴：参数是分成几段，5段 = 两个主刻度间插4个次刻度
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

#1个十倍频(x) 的宽度 = 10 dB(y) 的高度，使主网格为正方形
ax.set_aspect(1 / 10, adjustable = 'box')


# ============================================================
# 外观：刻度线、边框、网格
# ============================================================
ax.tick_params(axis = 'both', which = 'major', direction = 'in',
               length = 5, width = 1, top = False, right = False,
               color = 'black', labelcolor = 'black', labelsize = 18)
ax.tick_params(axis = 'both', which = 'minor', direction = 'in',
               length = 2.5, width = 1, top = False, right = False,
               color = 'black')
ax.tick_params(axis = 'x', which = 'major', pad = 8)    #横轴刻度数字向下移

#四周边框：黑色实线
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.2)

ax.grid(True, which = 'major', linestyle = '-', linewidth = 0.35,
        alpha = 0.6, color = 'dimgrey')                 #贯穿的实线
ax.grid(True, which = 'minor', dashes = (4, 4), linewidth = 0.3,
        alpha = 0.3, color = 'grey')                    #贯穿的虚线，(线长, 间隔)


# ============================================================
# 文字标注
# ============================================================
ax.set_xlabel('Frequency (Hz)', fontsize = 18, fontweight = 'bold')
ax.set_ylabel('Gain (dB)', fontsize = 18, fontweight = 'bold')

#transform=ax.transAxes：(0,0)是左下角，(1,1)是右上角
ax.text(0.99, 0.99, 'Gain', transform = ax.transAxes,
        fontsize = 24, fontweight = 'bold', fontstyle = 'italic',
        color = 'black', ha = 'right', va = 'top')

#按数据坐标定位
ax.text(2e5, 30.3, '30.1030dB', fontsize = 14, color = 'red', va = 'center')


# ============================================================
# 保存（必须在 show 之前）
# ============================================================
plt.savefig(PATH_PNG, bbox_inches = 'tight', dpi = 1200)
plt.show()


# ============================================================
# 换新数据时的修改清单
# ============================================================
#
# 【必改】
#
# 1. 文件路径 —— 第18、19行
#    PATH_CSV 改成新的 csv；PATH_PNG 改新名字，否则会覆盖旧图。
#
# 2. 曲线条数 —— 第43行 range(1, 5) 和 第25~28行 CURVES
#    range(1, 5) 表示读第1~4列（不含5）。
#      6条曲线 → range(1, 7)，同时 CURVES 补到6项；
#      不确定几列时，先看开头 print 出来的列号，或直接用
#      gains = [[float(row[i]) for row in rows] for i in range(1, len(header_row))]
#    CURVES 少于曲线数时 zip 会静默丢掉多余曲线，图上会少线，注意核对。
#
# 3. 坐标范围 —— 第21、22行 X_LIM / Y_LIM
#    先注释掉 set_xlim/set_ylim（第76、77行）跑一次看自动范围，再回填。
#    Y_LIM 建议取 10 的整数倍，主刻度才落在整十位上。
#
# 4. 正方形网格的比例 —— 第89行 set_aspect(1/10)
#    含义是「1个十倍频 = 多少 dB」。纵轴主刻度若不是 10 dB 一格要改：
#      20 dB 一格 → set_aspect(1/20)
#    同时第65行 figsize 建议按 (十倍频个数, 10dB格数) 给，
#    否则图会被压扁或留大片空白。
#      当前：x 跨 10^-3~10^7 = 10个十倍频，y 跨 -20~55 ≈ 7.5格 → (9, 7) 接近
#
# 5. 文字标注 —— 第122、127行
#    ax.text(2e5, 30.3, '30.1030dB', ...) 是按数据坐标写死的，
#    新数据的增益值变了必须改，否则标签会指错位置。
#    可以改成自动取值：
#      g0 = gains[0][0]
#      ax.text(2e5, g0 + 0.3, f'{g0:.4f}dB', fontsize=14, color='red')
#
#
# 【按需改】
#
# 6. 轴标签 —— 第118、119行
#    画相位图就改成 'Phase (deg)'，右上角第122行的 'Gain' 一起改。
#
# 7. 标记密度 —— 第69行 markevery
#    数据点变多时标记会糊成一片，改成 markevery=3 或 5 抽稀。
#
# 8. 出图分辨率 —— 第133行 dpi
#    调参阶段用 dpi=150 存得快，定稿再调回 1200。
#
#
# 【容易忘的坑】
#
# - csv 第一行必须是表头，否则 next(reader) 会吃掉一行真实数据。
# - 频率为 0 的点在对数轴上画不出来，会被静默丢弃。
# - 数据列数不足 5 列时，第43行会直接 IndexError。
