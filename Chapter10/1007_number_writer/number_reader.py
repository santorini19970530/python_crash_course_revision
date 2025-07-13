# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
