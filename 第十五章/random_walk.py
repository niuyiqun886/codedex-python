#-------------------------------------------------------------------------------
###15.3.1创建Randomwalk类
from random import choice

class RandomWalk:
    def __init__(self, num_points = 5000):
        """初始化随机游走的属性"""
        self.num_points = num_points

        #所有随机游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
#-------------------------------------------------------------------------------
###15.3.2选择方向
#    def fill_walk(self):
#        """计算随机游走包含的所有点"""

#        #不断游走，直到列表达到了指定的长度
#        while len(self.x_values) < self.num_points:

#            #决定前进的方向以及沿这个方向前进的距离
#            x_direction = choice([1,-1])
#            x_distance = choice([0, 1, 2, 3, 4])
#            x_step = x_direction * x_distance

#            y_direction = choice([1,-1])
#            y_distance = choice([0, 1, 2, 3, 4])
#            y_step = y_direction * y_distance        
            
#            #拒绝原地踏步
#            if x_step == 0 and y_step == 0:
#                continue

#            #计算下一个点的x坐标值和y坐标值
#            x = self.x_values[-1] + x_step   #表示最后一个的self.x_values的值加上x_step即走的长度
#            y = self.y_values[-1] + y_step

#            self.x_values.append(x)
#            self.y_values.append(y)


#重新构造，定义get_step函数可以简化写法
    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance
        

    def fill_walk(self):
        """计算随机游走包含的所有点"""

        #不断游走，直到列表达到了指定的长度
        while len(self.x_values) < self.num_points:

            #决定前进的方向以及沿这个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()    
            
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x坐标值和y坐标值
            x = self.x_values[-1] + x_step   #表示最后一个的self.x_values的值加上x_step即走的长度
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


