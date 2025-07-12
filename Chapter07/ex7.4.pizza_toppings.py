pizza_toppings = []

active = True
while active == True:
    pizza_topping = input("Enter one pizza topping (or type \'quit\' to exit): ").lower()
    if pizza_topping == 'quit':
        active = False
    else :
        pizza_toppings.append(pizza_topping

if len(pizza_toppings) == 0:
    print("You will get a bare pizza.\n")
else:
    print(f"There are {len(pizza_toppings)} of pizza toppings:")
    for pizza_topping in pizza_toppings:
       print(pizza_topping.title())
