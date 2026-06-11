#9.4 导入类
#9.4.1 导入单个类
#from car import Car
#my_new_car = Car('audi', 'a4', 2024)
#print(my_new_car.get_descriptive_name())
#my_new_car.update_odometer(23)
#my_new_car.read_odometer()

#from car import ElectricCar

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())
#my_leaf.battery.import_battery(65)    ##调用Battery类中的import_battery方法来修改电池容量
#my_leaf.battery.describe_battery()
#my_leaf.battery.get_range()

#9.4.3 从一个模块中导入多个类
#from car import Car, ElectricCar

#my_mustang = Car('ford', 'mustang', 2024)
#print(my_mustang.get_descriptive_name())
#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())

#9.4.4导入整个模块
#import car  #这里在下面使用car.Car和car.ElectricCar来访问类

#my_mustang = car.Car('ford', 'mustang', 2024)
#print(my_mustang.get_descriptive_name())

#my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())

#9.4.5 导入模块中的所有类   #这种方法不太推荐，因为它会导入模块中的所有类，可能会导致命名冲突
#from car import *   #这里直接使用Car和ElectricCar来访问类
#my_mustang = Car('ford', 'mustang', 2024)
#print(my_mustang.get_descriptive_name())

#my_leaf = ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())

#9.4.6 在一个模块中导入另一个模块
from car import Car
from electric_car import ElectricCar as EC #这里使用as来给ElectricCar类起一个别名EC

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())














































