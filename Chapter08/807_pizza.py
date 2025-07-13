# Python Crash Course, 2Ed, writtern by Eric Matthes

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_a(*toppings):
    """Summarise the pizza with the following toppings."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza_a('pepperoni')
make_pizza_a('mushrooms', 'green peppers', 'extra cheese')

def make_pizza_b(size, *toppings):
    """Summarise the pizza we are about to make."""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza_b(16, 'pepperoni')
make_pizza_b(12, 'mushrooms', 'green peppers', 'extra cheese')
