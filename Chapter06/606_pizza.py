# Python Crash Course, 2Ed, writtern by Eric Matthes

pizza = {
        'crust' : 'thick',
        'toppings' : ['mushrooms', 'extra cheese']
        }

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
