def print_H():
    print("------------------------")

from car import Car
#import Car
from electric_car import ElectricCar
#import electric_car

my_new_car = Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print_H()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

print_H()

my_used_car = Car('suburu', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

print_H()

my_bettle = Car('volkswagen', 'roadstar', 2019)
print(my_bettle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadstar', 2019)
print(my_tesla.get_descriptive_name())
