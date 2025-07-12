admin = ['sowon', 'yerin', 'eunha']
users = ['sowon', 'yerin', 'eunha', 'yuju', 'sinb', 'umji']

for user in users:
    if user in admin:
        print(f"Hello admin {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")
