# Chapter 8: Functions

## 1. Function - Reusable Code Block

**Definition**: A named block of code that performs a specific task and can be called from other parts of your program.

**Key Points**:
- Use `def` keyword to define functions
- Functions are reusable code blocks
- Use docstrings for documentation
- Call functions with parentheses `()`

**Example**:
```python
# Basic function definition
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

**Exercise 8.1 - Message:**
```python
# Exercise 8.1: Basic function definition
def display_message():
    print("I am going to learn this chapter.")

display_message()
```

## 2. def Statement - Function Definition

**Definition**: A statement that defines a function, specifying its name and parameters.

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
```

## 3. Parameter - Function Input

**Definition**: A piece of information that a function needs to do its job, specified in the function definition.

```python
def greet_user(username):
    print(f"Hello, {username.title()}!")
```

## 4. Argument - Function Call Value

**Definition**: A piece of information that's passed from a function call to a function.

```python
greet_user('jesse')  # 'jesse' is the argument
```

**Exercise 8.2 - Favorite Book:**
```python
# Exercise 8.2: Function with parameter
def favourite_book(title):
    print(f"One of my favourite books is {title.title()}.")

books = ['Alice in the Wonderland', 'The Wealth of Nations', '1984']

for book in books:
    favourite_book(book)
```

## 5. Return Value - Function Output

**Definition**: The value that a function returns to the calling line of code.

```python
# Function with return value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

## 6. Default Parameter Value - Optional Arguments

**Definition**: A parameter that has a default value, making it optional when calling the function.

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
```

**Exercise 8.3 - T-Shirt:**
```python
# Exercise 8.3: Default parameters
def make_shirt(size='M', message='Wie heißen Sie?'):
    print(f"We will make {size} T-shirt with a slogen of \"{message}.\"\n")

make_shirt()
make_shirt('S')
make_shirt(message='Und Sie?', size='L')
make_shirt('XL', 'Ich heiße Stefan.')
```

## 7. Positional Arguments - Order-Based

**Definition**: Arguments that must be passed to a function in the same order as the parameters are defined.

```python
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
```

## 8. Keyword Arguments - Name-Based

**Definition**: Arguments that are passed to a function by parameter name, allowing any order.

```python
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

## 9. Arbitrary Arguments - *args

**Definition**: A parameter that allows a function to accept any number of arguments.

```python
# Arbitrary arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

## 10. Arbitrary Keyword Arguments - **kwargs

**Definition**: A parameter that allows a function to accept any number of keyword arguments.

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                           location='princeton',
                           field='physics')
```

**Exercise 8.5 - Cities:**
```python
# Exercise 8.5: Function with arbitrary arguments
def describe_city(city, country='unknown'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('tokyo', 'japan')
describe_city('seoul', 'korea')
describe_city('berlin')
```

**Exercise 8.6 - Cities (Extended):**
```python
# Exercise 8.6: Extended cities function
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('tokyo', 'japan'))
print(city_country('seoul', 'korea'))
```

## 11. Docstring - Function Documentation

**Definition**: A string that describes what a function does, enclosed in triple quotes.

```python
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
```

## 12. Module - Code Organization

**Definition**: A file containing functions and variables that can be imported into other programs.

```python
# pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

## 13. import Statement - Module Usage

**Definition**: A statement that makes functions and variables from a module available in your program.

```python
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

## 14. from...import Statement - Selective Import

**Definition**: A statement that imports specific functions from a module.

```python
from pizza import make_pizza
make_pizza(16, 'pepperoni')
```

**Exercise 8.7 - Albums:**
```python
# Exercise 8.7: Function with arbitrary keyword arguments
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album('beatles', 'abbey road'))
print(make_album('pink floyd', 'dark side of the moon', 10))
print(make_album('queen', 'a night at the opera'))
```

**Exercise 8.8 - Albums (Extended):**
```python
# Exercise 8.8: Extended albums with user input
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    artist = input("Enter artist name (or 'quit' to exit): ")
    if artist == 'quit':
        break
    
    title = input("Enter album title: ")
    tracks = input("Enter number of tracks (or press Enter to skip): ")
    
    if tracks:
        album = make_album(artist, title, int(tracks))
    else:
        album = make_album(artist, title)
    
    print(album)
```

**Exercise 8.9 - Messages:**
```python
# Exercise 8.9: List of messages
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = ['Hello there!', 'How are you?', 'Good morning!']
sent_messages = []

show_messages(text_messages)
send_messages(text_messages, sent_messages)

print(f"\nOriginal list: {text_messages}")
print(f"Sent messages: {sent_messages}")
```

**Exercise 8.10 - Messages (Extended):**
```python
# Exercise 8.10: Extended messages with copy
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

text_messages = ['Hello there!', 'How are you?', 'Good morning!']
sent_messages = []

# Send messages using a copy of the original list
send_messages(text_messages[:], sent_messages)

print(f"\nOriginal list: {text_messages}")
print(f"Sent messages: {sent_messages}")
```

**Exercise 8.12 - Sandwiches:**
```python
# Exercise 8.12: Function with arbitrary arguments
def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'tomato')
make_sandwich('peanut butter', 'jelly', 'banana')
```

**Exercise 8.13 - User Profile:**
```python
# Exercise 8.13: Function with arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('albert', 'einstein',
                          location='princeton',
                          field='physics',
                          age=76)

print(my_profile)
```

**Exercise 8.14 - Cars:**
```python
# Exercise 8.14: Function with arbitrary keyword arguments
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
```

**Exercise 8.15 - Printing Models:**
```python
# Exercise 8.15: Functions in separate module
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

## Practical Examples from Chapter 8

### Working with Functions

Chapter 8 introduces functions and their various forms. Here are the key files:

**Basic Function Definition:**
```python
# Chapter08/801_greeter.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

**Functions with Return Values:**
```python
# Chapter08/803_formatted_name.py
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```

**Functions with Arbitrary Arguments:**
```python
# Chapter08/807_pizza.py
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

## Key Takeaways

**Function Basics**:
- Use `def` to define functions
- Functions are reusable code blocks
- Use docstrings for documentation
- `return` sends values back to caller

**Parameters and Arguments**:
- Parameters receive information in functions
- Arguments provide information to functions
- Default parameters make arguments optional
- Positional arguments must be in correct order
- Keyword arguments can be in any order

**Advanced Features**:
- `*args` accepts any number of arguments
- `**kwargs` accepts any number of keyword arguments
- Modules organize code into files
- `import` makes modules available
- `from...import` brings specific functions 