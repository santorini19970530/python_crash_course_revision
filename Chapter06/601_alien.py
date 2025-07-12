def print_H():
    print("-----------")

alien_0 = {
        'color': 'green',
        'points' : 5
        }
print(alien_0['color'])
print(alien_0['points'])

print_H()

new_pionts = alien_0['points']

print(f"You just earned {new_pionts} points!")

print_H()

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print_H()

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print_H()

print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'Yellow'

print(f"The alien is now {alien_0['color']}")

print_H()

alien_0 = {
        'x_position' : 0,
        'y_position' : 23,
        'speed' : 'medium'
        }
print(f"Original positon: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position : {alien_0['x_position']}")

print_H()

alien_0 = {
        'color' : 'green',
        'points' : 5
        }
print(alien_0)

del alien_0['points']
print(alien_0)


