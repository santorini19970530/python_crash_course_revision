# Python Crash Course, 2Ed, writtern by Eric Matthes

### Car.py ###
### class Car ###

class Car:

    # class Car : A simple attempt to represent a car

    # __init__ : Initiate attributes to describe a car
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # get_descriptive_name : return a neatly formatted descriptive name
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    # read_odometer : print a statement showing the car's mileage
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    # update_odometer : set the odometer reading to the given value
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")

    # increment_odometer : add the given amount to the odometer reading
    def increment_odometer(self, miles):
        self.odometer_reading += miles
