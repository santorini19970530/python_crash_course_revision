# Python Crash Course, 2Ed, writtern by Eric Matthes

users = {
        'aeinstein':{
            'first' : 'albert',
            'last' : 'einstein',
            'location' : 'princeton',
            },
        'mcurie':{
            'first' : 'marie',
            'last' : 'curie',
            'location' : 'parts',
            },
        }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")
