# Python Crash Course, 2Ed, writtern by Eric Matthes

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['haha', 'ty', 'margot']
greet_users(usernames)
