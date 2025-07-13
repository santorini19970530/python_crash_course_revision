# Python Crash Course, 2Ed, writtern by Eric Matthes

alien_0 = {
        'color' : 'green',
        'speed' : 'slow'
        }

## print(alien_0['points'])
# this will generate error, since there is no points property

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

