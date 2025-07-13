# Python Crash Course, 2Ed, writtern by Eric Matthes

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.lower())
    else:
        print(car.title())
