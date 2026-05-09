#第9章 类
#9.1创建和使用类
#9.1.1 创建Dog类
class Dog:#首字母大写指的是类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):      #这里相当于是self python自动传入名字为my_dog，然后给my_dog起名字，一个是name，一个是age。
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令坐下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """摩西小狗收到命令是打滚"""
        print(f"{self.name} rolled over!")

#9.1.2 根据类创建实例
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#调用方法
my_dog.sit()
my_dog.roll_over()

#创建多个实例
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


























































































































































