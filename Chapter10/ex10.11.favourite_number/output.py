# Python Crash Course, 2Ed, writtern by Eric Matthes

import json

filename = 'data.json'
with open(filename) as f:
    fav_num= json.load(f)

print(f"I know your favourite number! It's {fav_num}.")
