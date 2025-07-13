# Python Crash Course, 2Ed, writtern by Eric Matthes

# strip.py -- manipulating string with strip functions.

name = " Jung Eun Bi "

name2 = " Jung \n Eun \t Bi "

print("For no \\n and \\t characters:")
print(f"No strip: {name}")
print(f"With lstrip(): {name.lstrip()}")
print(f"With rstrip(): {name.rstrip()}")
print(f"WIth strip(): {name.strip()}")

print("When \\n and \\t characters are included:")
print(f"No strip: {name2}")
print(f"With lstrip(): {name2.lstrip()}")
print(f"With rstrip(): {name2.rstrip()}")
print(f"WIth strip(): {name2.strip()}")

