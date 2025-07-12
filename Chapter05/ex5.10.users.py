admin = ['sowon', 'yerin', 'eunha']
users = ['sowon', 'yerin', 'eunha', 'yuju', 'sinb', 'umji']
walk_in_users = ['eunso', 'yeorum', 'IU', 'sana', 'eunha', 'sinb']
walk_in_users_updated = []

for walk_in_user in walk_in_users:
    walk_in_users_updated.append(walk_in_user.lower())

if users:
    for walk_in_user in walk_in_users_updated:
        if walk_in_user in users:
            print(f"{walk_in_user.title()} name is already in user list. Please use another name.")
        else:
            users.append(walk_in_user)
            print(f"{walk_in_user.title()} has been newly registered.")
else:
    print("There is no registered user.")
