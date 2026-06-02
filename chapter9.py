#第9章 类
#9.1创建和使用类
#9.1.1 创建Dog类
#class Dog:#首字母大写指的是类，__init__称为方法
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
#class User:
#   def __init__(self, first_name, last_name):
#        self.last_name = last_name
#        self.login_attempts = 0
       
#    def describe_user(self):
#        """用于打印用户信息摘要"""
#        print(f"This user's name is {self.first_name} {self.last_name}.")

#    def greet_user(self):
#        """用于向用户发出个性化的问候"""
#        print(f"Welcome to our website, {self.first_name}!")

#    def increment_login_attempts(self):
#        self.login_attempts += 1
#        print(self.login_attempts)

#    def reset_login_attempts(self):
#        self.login_attempts = 0
#        print(self.login_attempts)

#user1 = User('Niu', 'yiqun')
#user1.describe_user()
#user1.greet_user()
#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.increment_login_attempts()
#user1.reset_login_attempts()

#9.3继承
#9.3.1子类的__init__()方法,定义一个子类，包含父类的所有特征
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

#   def update_odometer(self,mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        """让里程表读数增加指定的量"""
#        self.odometer_reading += miles
    
#    def fill_gas_tank(self):
#        print(f"This car has a gas tank.")

#class ElectricCar(Car):  #定义子类的时候必须在括号内指定父类名称。
#    """电动汽车的独特之处"""
#    def __init__(self, make, model, year):
#        """初始化父类的属性"""
#        super().__init__(make, model, year)  #是一个特殊的函数，然你可以调用父类的方法。
#        #父类也称为“超类”superclass，函数名由此得名。
#        self.battery_size = 40

#    def describe_battery(self):
#        """打印一条描述电池容量的消息"""
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def fill_gas_tank(self):
#        """电动汽车没有油箱"""
#        print("This car doesn't have a gas tank!")

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())
#my_leaf.describe_battery()

#my_leaf.fill_gas_tank()
#my_car = Car('Toyota', 'badao', 2018)
#print(my_car.get_descriptive_name())


#9.3.3重写父类中的方法

#9.3.4 将实例用作属性
#class Car:
#    """一次模拟汽车的简单尝试"""
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#       self.odometer_reading = 10
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()
#class Battery:
#    """一次模拟电动汽车电池的简单尝试"""
#    def __init__(self, battery_size=40):
#        """初始化电池属性"""
#        self.battery_size = battery_size

#    def describe_battery(self):
#        """打印出一条电池容量的消息"""
#        print(f"This car has a {self.battery_size}-kWh battery.")
        
#class ElectricCar(Car):  #定义子类的时候必须在括号内指定父类名称。
#    """电动汽车的独特之处"""
#   def __init__(self, make, model, year):
#        """先初始化父类的属性，在初始化电动汽车特有属性"""
#        super().__init__(make, model, year)
#        self.battery = Battery()

#y_leaf = ElectricCar('nissan', 'leaf', 2024)
#rint(my_leaf.get_descriptive_name())
#my_leaf.battery.describe_battery()


#虽然看似做了很多额外的工作，但是现在想编辑电池的信息，就不会导致ElectricCar混乱
#class Car:
#    """一次模拟汽车的简单尝试"""
#   def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#       self.year = year
#       self.odometer_reading = 10
        
#    def get_descriptive_name(self):
#        """返回格式规范的描述性信息"""
#        long_name = f"{self.year} {self.make}, {self.model}"
#        return long_name.title()
#class Battery:
#    """一次模拟电动汽车电池的简单尝试"""
#    def __init__(self, battery_size=40):
#        """初始化电池属性"""
#        self.battery_size = battery_size

#    def describe_battery(self):
#        """打印出一条电池容量的消息"""
#        print(f"This car has a {self.battery_size}-kWh battery.")
    
#    def get_range(self):
#        """打印一条消息，指出电池续航里程"""
#        if self.battery_size == 40:
#            range = 150
#        elif self.battery_size ==65:
#            range ==225
#        print(f"This car can go about {range} miles on a full charge.")


#class ElectricCar(Car):  #定义子类的时候必须在括号内指定父类名称。
#    """电动汽车的独特之处"""
#    def __init__(self, make, model, year):
#        """先初始化父类的属性，在初始化电动汽车特有属性"""
#        super().__init__(make, model, year)
#        self.battery = Battery()

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())
#my_leaf.battery.describe_battery()
#my_leaf.battery.get_range()


#练习9.6 餐馆 
#class Restaurant:
#    def __init__(self, restaurant_name, restaurant_type):
#        self.restaurant_name = restaurant_name
#        self.restaurant_type = restaurant_type

#   def describe_restaurant(self):
#        """餐馆的两项信息"""
#        print(f"The restaurant's name is {self.restaurant_name}.")
#        print(f"This is a {self.restaurant_type} restaurant.")

#    def open_restaurant(self):
#        print("This restaurant is opening today.")

#class IceCreamStand(Restaurant):
#    def __init__(self,restaurant_name,restaurant_type):
#        super().__init__(restaurant_name,restaurant_type)
#        self.flavors = []

#    def show_flavors(self):
#        for flavor in self.flavors:
#            print(flavor)


#my_stand = IceCreamStand('Cold Stone', 'Ice cream')
#y_stand.flavors.append('chocolate')
#my_stand.flavors.append('vanilla')
#my_stand.show_flavors()


#练习 9.7：管理员
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


#class Admin(User):
#    def __init__(self, first_name, last_name):
#        super().__init__(first_name, last_name)
#        self.privileges = []

#    def show_privileges(self):
#        for privilege in self.privileges:
#            print(privilege)



#admin1 = Admin('Niu', 'yiqun')
#admin1.privileges.append('can add post')
#admin1.privileges.append('can delete post')
#admin1.privileges.append('can ban user')
#admin1.show_privileges()



####再学一遍9.2使用类和实例
#9.2.1Car 类
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make          #这三行是将实例中的内容永久的存储在左侧的三个self.xxx上
#        self.model = model
#        self.year = year

#   def get_descriptive_name(self):  #定义一个get_descriptive_name()的方法
#        long_name = f"{self.year} {self.make} {self.model}"
#        #return long_name.title()
#        print(long_name)

#my_new_car = Car('audi', 'a4', 2024)   #根据Car类创建一个实例
#print(my_new_car.make)
#print(my_new_car.get_descriptive_name())
#my_new_car.get_descriptive_name()

#9.2.2 给属性指定默认值
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make          #这三行是将实例中的内容永久的存储在左侧的三个self.xxx上
#        self.model = model
#        self.year = year
#       self.odometer_reading = 0   #添加一个名为odometer_reading的属性，初始值为0

#    def get_descriptive_name(self):  #定义一个get_descriptive_name()的方法
#        long_name = f"{self.year} {self.make} {self.model}"
#        #return long_name.title()
#        print(long_name)

#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")


#my_new_car = Car('audi', 'a4', 2024)   #根据Car类创建一个实例
#print(my_new_car.make)
#print(my_new_car.get_descriptive_name())
#my_new_car.get_descriptive_name()
#01直接修改属性值
#my_new_car.odometer_reading = 23    #可以使用这个修改默认值
#my_new_car.read_odometer()
#print(my_new_car.odometer_reading)

#02 通过方法修改属性值
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make          #这三行是将实例中的内容永久的存储在左侧的三个self.xxx上
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0   #添加一个名为odometer_reading的属性，初始值为0

#    def get_descriptive_name(self):  #定义一个get_descriptive_name()的方法
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)

#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        self.odometer_reading = mileage

#my_new_car = Car('audi', 'a4', 2024)   #根据Car类创建一个实例
#print(my_new_car.make)
#my_new_car.get_descriptive_name()
#my_new_car.read_odometer()
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#class Car:
#    def __init__(self, make, model, year):
#        self.make = make          #这三行是将实例中的内容永久的存储在左侧的三个self.xxx上
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0   #添加一个名为odometer_reading的属性，初始值为0

#    def get_descriptive_name(self):  #定义一个get_descriptive_name()的方法
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)

#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")
        

#my_new_car = Car('audi', 'a4', 2024)   #根据Car类创建一个实例
#print(my_new_car.make)
#my_new_car.get_descriptive_name()
#my_new_car.read_odometer()
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#03通过方法让属性的值递增
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make          #这三行是将实例中的内容永久的存储在左侧的三个self.xxx上
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0   #添加一个名为odometer_reading的属性，初始值为0

#    def get_descriptive_name(self):  #定义一个get_descriptive_name()的方法
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)

#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        self.odometer_reading += miles


#my_used_car = Car('subaru', 'outback', 2019)   #根据Car类创建一个实例
#my_used_car.get_descriptive_name()
#my_used_car.update_odometer(23)
#my_used_car.read_odometer()
#my_used_car.increment_odometer(100)
#my_used_car.read_odometer()

#练习9.4：就餐人数
#class Restaurant:
#    def __init__(self, restaurant_name, cuisine_type):
#        self.restaurant_name = restaurant_name
#        self.cuisine_type = cuisine_type
#        self.number_served = 0

#    def describe_restaurant(self):
#        print(f"The restaurant's name is {self.restaurant_name}.")
#        print(f"This is a {self.cuisine_type} restaurant.")

#    def open_restaurant(self):
#        print("This restaurant is opening today.")

#    def set_number_served(self, number):
#        self.number_served = number

#    def increase_number_served(self, number):\
#        self.number_served += number

##restaurant = Restaurant('Star bark', 'America')
##restaurant.describe_restaurant()
##restaurant.open_restaurant()
##print(f"There are {restaurant.number_served} people in this restaurant.")   ###这里需要使用实例名字restaurant.number_served = 20
##restaurant.number_served = 20  ###这样可以直接赋值给内部的这个属性
##print(f"There are {restaurant.number_served} people in this restaurant.")

###restaurant = Restaurant('Star bark', 'America')
###restaurant.set_number_served(20)
###print(f"There are {restaurant.number_served} people in this restaurant.")

#restaurant = Restaurant('Star bark', 'America')
#restaurant.set_number_served(20)
#rint(f"There are {restaurant.number_served} people in this restaurant.")
#estaurant.increase_number_served(5)
#rint(f"There are {restaurant.number_served} people in this restaurant.")


#练习9.5:尝试登录次数
#class User:
#    def __init__(self, first_name, last_name):
#       self.first_name = first_name
#        self.last_name = last_name
#        self.login_attempts = 0

#    def describe_user(self):
#        print(f"This user's name is {self.first_name} {self.last_name}.")

#    def greet_user(self):
#        print(f"Welcome to our website, {self.first_name}!")

#    def increament_login_attempts(self):
#        self.login_attempts += 1

#    def reset_login_attempts(self):
#        self.login_attempts = 0

##user1 = User('Niu', 'yiqun')
##user1.describe_user()
##user1.greet_user()

##user2 = User('Li', 'hua')
##user2.describe_user()
##user2.greet_user()

#user = User('Wang', 'wu')
#user.describe_user()
#user.greet_user()
#user.increament_login_attempts()
#user.increament_login_attempts()
#user.increament_login_attempts()
#print(f"Login attempts: {user.login_attempts}")
#user.reset_login_attempts()
#print(f"Login attempts: {user.login_attempts}")


#9.3继承
#9.3.1子类的__init__()方法
#class Car:
#    def __init__(self, make, model, year):
#       self.make = make
#        self.model = model
#        self.year = year
#       self.odometer_reading = 0

#    def get_descriptive_name(self):
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)
    
#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#       self.odometer_reading += miles

#class ElectricCar(Car):  ###定义子类的时候必须在括号内指定父类名称。
#    def __init__(self, make, model, year):
#       super().__init__(make, model, year)   ###super()是一个特殊的函数，让你可以调用父类的方法。父类也称为“超类”superclass，函数名由此得名。

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#my_leaf.get_descriptive_name()

#9.3.2 给子类定义属性和方法
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0

#    def get_descriptive_name(self):
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)
    
#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        self.odometer_reading += miles

#class ElectricCar(Car):  ###定义子类的时候必须在括号内指定父类名称。
#    def __init__(self, make, model, year):
#        super().__init__(make, model, year)   ###super()是一个特殊的函数，让你可以调用父类的方法。父类也称为“超类”superclass，函数名由此得名。
#        self.battery_size = 40

#    def describe_battery(self):
#        print(f"This car has a {self.battery_size}-kWh battery.")


#my_car = Car('Toyota', 'badao', 2018)
#my_car.increment_odometer(100)
#my_car.read_odometer()
##my_car.describe_battery()  ###Car类没有这个方法，所以会报错
#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#my_leaf.get_descriptive_name()
#my_leaf.describe_battery()


#9.3.3 重写父类中的方法
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0

#    def get_descriptive_name(self):
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)
    
#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#           self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#       self.odometer_reading += miles

#    def fill_gas_tank(self):
#        print(f"This car has a gas tank.")

#class ElectricCar(Car):  ###定义子类的时候必须在括号内指定父类名称。
#    def __init__(self, make, model, year):
#        super().__init__(make, model, year)   ###super()是一个特殊的函数，让你可以调用父类的方法。父类也称为“超类”superclass，函数名由此得名。
#        self.battery_size = 40

#    def describe_battery(self):
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def fill_gas_tank(self):  ###如果有人对ElectricCar实例调用fill_gas_tank()，Python将忽略Car类中的这个方法，而只运行ElectricCar类中的这个方法。
#        print("This car doesn't have a gas tank!")

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#my_leaf.get_descriptive_name()
#my_leaf.describe_battery()
#my_leaf.fill_gas_tank()###只运行电车中的这个方法，不运行父类中的这个方法



#9.3.4 将实例用作属性
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0

#    def get_descriptive_name(self):
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)
    
#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        self.odometer_reading += miles

#    def fill_gas_tank(self):
#        print(f"This car has a gas tank.")

#class Battery:  ###当属性和方法变的太多的时候，可以单独弄一个类出来。
#    def __init__(self, battery_size=40):
#        self.battery_size = battery_size

#    def describe_battery(self):
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def get_range(self):
#        if self.battery_size == 40:
#            range = 150
#        elif self.battery_size == 65:
#            range = 225
#        print(f"This car can go about {range} miles on a full charge.")


#class ElectricCar(Car):  ###定义子类的时候必须在括号内指定父类名称。
#    def __init__(self, make, model, year):
#        super().__init__(make, model, year)   ###super()是一个特殊的函数，让你可以调用父类的方法。父类也称为“超类”superclass，函数名由此得名。
#        self.battery = Battery()  ###将一个Battery实例作为ElectricCar的一个属性。这样就可以将电池独立出来，且不影响ElectricCar类的其他属性和方法。
#        ##相当于新增一个属性


#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#my_leaf.get_descriptive_name()
#my_leaf.battery.describe_battery()
#my_leaf.battery.get_range()

#练习9.6 冰激凌小店
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


#class IceCreamStand(Restaurant):
#    def __init__(self, restaurant_name, restaurant_type):
#        super().__init__(restaurant_name, restaurant_type)
#        self.flavors = []

#    def show_flavors(self):
#        print("We have the following flavors:")
#        for flavor in self.flavors:
#            print(f"- {flavor}")

#restaurant = IceCreamStand('Cold Stone', 'Ice Cream')
#restaurant.flavors.append('Chocolate')
#restaurant.flavors.append('Vanilla')
#restaurant.flavors.append('Strawberry')
#restaurant.show_flavors()


#练习9.8 权限
#class User:
#    def __init__(self, first_name, last_name):
#        self.first_name = first_name
#        self.last_name = last_name
#        self.login_attempts = 0
       
#    def describe_user(self):
#        """用于打印用户信息摘要"""
#        print(f"This user's name is {self.first_name} {self.last_name}.")

#    def greet_user(self):
#        """用于向用户发出个性化的问候"""
#        print(f"Welcome to our website, {self.first_name}!")

#    def increment_login_attempts(self):
#        self.login_attempts += 1
#        print(self.login_attempts)

#   def reset_login_attempts(self):
#        self.login_attempts = 0
#        print(self.login_attempts)

#class Privileges:
#    def __init__(self, privileges=[]):
#        self.privileges = privileges

#    def show_privileges(self):
#        print('Admin privileges:')
#        for privilege in self.privileges:
#            print(f"- {privilege}")


#class Admin(User):
#    def __init__(self,first_name, last_name):
#        super().__init__(first_name, last_name)
#        self.priv = Privileges()
    

#admin1 = Admin('Niu', 'yiqun')
#admin1.describe_user()
#admin1.priv.privileges.append('can add post')
#admin1.priv.privileges.append('can delete post')
#admin1.priv.privileges.append('can ban user')
#admin1.priv.show_privileges()
#print(admin1.priv.privileges)

#练习9.9 电池升级
#class Car:
#    def __init__(self, make, model, year):
#        self.make = make
#        self.model = model
#        self.year = year
#        self.odometer_reading = 0

#    def get_descriptive_name(self):
#        long_name = f"{self.year} {self.make} {self.model}"
#        print(long_name)
    
#    def read_odometer(self):
#        print(f"This car has {self.odometer_reading} miles on it.")

#    def update_odometer(self, mileage):
#        if mileage >= self.odometer_reading:
#            self.odometer_reading = mileage
#        else:
#            print("You can't roll back an odometer!")

#    def increment_odometer(self, miles):
#        self.odometer_reading += miles

#    def fill_gas_tank(self):
#        print(f"This car has a gas tank.")

#class Battery:  ###当属性和方法变的太多的时候，可以单独弄一个类出来。
#    def __init__(self, battery_size=40):
#        self.battery_size = battery_size

#    def describe_battery(self):
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def get_range(self):
#        if self.battery_size == 40:
#            range = 150
#        elif self.battery_size == 65:
#            range = 225
#        print(f"This car can go about {range} miles on a full charge.")

#    def upgrade_battery(self):
#        if self.battery_size != 65:
#            self.battery_size = 65

#class ElectricCar(Car):  ###定义子类的时候必须在括号内指定父类名称。
#    def __init__(self, make, model, year):
#        super().__init__(make, model, year)   ###super()是一个特殊的函数，让你可以调用父类的方法。父类也称为“超类”superclass，函数名由此得名。
#        self.battery = Battery()  ###将一个Battery实例作为ElectricCar的一个属性。这样就可以将电池独立出来，且不影响ElectricCar类的其他属性和方法。
#        ##相当于新增一个属性

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#my_leaf.battery.get_range()
#my_leaf.battery.upgrade_battery()
#my_leaf.battery.get_range()














































