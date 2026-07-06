#-------------------------------------------------------------------------------
###15.2绘制简单的折线图
#import matplotlib.pyplot as plt

#squares = [1, 4, 9, 16, 25]

#fig, ax = plt.subplots()
#ax.plot(squares)

#plt.show()

#-------------------------------------------------------------------------------
###15.2.1修改标签文字和线条粗细
#import matplotlib.pyplot as plt
#这两行是为了在图表中显示中文标签和标题
#plt.rcParams['font.family'] = ['Microsoft YaHei']  # 微软雅黑
#plt.rcParams['axes.unicode_minus'] = False          # 防止负号显示异常


#squares = [1, 4, 9, 16, 25]

#fig, ax = plt.subplots()
#ax.plot(squares, linewidth=3)

###----设置图题并给坐标轴加上标签
#ax.set_title("平方数:Square number", fontsize=16)
#ax.set_xlabel(" values",fontsize=14)
#ax.set_ylabel(" Square of values",fontsize=14)

###----设置刻度标记的样式
#ax.tick_params(labelsize=14)

#plt.show()


#-------------------------------------------------------------------------------
###15.2.2校正绘图
#import matplotlib.pyplot as plt
#plt.rcParams['font.family'] = ['Microsoft YaHei']
#plt.rcParams['axes.unicode_minus'] = False

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]

#fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth=3)

####----设置图题并给坐标轴加上标签
#ax.set_title("平方数:Square number", fontsize=16)
#ax.set_xlabel("Values",fontsize=14)
#ax.set_ylabel("Square of values",fontsize=14)

###----设置刻度标记的样式
#ax.tick_params(labelsize=14)

#plt.show()

#-------------------------------------------------------------------------------
###15.2.3使用内置样式
#import matplotlib.pyplot as plt
#style = plt.style.available  # 查看所有可用的样式
#print(style)


################################查看所有样式#####################################
####import matplotlib.pyplot as plt
####plt.rcParams['font.family'] = ['Microsoft YaHei']
####plt.rcParams['axes.unicode_minus'] = False

####squares = [1, 4, 9, 16, 25]

####for style in plt.style.available:
####    plt.style.use(style)
####    fig, ax = plt.subplots()
####    ax.plot(squares)
####    ax.set_title(style)  # 标题显示样式名字
####    plt.show()



#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')  # 使用seaborn样式
#plt.rcParams['font.family'] = ['Microsoft YaHei']
#plt.rcParams['axes.unicode_minus'] = False

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]

#fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth = 3)
#ax.set_title("平方数:Square number", fontsize=16)
#ax.set_xlabel("values", fontsize=14)
#ax.set_ylabel("Square of values", fontsize=14)

#ax.tick_params(labelsize=14)

#plt.show()

#-------------------------------------------------------------------------------
###15.2.4使用scatter绘制散点图并设置样式
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')
#fig, ax = plt.subplots()
#ax.scatter(2, 4, s=200)

##设置图题并给坐标轴加上标签
#ax.set_title('Square Numbers', fontsize = 16)
#ax.set_xlabel('Value', fontsize = 14)
#ax.set_ylabel('Square of value', fontsize = 14)

#设置刻度标记的样式
#ax.tick_params(labelsize = 14)

#plt.show()


#-------------------------------------------------------------------------------
###15.2.5使用scatter()绘制一系列散点图
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=100)

#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)
#ax.set_title('Square Numbers', fontsize=16)

#ax.tick_params(labelsize=14)

#plt.show()

#-------------------------------------------------------------------------------
###15.2.6自动计算数据
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')

#x_values = range(1, 1001)
#y_values = [x**2 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s = 10)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)
#ax.set_title('Square Numbers', fontsize=16)

##设置每个坐标轴的取值范围
#ax.axis([0, 1100, 0, 1_100_000])
#plt.show()

#-------------------------------------------------------------------------------
###15.2.7定制刻度标记
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')

#x_values = range(1, 1001, 50)
#y_values = [x**2 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s = 10)
#ax.set_title('Square Numbers', fontsize=16)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)

#ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style = 'plain')  # 设置刻度标记的样式为plain(普通计数法)
#plt.show()

#-------------------------------------------------------------------------------
###15.2.8定制颜色
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')

#x_values = range(1, 1001, 10)
#y_values = [x**2 for x in x_values]

#fig, ax = plt.subplots()
##ax.scatter(x_values, y_values, s = 10, color = 'red')
#ax.scatter(x_values, y_values, s = 10, color = (0, 0.8, 0))
#ax.set_title('Square Numbers', fontsize=16)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)

#ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style = 'plain')
#plt.show()

#-------------------------------------------------------------------------------
###15.2.9使用颜色映射
#import matplotlib.pyplot as plt
#plt.style.use('seaborn-v0_8')

#x_values = range(1, 1001, 10)
#y_values = [x**2 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Reds, s = 100)#颜色映射
##颜色映射可以：值越大颜色越深，值越小颜色越浅，或：温度越高颜色越深，温度越低颜色越浅

#ax.set_title('Square Numbers', fontsize=16)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)

#ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style = 'plain')
#plt.show()


#-------------------------------------------------------------------------------
###15.2.10自动保存绘图
#import matplotlib.pyplot as plt
#from pathlib import Path
#plt.style.use('seaborn-v0_8')

#x_values = range(1, 1001, 10)
#y_values = [x**2 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

#ax.set_title('Square Numbers', fontsize=16)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Square of value', fontsize=14)

#ax.axis([0, 1100, 0, 1_100_000])
#ax.ticklabel_format(style='plain')
#path = Path('D:/代码/PY_test/第十五章\squares_plot_1.png')  # 设置保存路径
#plt.savefig(path, bbox_inches='tight', dpi=500)  # 保存绘图
##格式，'mingzi.png'，bbox_inches='tight'表示去掉多余的空白区域，这个dpi是调整图片的清晰度，dpi越大，图片越清晰
#plt.show()

#-------------------------------------------------------------------------------
###练习15.1：立方
###前五个正整数的立方数
#import matplotlib.pyplot as plt
#from pathlib import Path
#plt.style.use('seaborn-v0_8')
#path = Path('D:/代码/PY_test/第十五章/cubes_plot.png')

#x_values = range(1, 6, 1)
#y_values = [x**3 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=100)

#ax.set_title('Cubes Numbers', fontsize=16)
#ax.set_xlabel('Value', fontsize=14)
#ax.set_ylabel('Cubes of value', fontsize=14)

#ax.axis([0, 6, 0, 150])
#ax.ticklabel_format(style='plain')
#plt.savefig(path, bbox_inches='tight', dpi=500)
#plt.show()

###前5000个正整数的立方数
import matplotlib.pyplot as plt
from pathlib import Path
plt.style.use('seaborn-v0_8')
path = Path('D:/代码/PY_test/第十五章/cubes_plot.png')

x_values = range(1, 5001, 10)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('Cubes Numbers', fontsize=16, fontname='Times New Roman')
ax.set_xlabel('Value', fontsize=14, fontname='Times New Roman')
ax.set_ylabel('Cubes of value', fontsize=14, fontname='Times New Roman')

ax.axis([0, 5001, 0, 125_000_000_000])
#ax.ticklabel_format(style='plain')
plt.savefig(path, bbox_inches='tight', dpi=200)
plt.show()












































