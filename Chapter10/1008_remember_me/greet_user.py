# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

