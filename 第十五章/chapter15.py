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



import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')  # 使用seaborn样式
plt.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
ax.set_title("平方数:Square number", fontsize=16)
ax.set_xlabel("values", fontsize=14)
ax.set_ylabel("Square of values", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()








































































