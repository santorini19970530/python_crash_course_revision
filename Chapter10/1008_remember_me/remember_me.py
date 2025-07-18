# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

def get_stored_username():

    """Get stored username if available."""

    filename = 'username.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():

    """ Greet the user by name. """

    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you whe you come back, {username}!")

greet_user()

def get_new_username():

    """Pronpt for a new username."""

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
