# Python Crash Course, 2Ed, writtern by Eric Matthes

def build_person(first_name, last_name, age=None):
    """ Return a dictionary of information about a person."""
    person = {
            'first' : first_name,
            'last' : last_name,
            }
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

musician = build_person('hihi', 'hihihi')
print(musician)
