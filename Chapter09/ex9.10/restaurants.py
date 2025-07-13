# Python Crash Course, 2Ed, writtern by Eric Matthes

class Restaurant:
### Description of the class ###
# attributes
# restaurant_name : name of the restaurant
# cuisine_type : what sort of food can be eaten fron that restuarant
# number_served : number of customers that the restaurant has served; default 0
### End of description ###

### Methods ###

    # __init__ : initialize the class
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    # describe_restaurant : print the information of restaurant
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")
        print(f"Number of Customers Served: {self.number_served}")

    # open_restaurant : print an message for siumating the opeing of that restaurant
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

    # set_number_served : set the number of customers that have been served
    def set_number_served(self, numbers):
        self.number_served = numbers
        print(f"The new number of customers served becomes {self.number_served}.")

    # increment_numbers_served : increase the number of customers who've been served
    def increment_numbers_served(self, increment):
        self.number_served += increment
        print(f"Addind {increment} customers, the number of customers served is {self.number_served}.")

### End of Methods ###

class IceCreamStand(Restaurant):
### Description of the class ###
# child class of Restaurant
# flavors : a List of ice-crean flavors
### End of description ###

### Methods ###

    # __init__ : initialize the clsss
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors[:]

    # describe_restaurant : add ice-cream flavors available
    def describe_restaurant(self):
        super().describe_restaurant()
        print("Ice-Cream flavors available:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")

### End of Methods ###

