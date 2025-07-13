# Python Crash Course, 2Ed, writtern by Eric Matthes

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

sukiya = Restaurant('sukiya', 'japanese beef rice')
sukiya.describe_restaurant()
sukiya.open_restaurant()
