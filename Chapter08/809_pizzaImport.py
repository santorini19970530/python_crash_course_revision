# Python Crash Course, 2Ed, writtern by Eric Matthes

def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make."""
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

