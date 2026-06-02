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
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())


