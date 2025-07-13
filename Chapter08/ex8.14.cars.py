# Python Crash Course, 2Ed, writtern by Eric Matthes

cars = []

def make_car(manufacturer, model, **car):
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
cars.append(car)

for car in cars:
    print(car)
