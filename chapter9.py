#第9章 类
#9.1创建和使用类
#9.1.1 创建Dog类
#class Dog:#首字母大写指的是类
#    """一次模拟小狗的简单尝试"""
#    def __init__(self, name, age):      #这里相当于是self python自动传入名字为my_dog，然后给my_dog起名字，一个是name，一个是age。
#        self.name = name
#        self.age = age

#    def sit(self):
#        """模拟小狗收到命令坐下"""
#        print(f"{self.name} is now sitting.")

#    def roll_over(self):
#        """摩西小狗收到命令是打滚"""
#        print(f"{self.name} rolled over!")

#9.1.2 根据类创建实例
#my_dog = Dog('Willie', 6)
#print(f"My dog's name is {my_dog.name}.")
#print(f"My dog is {my_dog.age} years old.")

#调用方法
#my_dog.sit()
#my_dog.roll_over()

#创建多个实例
#your_dog = Dog('Lucy', 3)
#print(f"Your dog's name is {your_dog.name}.")
#print(f"Your dog is {your_dog.age} years old.")
#your_dog.sit()

#练习9.1 餐馆 
#class Restaurant:
#    def __init__(self, restaurant_name, restaurant_type):
#        self.restaurant_name = restaurant_name
#        self.restaurant_type = restaurant_type

#    def describe_restaurant(self):
#        """餐馆的两项信息"""
#        print(f"The restaurant's name is {self.restaurant_name}.")
#        print(f"This is a {self.restaurant_type} restaurant.")

#    def open_restaurant(self):
#        print("This restaurant is opening today.")

#restaurant = Restaurant('Star bark', 'America')
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

#restaurant1 = Restaurant('Lanzhou Lamian', 'Chinese')
#restaurant1.describe_restaurant()
#restaurant1.open_restaurant()

#restaurant2 = Restaurant('Re ganmian', 'Wu Han')
#restaurant2.describe_restaurant()
#restaurant2.open_restaurant()

#练习 9.2：三家餐馆
#restaurant3 = Restaurant('Guo baorou', 'Harbin')
#restaurant3.describe_restaurant()

#restaurant4 = Restaurant('Cu yu', 'Hang Zhou')
#restaurant4.describe_restaurant()

#restaurant5 = Restaurant('Hot pot', 'Si Chuan')
#restaurant5.describe_restaurant()

#练习 9.3：用户
#class User:
#    def __init__(self, first_name, last_name):
#       self.first_name = first_name
#       self.last_name = last_name

#    def describe_user(self):
#        """用于打印用户信息摘要"""
#        print(f"This user's name is {self.first_name} {self.last_name}.")

#    def greet_user(self):
#        """用于向用户发出个性化的问候"""
#        print(f"Welcome to our website, {self.first_name}!")

#user1 = User('Niu', 'yiqun')
#user1.describe_user()
#user1.greet_user()

#9.2 使用类和实例
#9.2.1 Car 类
#class Car:
#    """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()
        
#my_new_car = Car('audi', 'a4', '2024')
#print(my_new_car.get_descriptive_name())

#9.2.2 给属性指定默认值
#class Car:
#   """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#       self.odometer_reading = 0
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()

#    def read_odometer(self):
#        """打印一条指出汽车行驶里程的消息"""
#        print(f"This car has {self.odometer_reading} miles on it.")

#my_new_car = Car('audi', 'a4', '2024')
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#9.2.3 修改属性的值
#01直接修改属性值，可以直接赋值给odometer_reading
#my_new_car.odometer_reading = 23
#my_new_car.read_odometer()
#02通过方法修改属性的值
#class Car:
#    """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()

#    def read_odometer(self):
#        """打印一条指出汽车行驶里程的消息"""
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self,mileage):
#        """这里里程表的读数设置为指定值"""
#        self.odometer_reading = mileage

        
#my_new_car = Car('audi', 'a4', '2024')
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#03通过方法让属性的值递增
#class Car:
#    """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 10
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()

#    def read_odometer(self):
#        """打印一条指出汽车行驶里程的消息"""
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self,mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        """让里程表读数增加指定的量"""
#        self.odometer_reading += miles

#my_used_car = Car('subaru', 'outback', '2019')
#print(my_used_car.get_descriptive_name())

#my_used_car.update_odometer(23_500)
#my_used_car.read_odometer()

#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()


#练习9.4 餐馆人数
#class Restaurant:
#    def __init__(self, restaurant_name, restaurant_type):
#        self.restaurant_name = restaurant_name
#        self.restaurant_type = restaurant_type
#        self.number_served = 0    

#    def describe_restaurant(self):
#        """餐馆的两项信息"""
#        print(f"The restaurant's name is {self.restaurant_name}.")
#        print(f"This is a {self.restaurant_type} restaurant.")

#    def open_restaurant(self):
#        print("This restaurant is opening today.")

#    def set_number_served(self,number):
#        self.number_served = number
#        print(f"There are {self.number_served} people in this restaurant.")

#    def increment_number_served(self,number_n):
#        self.number_served += number_n
#        print(f"There are {self.number_served} people in this restaurant.")


#restaurant = Restaurant('Star bark', 'America')
#restaurant.describe_restaurant()
#restaurant.open_restaurant()
#restaurant.set_number_served(5)

#restaurant.increment_number_served(2)


#练习9.5 :尝试登录次数
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
       
    def describe_user(self):
        """用于打印用户信息摘要"""
        print(f"This user's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        """用于向用户发出个性化的问候"""
        print(f"Welcome to our website, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

user1 = User('Niu', 'yiqun')
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()









































































































