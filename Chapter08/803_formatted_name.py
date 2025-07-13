# Python Crash Course, 2Ed, writtern by Eric Matthes

def print_H():
    print("=-------------=")

def get_formatted_name(first_name, last_name):
    """ Return a full name, neatly formatted. """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

print_H()

def get_formatted_name_A(first_name, middle_name, last_name):
    """ Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_A('john', 'lee', 'hooker')
print(musician)

print_H()

def get_formatted_name_B(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_B('Jimi', 'hendrix')
print(musician)
musician = get_formatted_name_B('john', 'hooker', 'lee')
print(musician)
