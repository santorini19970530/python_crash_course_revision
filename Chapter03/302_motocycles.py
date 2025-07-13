# Python Crash Course, 2Ed, writtern by Eric Matthes

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

print("---------")
motorcycles = ['honda', 'yamaha', 'suzuki']
# appending elements to list, preset to the last position
motorcycles.append('ducati')
print(motorcycles)

print("---------")
motorcycles = []
# appending elements to list, one by one 
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
# insert can insert to the specific location
motorcycles.insert(0, 'ducati')
print(motorcycles)
print("---------")
# del can delete one of the elements
del motorcycles[0]
print(motorcycles)

print("---------")
# pop : chop out the last item and store that into the last value
poped_motorcycles = motorcycles.pop()
print(motorcycles)
print(poped_motorcycles)

print("---------")
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

print("---------")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

print("---------")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# removing item by value
motorcycles.remove('ducati')
print(motorcycles)

print("---------")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# removing item by value, same result as pop
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
