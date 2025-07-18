# Python Crash Course, 2Ed, writtern by Eric Matthes

def print_H():
    print("------------------------")

"""A set of classes used to represent gas and electric car."""

from car import Car

class Battery:

    """A simple attempt to model a battery for an electic car."""

    def __init__(self, battery_size = 75):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):

    """ Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initiate attributes of the parent class.
        Then initiaise attributes specific to an eletric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesm't need a gas tank!")
