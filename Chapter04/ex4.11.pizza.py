# Python Crash Course, 2Ed, writtern by Eric Matthes

pizzas = ['peccato', 'diavola', 'capricciosa']

for pizza in pizzas:
    print(f"I like {pizza.title()}.")
print("The above statements are fake.")

friend_pizzas = pizzas[:]

print("\n----")
print("Another pizza list as per below:")
for pizza in friend_pizzas:
    print(f"{pizza.title()}")

friend_pizzas.append('Clam pie')
print("\n----")
print(f"Adding {friend_pizzas[-1]}\nThe pizza list:")
for pizza in friend_pizzas:
    print(f"{pizza.title()}")
