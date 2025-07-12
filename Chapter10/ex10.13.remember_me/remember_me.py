import json
import os

def get_stored_username():

    """Get stored username if available."""

    filename = 'username.json'
    if os.path.getsize(filename) > 0:
        try:
            with open(filename) as f:
                username = json.load(f)
        except FileNotFoundError:
            return None
        else:
            return username
    else:
        return None

def greet_user():

    """ Greet the user by name. """

    username = get_stored_username()
    if username:
        confirmation = input(f"Are you {username}?\n(Input \'Y\' or\'y\' if yes, other input will be cosidered as no.)\n>> ").lower()
        if confirmation == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you whe you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you whe you come back, {username}!")

def get_new_username():

    """Pronpt for a new username."""

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

greet_user()
