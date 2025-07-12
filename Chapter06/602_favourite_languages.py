def print_H():
    print("------------------")

favourite_languages = {
        'jen' : 'python',
        'sarah' : 'c',
        'edward' : 'ruby',
        'phil' : 'python'
        }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

print_H()

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

print_H()

for name in favourite_languages.keys():
    print(name.title())
# loopint through the keys is actually the default bahaviour when looping through a dictionary
# the .keys() can be omitted

print_H()

friends = ['phil', 'sarah']

for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print_H()

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

print_H()

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print_H()

print("The folloing langauges have been mentiond:")
for language in set(favourite_languages.values()):
    print(language.title())

print_H()

favourite_languages = {
        'jen' : ['python', 'ruby'],
        'sarah' : ['c'],
        'edward' : ['ruby', 'go'],
        'phil' : ['python', 'haskell']
        }

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
