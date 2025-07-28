# Chapter 6: Dictionaries

## 1. Dictionary - Key-Value Pairs

**Definition**: A collection of key-value pairs that allows you to connect pieces of related information.

**Key Points**:
- Use curly braces `{}` to create dictionaries
- Keys must be immutable (strings, numbers, tuples)
- Values can be any data type
- Access values using square brackets: `dict['key']`

**Example**:
```python
# Basic dictionary operations
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
```

**Exercise 6.1 - Person Information**:
```python
# Exercise 6.1: Creating a person dictionary
person = {
    'first_name': 'eunbi',
    'last_name': 'jung',
    'age': 26,
    'city': 'seoul'
}

print(f"I am going to talk about my wife:\nHer name is {person['last_name'].title() + ' ' + person['first_name'].title()}.\nShe is {person['age']} years old.\nShe is living in {person['city'].title()}.")
```

## 2. Key-Value Pair - Dictionary Element

**Definition**: A set of values associated with each other, where a key is used to access its associated value.

**Key Points**:
- Each key-value pair is separated by a colon `:`
- Pairs are separated by commas
- Keys must be unique within a dictionary

**Example**:
```python
alien_0 = {'color': 'green', 'points': 5}
```

**Exercise 6.2 - Favorite Numbers**:
```python
# Exercise 6.2: Storing favorite numbers
favourite_number = {
    'sowon': 1,
    'yerin': 2,
    'eunha': 3,
    'yuju': 4,
    'sinb': 5,
    'umji': 6
}

print(f"Sowon's favourite number is {favourite_number['sowon']}.")
print(f"Yerin's favourite number is {favourite_number['yerin']}.")
print(f"Eunha's favourite number is {favourite_number['eunha']}.")
print(f"Yuju's favourite number is {favourite_number['yuju']}.")
print(f"Sinb's favourite number is {favourite_number['sinb']}.")
print(f"Umji's favourite number is {favourite_number['umji']}.")
```

## 3. Accessing Values - Dictionary Lookup

**Definition**: The process of retrieving a value from a dictionary using its key.

**Key Points**:
- Use square brackets with key name: `dict['key']`
- Raises KeyError if key doesn't exist
- Use `.get()` method for safe access with default value

**Example**:
```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # 'green'
```

**Exercise 6.3 - Glossary**:
```python
# Exercise 6.3: Accessing dictionary values
glossary = {
    'die Adresse': "address",
    'die Webseite': "website"
}

print(f"'die Adresse' means {glossary['die Adresse'].title()}.")
print(f"'die Webseite' means {glossary['die Webseite'].title()}.")
```

## 4. Adding Key-Value Pairs - Dictionary Modification

**Definition**: The process of adding new key-value pairs to an existing dictionary.

**Key Points**:
- Assign to a new key to add pairs
- Syntax: `dict['new_key'] = value`
- Keys are case-sensitive

**Example**:
```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
```

## 5. Starting with Empty Dictionary - Dynamic Creation

**Definition**: Creating a dictionary with no key-value pairs and adding them as needed.

**Key Points**:
- Use empty braces `{}`
- Add pairs one by one
- Useful for building dictionaries dynamically

**Example**:
```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
```

## 6. Modifying Values - Dictionary Updates

**Definition**: Changing the value associated with a key in a dictionary.

**Key Points**:
- Assign to existing key to modify
- Overwrites the previous value
- No special method needed

**Example**:
```python
alien_0 = {'color': 'green', 'points': 5}
alien_0['color'] = 'yellow'
```

## 7. Removing Key-Value Pairs - del Statement

**Definition**: Permanently removing a key-value pair from a dictionary using the del statement.

**Key Points**:
- Use `del dict['key']` syntax
- Permanently removes the pair
- Raises KeyError if key doesn't exist

**Example**:
```python
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
```

## 8. Looping Through Dictionary - items() Method

**Definition**: Iterating through all key-value pairs in a dictionary.

**Key Points**:
- Use `.items()` method to get key-value pairs
- Returns tuples of (key, value)
- Can unpack directly in for loop

**Example**:
```python
# Looping through dictionaries
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
```

**Exercise 6.4 - Glossary with Looping:**
```python
# Exercise 6.4: Looping through dictionary items
glossary = {
    'die Adresse': "address",
    'die Webseite': "website",
    'können': "can",
    'Velen Dank': "Very thnks"
}

for word, meaning in glossary.items():
    print(f"{word.title()} means {meaning.title()}.")
```

**Exercise 6.5 - Rivers:**
```python
# Exercise 6.5: Looping through rivers and countries
rivers = {
    'nile': "egypt",
    'eunha': "Jung Eun Bi",
    'komogawa': "japan"
}
countRiver = 0
countCountry = 0

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    countRiver += 1
    print(f"River {countRiver}: {river.title()}")

for country in rivers.values():
    countCountry += 1
    print(f"Country {countCountry}: {country.title()}")
```

## 9. Looping Through Keys - keys() Method

**Definition**: Iterating through all keys in a dictionary.

**Key Points**:
- Use `.keys()` method to get all keys
- Default behavior when looping through dict
- Can omit `.keys()` - just loop through dict directly

**Example**:
```python
favourite_languages = {'jen': 'python', 'sarah': 'c'}
for name in favourite_languages.keys():
    print(name.title())
# looping through the keys is actually the default behaviour when looping through a dictionary
# the .keys() can be omitted
```

## 10. Looping Through Values - values() Method

**Definition**: Iterating through all values in a dictionary.

**Key Points**:
- Use `.values()` method to get all values
- Returns only the values, not keys
- Use `set()` to get unique values

**Example**:
```python
favourite_languages = {'jen': 'python', 'sarah': 'c'}
for language in favourite_languages.values():
    print(language.title())
```

**Exercise 6.6 - Favorite Languages with Conditional Logic:**
```python
# Exercise 6.6: Checking if keys exist in dictionary
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
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
```

## 11. Nesting - Dictionaries in Dictionaries

**Definition**: Storing multiple dictionaries in a list, or a list of items as a value in a dictionary.

**Key Points**:
- Lists can contain dictionaries
- Dictionaries can contain lists
- Dictionaries can contain other dictionaries
- Allows complex data structures

**Example**:
```python
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
```

**Exercise 6.7 - Multiple People:**
```python
# Exercise 6.7: List of dictionaries
members = []

countMember = 0

for count in range(6):
    person = {
        'nick_name': 'eunha',
        'first_name': 'eunbi',
        'last_name': 'jung',
        'age': 26,
        'city': 'seoul'
    }
    members.append(person)

members[0]['first_name'] = 'sojung'
members[0]['last_name'] = 'kim'
members[0]['age'] = 27
members[0]['nick_name'] = 'sowon'

members[1]['first_name'] = 'yerin'
members[1]['last_name'] = 'jung'
members[1]['nick_name'] = 'yerin'

members[3]['first_name'] = 'yuna'
members[3]['last_name'] = 'choi'
members[3]['age'] = 25
members[3]['nick_name'] = 'yuju'

members[4]['last_name'] = 'hwang'
members[4]['age'] = 24
members[4]['nick_name'] = 'sinb'

members[5]['first_name'] = 'yewon'
members[5]['last_name'] = 'kim'
members[5]['age'] = 24
members[5]['nick_name'] = 'umji'

for member in members:
    countMember += 1
    print(f"I am going to talk about my wife no. {countMember}:\nHer name is {member['last_name'].title() + ' ' + member['first_name'].title()}.\nShe is {member['age']} years old.\nShe is living in {member['city'].title()}.")
    print("...\n")
```

**Exercise 6.8 - Pets:**
```python
# Exercise 6.8: List of pet dictionaries
pets = []

pet = {
    'type': 'cat',
    'name': 'david',
    'owner': 'lawrence',
    'weight': 44,
    'food': "meat"
}
pets.append(pet)

pet = {
    'type': 'dog',
    'name': 'alan',
    'owner': 'steve',
    'weight': 29,
    'food': "sausage"
}
pets.append(pet)

pet = {
    'type': 'parrot',
    'name': 'baga',
    'owner': 'sarah',
    'weight': 3,
    'food': "peanuts"
}
pets.append(pet)

for pet in pets:
    print(f"{pet['type'].title()}'s names is {pet['name']}, owner is {pet['owner'].title()}.")
    print(f"Weight is {pet['weight']}, and it eats {pet['food']}.")
```

## 12. List in Dictionary - Complex Data

**Definition**: Using a list as a value in a dictionary to store multiple items.

```python
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go']
}
```

**Exercise 6.9 - Favorite Places:**
```python
# Exercise 6.9: Lists as dictionary values
favourite_places = {
    "steven": ['tokyo', 'pusan', 'yokohama'],
    "apple": ['new york', 'london'],
    "baka": ['rome', 'frankfurt', 'seoul', 'taipei']
}

for name, places in favourite_places.items():
    print(f"{name.title()}\'s favourite place are:")
    for place in places:
        print(f"{place.title()}")
```

**Exercise 6.10 - Favorite Numbers:**
```python
# Exercise 6.10: Lists of numbers in dictionary
favourite_numbers = {
    'sowon': [1, 3, 4, 8],
    'yerin': [2, 6, 9],
    'eunha': [3, 7, 11],
    'yuju': [4, 112, 1100],
    'sinb': [5, 6, 7],
    'umji': [1, 6]
}

for person, numbers in favourite_numbers.items():
    print(f"{person.title()}'s favourite numbers are:")
    for number in numbers:
        print(number)
```

## 13. Dictionary in Dictionary - Nested Structures

**Definition**: Storing a dictionary as a value in another dictionary.

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    }
}
```

**Exercise 6.11 - Cities:**
```python
# Exercise 6.11: Nested dictionaries
cities = {
    'tokyo': {
        'country': 'japan',
        'population': 1_000_000,
        'food': 'sushi'
    },
    'new york': {
        'country': 'the unided states',
        'population': 2_000_000,
        'food': 'hamburger'
    },
    'hongkong': {
        'country': 'hongkong',
        'population': 6_000_000,
        'food': 'noodles'
    }
}

for city, information in cities.items():
    print(f"Information of {city.title()}:")
    print(f"Country: {information['country'].title()}\nPopulation: {information['population']}\nFamous food :{information['food'].title()}\n")
```

## Key Takeaways

**Dictionary Basics**:
- Use curly braces `{}` to create dictionaries
- Keys must be immutable (strings, numbers, tuples)
- Values can be any data type
- Keys are case-sensitive and must be unique

**Accessing and Modifying**:
- Use square brackets: `dict['key']` to access values
- Assign to keys to add/modify: `dict['key'] = value`
- Use `del dict['key']` to remove pairs
- Use `.get()` method for safe access with defaults

**Looping Methods**:
- `.items()` - loop through key-value pairs
- `.keys()` - loop through keys (default behavior)
- `.values()` - loop through values
- Use `set()` to get unique values

**Advanced Features**:
- Check membership: `'key' in dict`
- Nesting: lists in dicts, dicts in dicts
- Order preserved (Python 3.7+)
- Use `.copy()` for shallow copies 