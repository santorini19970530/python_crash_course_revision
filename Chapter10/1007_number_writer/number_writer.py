# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

numbers = [2,3,4,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers,f)
