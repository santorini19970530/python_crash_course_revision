# Python Crash Course, 2Ed, writtern by Eric Matthes

dimensions = (300, 50)
print(dimensions[0])
print(dimensions[1])

# nothing can modify Tuple, i.e. assign the value of it

for dimension in dimensions :
    print(dimension)

# but we can re-define the Tuple

dimensions = (1000,20)

for dimension in dimensions :
    print(dimension)
