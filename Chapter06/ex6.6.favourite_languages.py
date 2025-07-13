# Python Crash Course, 2Ed, writtern by Eric Matthes

favourite_languages = {
    'jen' : 'python',
        'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}

for name, language in favourite_languages.items():
    print(f"{name.title()}s favourite language is {language.title()}.")

print("\n-----\n")

people = ['david', 'stefan', 'modric', 'sarah', 'phil']

for person in people:
    if person in favourite_languages:
        print(f"{person.title()}, thank you for the poll.\nYour favourite language is {favourite_languages.get(person).title()}.")
    else:
        print(f"{person.title()}, please take the poll.")
