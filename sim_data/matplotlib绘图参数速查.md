# Matplotlib 绘图参数速查（以 gain.py 为例）

对应文件：`python_png/gain.py`
目标效果：Origin 风格的波特图（对数横轴、黑色边框、Arial 粗体、方形网格）

---

## 0. 总体结构

```
读数据  →  设样式/字体(rcParams)  →  建画布(subplots)  →  画曲线(plot)
       →  设坐标轴(scale/lim/locator)  →  设外观(tick_params/spines/grid)
       →  加文字(text)  →  保存(savefig)  →  显示(show)
```

**顺序要求**：`plt.style.use()` 和 `plt.rcParams` 必须写在 `plt.subplots()` **之前**，否则不生效（画布已经建好了，样式改不动它）。

---

## 1. 全局样式与字体

### `plt.style.use(样式名)`
一键套用整套配色方案。

| 样式名 | 效果 |
|---|---|
| `'seaborn-v0_8'` | **灰色**背景 + 白网格 |
| `'seaborn-v0_8-whitegrid'` | 白底 + 灰网格，无外框 ← 当前使用 |
| `'seaborn-v0_8-white'` | 白底 + 四边黑框，默认无网格 |
| `'seaborn-v0_8-ticks'` | 白底 + 外框 + 明显刻度线，最接近论文风格 |
| `'default'` | matplotlib 原生 |

### `plt.rcParams[...]`
全局默认值，之后所有元素都继承。

```python
plt.rcParams['font.family']     = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']     # 字体名
plt.rcParams['font.weight']     = 'bold'        # 正文/刻度数字加粗
plt.rcParams['axes.labelweight']= 'bold'        # 坐标轴标题加粗
plt.rcParams['mathtext.fontset']= 'custom'      # 关键：10³ 这类指数的字体
plt.rcParams['mathtext.rm']     = 'Arial:bold'
```

> **为什么要设 mathtext**：横轴的 `10³` `10⁴` 是 matplotlib 用数学公式引擎渲染的，不单独设置的话会用默认的 DejaVu 字体，和其它文字不统一。

> 若报错 `findfont: Font family 'Arial' not found`，删掉缓存目录 `C:\Users\<用户名>\.matplotlib` 让它重建。

---

## 2. 画布与坐标范围

### `plt.subplots(figsize=(宽, 高))`
返回 `fig`（整张图）和 `ax`（坐标区）。`figsize` 单位是**英寸**，决定图的长宽比。

### `ax.set_xlim(下限, 上限)` / `ax.set_ylim(...)`
锁定坐标范围。不设的话 matplotlib 自动根据数据推断。

### `ax.set_aspect(比值, adjustable='box')`
**控制网格是不是正方形。**

含义：`比值 = y方向1个数据单位的长度 ÷ x方向1个数据单位的长度`。

log 轴上，x 的「1 个单位」= 1 个十倍频。所以想让 **1 个十倍频宽 = 10 dB 高**：

```python
ax.set_aspect(1/10, adjustable='box')
```

- `adjustable='box'`：靠压缩坐标框满足比例（数据范围不变），可能出现空白边
- 更省事的替代方案：不用 `set_aspect`，直接把 `figsize` 按「十倍频数 : 10dB格数」给。例如 x 跨 9 个十倍频、y 跨 7 个 10dB → `figsize=(9, 7)`
- 注意：**次网格的小格永远不可能是正方形**，因为 x 的次刻度是 log 分布（越靠右越密），y 是均分的

---

## 3. 画曲线 `ax.plot()`

```python
ax.plot(x, y, color='red', marker='s', markersize=3, markevery=1)
```

| 参数 | 作用 |
|---|---|
| `color` | 线的颜色 |
| `linewidth` / `lw` | 线宽 |
| `linestyle` / `ls` | 线型，见第 6 节 |
| `label` | 图例名字（配合 `ax.legend()`） |
| `marker` | 数据点标记形状 |
| `markersize` / `ms` | 标记大小 |
| `markevery` | **每隔几个点画一个标记** |
| `markerfacecolor` | 标记填充色，设 `'white'` 即空心 |
| `markeredgewidth` | 标记边框粗细 |

### marker 形状对照表

| 符号 | 形状 | 符号 | 形状 |
|---|---|---|---|
| `'o'` | 圆形 | `'s'` | 方形 |
| `'^' 'v' '<' '>'` | 上/下/左/右三角 | `'D'` `'d'` | 菱形 / 瘦菱形 |
| `'p'` | 五边形 | `'h'` `'H'` | 六边形 |
| `'*'` | 星形 | `'8'` | 八边形 |
| `'+'` `'x'` | 加号 / 叉 | `'.'` | 小点 |

### markevery 的几种写法
- `markevery=3` — 每 3 个数据点画一个（**数据密时必用**，否则标记糊成一片）
- `markevery=0.1` — 按曲线长度每 10% 放一个，log 轴上分布更均匀
- `markevery=(2, 5)` — 从第 2 个点起每 5 个画一个；几条线错开可避免标记重叠

---

## 4. 坐标轴类型 `ax.set_xscale()`

```python
ax.set_xscale('log')
```

| 值 | 效果 |
|---|---|
| `'linear'` | 线性（默认） |
| `'log'` | 对数 |
| `'symlog'` | 对数但允许 0 和负数，配 `linthresh=1e3` 指定线性区宽度 |

> **坑**：对数轴无法显示 `x = 0` 的点，该点会被静默丢弃。数据第一行若是 0 Hz，就少画一个点。

---

## 5. 刻度位置与格式（ticker 模块）

需要先导入：
```python
from matplotlib.ticker import LogLocator, LogFormatterSciNotation, NullFormatter, AutoMinorLocator
```

**四个概念要分清**：
- **Locator** = 刻度画在**哪里**
- **Formatter** = 刻度**写什么字**
- **major** = 主刻度（带数字、长线）
- **minor** = 次刻度（一般不带数字、短线）

### 横轴（对数）

```python
# 主刻度：每个十倍频一个，一个都不省略
ax.xaxis.set_major_locator(LogLocator(base=10.0, subs=(1.0,), numticks=100))

# 主刻度标签：10³ 这种科学计数法
ax.xaxis.set_major_formatter(LogFormatterSciNotation(base=10.0))

# 次刻度：每个十倍频内的 2、3 … 9 倍处
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=tuple(range(2,10)), numticks=100))

# 次刻度不写数字，否则挤成一团
ax.xaxis.set_minor_formatter(NullFormatter())
```

- `subs=(1.0,)` + `numticks=100` 是关键：不写的话 matplotlib 会**自动抽稀**，变成每两三个十倍频才标一个
- 想显示 `1M` `100k` 这种工程记法，把 formatter 换成 `EngFormatter(unit='Hz')`

### 纵轴（线性）

```python
ax.yaxis.set_minor_locator(AutoMinorLocator(5))
```
`AutoMinorLocator(n)` 的 **n 是把主刻度区间分成几段，不是插几根线**。分 5 段 = 插入 **4** 根次刻度线。

主刻度想每隔固定值一个，用：
```python
from matplotlib.ticker import MultipleLocator
ax.yaxis.set_major_locator(MultipleLocator(10))   # 每 10 dB 一个
```

---

## 6. 刻度线外观 `ax.tick_params()`

**注意区分三种「线」和它们各自的粗细参数：**

| 想改什么 | 用哪个 | 参数名 |
|---|---|---|
| 轴边上探出的**短刻度线** | `ax.tick_params()` | `width` |
| 贯穿整张图的**网格线** | `ax.grid()` | `linewidth` |
| 最外圈的**边框** | `spine.set_linewidth()` | — |

```python
ax.tick_params(axis='both', which='major',
               direction='in', length=5, width=1,
               top=False, right=False,
               color='black', labelcolor='black',
               labelsize=18, pad=8)
```

| 参数 | 作用 |
|---|---|
| `axis` | `'x'` / `'y'` / `'both'` |
| `which` | `'major'` / `'minor'` / `'both'` |
| `direction` | `'in'` 朝内 / `'out'` 朝外 / `'inout'` 穿过轴线 |
| `length` | 刻度线长度 |
| `width` | 刻度线粗细 |
| `top` `right` | 上边、右边要不要也画刻度（四边刻度设 `True`） |
| `color` | 刻度线颜色 |
| `labelcolor` | 刻度数字颜色 |
| `labelsize` | 刻度数字字号 |
| `pad` | **刻度数字离轴的距离**，默认 3.5，调大即数字往外移 |

> 多次调用 `tick_params` 只会覆盖你重复写到的参数，没写的保持不变，所以可以分几行分别设置。

---

## 7. 边框 `ax.spines`

`ax.spines` 是四条边框，键为 `'left'` `'right'` `'top'` `'bottom'`。

```python
# 四条全部黑色实线
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.2)
```

只保留左、下两条（论文常见）：
```python
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
```

> `whitegrid` 样式默认把边框设为浅灰甚至隐藏，所以要显式 `set_visible(True)`。

---

## 8. 网格 `ax.grid()`

```python
ax.grid(True, which='major', linestyle='-',   linewidth=0.35, alpha=0.6, color='dimgrey')
ax.grid(True, which='minor', dashes=(4, 4),   linewidth=0.3,  alpha=0.3, color='grey')
```

| 参数 | 作用 |
|---|---|
| `which` | `'major'` / `'minor'` / `'both'` |
| `axis` | `'x'` 只画竖线 / `'y'` 只画**横线** / `'both'` |
| `linestyle` | 线型 |
| `dashes` | 自定义虚线，`(线段长, 间隔长)`，单位 point |
| `linewidth` | 线粗 |
| `color` | 颜色 |
| `alpha` | 透明度，0 全透明、1 不透明 |

### 线型对照

| 写法 | 效果 |
|---|---|
| `'-'` | 实线 |
| `'--'` | 短横虚线 |
| `'-.'` | 点划线 |
| `':'` | 点线 |

> 只认 ASCII 的 `--`，中文破折号 `——` 会报错。

**虚线间隔想调大**：别用 `linestyle`，改用 `dashes=(线长, 间隔)`：
- `(4, 6)` 疏 ｜ `(2, 8)` 很稀疏、接近点状 ｜ `(6, 3)` 长划线密排
- `dashes` 和 `linestyle` 二选一，同时写 `linestyle` 会覆盖 `dashes`

### 颜色（灰度由浅到深）
`lightgrey` → `silver` → `darkgrey` → `grey` → `dimgrey`
也可以用灰度字符串 `color='0.3'`（0 黑、1 白）或 16 进制 `'#404040'`。

> 改深颜色时记得同步调高 `alpha`，否则透明度太高会被冲淡看不出区别。

---

## 9. 标题与轴标签

```python
ax.set_title('标题',  fontsize=24)
ax.set_xlabel('Frequency (Hz)', fontsize=18, fontweight='bold', labelpad=12)
ax.set_ylabel('Gain (dB)',      fontsize=18, fontweight='bold')
```

- `labelpad` — 标签离坐标轴的距离
- 更精细的定位：`ax.xaxis.set_label_coords(0.5, -0.12)`，第二个数越负越靠下

### 「往下移」的三种情况别搞混

| 想移动什么 | 用什么 |
|---|---|
| 刻度数字（`10³` 整体） | `ax.tick_params(axis='x', pad=8)` |
| 轴标题（`Frequency (Hz)`） | `set_xlabel(..., labelpad=12)` 或 `set_label_coords()` |
| 上标 `³` 相对 `10` 的高度 | **没有直接参数**，mathtext 写死的 |

第三种只能绕开：放弃 `LogFormatterSciNotation`，改用 `FuncFormatter` 输出不带上标的写法，就不存在角标高低问题了：

```python
from matplotlib.ticker import FuncFormatter, EngFormatter
ax.xaxis.set_major_formatter(EngFormatter(unit='Hz'))     # 显示成 1k / 100k / 1M
```

---

## 10. 添加文字 `ax.text()`

### 按**比例**定位（推荐，尤其是 log 轴）

```python
ax.text(0.99, 0.99, 'Gain',
        transform=ax.transAxes,          # 关键：切换到比例坐标
        fontsize=24, fontweight='bold', fontstyle='italic', color='black',
        ha='right', va='top')
```

- `transform=ax.transAxes` → 坐标变成**相对坐标框的比例**：`(0,0)` 左下角，`(1,1)` 右上角
- `ha` 水平对齐：`'left'` / `'center'` / `'right'`
- `va` 垂直对齐：`'top'` / `'center'` / `'bottom'`
- **放右上角必须配 `ha='right', va='top'`**，文字才以右上角为锚点向左下延伸，不会跑出图外；放左上角则用 `(0.02, 0.98)` + `ha='left'`

### 按**数据值**定位

去掉 `transform`，直接给真实数值：
```python
ax.text(2e5, 30.3, '30.1030dB', fontsize=14, color='red', va='center')
```

### 其它常用参数
```python
rotation=90,                                    # 旋转角度
bbox=dict(facecolor='white', edgecolor='black', alpha=0.8, pad=4)   # 加白底方框
```

### 带箭头的标注 `ax.annotate()`
```python
ax.annotate('说明文字',
            xy=(指向的数据点),          # 箭头尖端
            xytext=(文字所在位置),      # 文字位置
            arrowprops=dict(arrowstyle='->', color='black'))
```

---

## 11. 保存与显示

```python
plt.savefig(path_fig, bbox_inches='tight', dpi=1200)
plt.show()
```

- `bbox_inches='tight'` — 自动裁掉多余白边
- `dpi` — 分辨率。论文投稿一般 600~1200；预览用 150 就够，dpi 越高存图越慢
- **`savefig` 必须写在 `show()` 之前**，否则 `show()` 关闭窗口后画布被清空，存出来是空白图
- 存矢量图（论文最佳）：文件名后缀改成 `.pdf` 或 `.svg`，此时 `dpi` 不起作用

---

## 附：常见坑速查

| 现象 | 原因 |
|---|---|
| 样式/字体设置没生效 | 写在了 `plt.subplots()` 之后 |
| 存出来是空白图 | `savefig` 写在了 `show()` 之后 |
| log 轴少了一个点 | 该点 x = 0，对数轴无法显示 |
| 横轴刻度隔好几个才标一个 | `LogLocator` 没设 `subs=(1.0,)` 和 `numticks` |
| 次刻度只插了 1 根 | `AutoMinorLocator(2)` 的 2 是「分 2 段」，要 4 根得填 5 |
| 看不到刻度线 | seaborn 样式默认隐藏，需 `tick_params` 显式设 `length` |
| `linestyle='——'` 报错 | 用了中文破折号，必须是 ASCII 的 `--` |
| 标记连成一片糊住曲线 | 数据点太密，用 `markevery` 抽稀 |
| 改深了颜色却看不出变化 | `alpha` 太低把颜色冲淡了 |
