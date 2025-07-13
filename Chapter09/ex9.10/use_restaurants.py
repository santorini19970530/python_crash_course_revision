# Python Crash Course, 2Ed, writtern by Eric Matthes

from restaurants import *

sukiya = Restaurant('sukiya', 'japanese beef rice')
sukiya.describe_restaurant()

print('\n')
hardees =  Restaurant('hardees', 'hamburger')
hardees.describe_restaurant()

print('\n')
abc = Restaurant('abc', 'western food')
abc.open_restaurant()
abc.describe_restaurant()

print("------")

print(f"\nSet the number of customers of {sukiya.restaurant_name.title()} -")
sukiya.set_number_served(100)

print(f"\nSet the number of customers of {hardees.restaurant_name.title()} -")
hardees.set_number_served(10000)

new_customer = 1
print(f"\nThere are {new_customer} customers coming in {abc.restaurant_name.title()} -")
abc.increment_numbers_served(new_customer)

print("------")

print("\nShow restaurants' information again:")
sukiya.describe_restaurant()
print('\n')
hardees.describe_restaurant()
print('\n')
abc.describe_restaurant()

print("------")

appolo = IceCreamStand('appolo', 'ice cream stand', ['chocolate', 'vanilla'])
appolo.describe_restaurant()
