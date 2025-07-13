# Python Crash Course, 2Ed, writtern by Eric Matthes

cars = ['bmw', 'audi', 'cars', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
# sort : change the order of the list permanently by alphabetical order

cars = ['bmw', 'audi', 'cars', 'toyota', 'subaru']
# sort in reversed alphabetical order
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'cars', 'toyota', 'subaru']
# reverse can also do this
cars.reverse()
print(cars)

print("----------")
cars = ['bmw', 'audi', 'cars', 'toyota', 'subaru']
print(f"This is the original list:\n{cars}")
# sorted: display the sorted list without affecting the original order
print(f"This is the sorted list:\n{sorted(cars)})")
print(f"This is the original list again:\n{cars})")

print("----------")
print(f"Length of list is {len(cars)}")
