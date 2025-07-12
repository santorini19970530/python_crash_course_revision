def print_H():
    print("\n-------------------\n")

def greet_user():
    """Display a simple greeting."""
    print("Hello")

def greet_user_a(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user()
greet_user_a('jesse')

print_H()

def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def greet_formatted_user(first_name, last_name):
    """ Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Please tell me your name: ")
    print("enter 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")
