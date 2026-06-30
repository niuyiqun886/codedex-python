from 前十章.car import Car
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
 

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def import_battery(self, battery_size): ##之前的代码battery_size是默认值，这里将battery_size重新赋值
        self.battery_size = battery_size

    def get_range(self):
#        if self.battery_size == 40:
#            range = 150
#        elif self.battery_size == 65:
#            range = 225
        if self.battery_size > 40:
            range = 225
        else:
            range = 150

        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
