# Python Crash Course, 2Ed, writtern by Eric Matthes

def print_H():
    print("--------------------")

alien_0 = {
        'color' : 'green',
        'points' : 5,
        }
alien_1 = {
        'color' : 'yellow',
        'points' : 10,
        }
alien_2 = {
        'color' : 'red',
        'points' : 15,
        }

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print_H()

aliens = []

for alien_nunber in range(30):
    new_alien = {
            'color' : 'green',
            'points' : 5,
            'speed' : 'slow',
            }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("etc.")

print(f"Total number of aliens: {len(aliens)}")

print_H()

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10

for alien in aliens[:5]:
    print(alien)
print("etc.")
