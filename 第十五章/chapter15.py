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
#import matplotlib.pyplot as plt
#from pathlib import Path
#plt.style.use('seaborn-v0_8')
#path = Path('D:/代码/PY_test/第十五章/cubes_plot.png')

#x_values = range(1, 5001, 10)
#y_values = [x**3 for x in x_values]

#fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#ax.set_title('Cubes Numbers', fontsize=16, fontname='Times New Roman')
#ax.set_xlabel('Value', fontsize=14, fontname='Times New Roman')
#ax.set_ylabel('Cubes of value', fontsize=14, fontname='Times New Roman')

#ax.axis([0, 5001, 0, 125_000_000_000])
##ax.ticklabel_format(style='plain')
#plt.savefig(path, bbox_inches='tight', dpi=200)
#plt.show()

#-------------------------------------------------------------------------------
###15.3随机游走
###15.3.3绘制随机游走图
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

##创建一个RandomWalk 实例
#w = RandomWalk()
#rw.fill_walk()

##将所有的点都绘制出来
#plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#fig, ax = plt.subplots()
#ax.scatter(rw.x_values, rw.y_values, s=15, color = 'red' )
#ax.set_aspect('equal')
#plt.show()


#-------------------------------------------------------------------------------
###15.3.4模拟多次随机游走
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机游走
#while True:
#    #创建一个RandomWalk实例
#    rw = RandomWalk()
#    rw.fill_walk()
#    #将所有的点都绘制出来
#    plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#    fig, ax = plt.subplots()
#    ax.scatter(rw.x_values, rw.y_values, s=15)
#    ax.set_aspect('equal')
#    plt.show()

#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
#        break


#-------------------------------------------------------------------------------
###15.3.5设置随机游走图的样式
###01给点着色
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

##只要程序处于活跃状态，就不断地模拟随机游走
#while True:
#    #创建一个RandomWalk实例
#    rw = RandomWalk()
#    rw.fill_walk()
#    #将所有的点都绘制出来
#    plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#    fig, ax = plt.subplots()
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Reds,
#                edgecolors='none', s=15)
#    ax.set_aspect('equal')
#    plt.show()

#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
#        break

###02重新绘制起点和终点
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机游走
#while True:
#    #创建一个RandomWalk实例
#    rw = RandomWalk()
#    rw.fill_walk()
#    #将所有的点都绘制出来
#    plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#    fig, ax = plt.subplots()
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues,
#                edgecolors='none', s=15)
#    ax.set_aspect('equal')

#    #突出起点和终点
#    ax.scatter(0, 0, c='green', edgecolors='none', s = 100)
#    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s = 100)
#    plt.show()

#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
#        break

###03隐藏坐标轴
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

##只要程序处于活跃状态，就不断地模拟随机游走
#while True:
#    #创建一个RandomWalk实例
#    rw = RandomWalk(10000)        #在括号中添加数值可以改变游走的点数
#    rw.fill_walk()
#    #将所有的点都绘制出来
#    plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#    fig, ax = plt.subplots()
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues,
#                edgecolors='none', s=15)
#    ax.set_aspect('equal')

#    #突出起点和终点
#    ax.scatter(0, 0, c='green', edgecolors='none', s = 100)
#    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s = 100)

#    #隐藏坐标轴
#    ax.get_xaxis().set_visible(False)
#    ax.get_yaxis().set_visible(False)
#    plt.show()

#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
#        break

###05调整尺寸以适应屏幕
#import matplotlib.pyplot as plt
#from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机游走
#while True:
#    #创建一个RandomWalk实例
#    rw = RandomWalk(10000)        #在括号中添加数值可以改变游走的点数
#    rw.fill_walk()
#    #将所有的点都绘制出来
#    plt.style.use('classic')           #使用的是什么图，classic这个图的形式
#    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
#    point_numbers = range(rw.num_points)
#    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues,
#                edgecolors='none', s=15)
#    ax.set_aspect('equal')

#    #突出起点和终点
#    ax.scatter(0, 0, c='green', edgecolors='none', s = 100)
#    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s = 100)

#    #隐藏坐标轴
#    ax.get_xaxis().set_visible(False)
#    ax.get_yaxis().set_visible(False)
#    plt.show()

#    keep_running = input("Make another walk?(y/n): ")
#    if keep_running == 'n':
#        break


#-------------------------------------------------------------------------------
###练习15.3：分子运动
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, color = 'red', linewidth = 1)
    ax.set_aspect('equal')

    #突出起点和终点
    ax.scatter(0, 0, color = 'green', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], color = 'blue',s = 100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break

































































