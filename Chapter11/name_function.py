# Python Crash Course, 2Ed, writtern by Eric Matthes

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatter full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
