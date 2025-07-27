# Chapter 10: Files and Exceptions

## 1. File - Data Storage

**Definition**: A collection of information stored as a unit on a computer, accessible by programs.

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
```

## 2. open() Function - File Access

**Definition**: A function that opens a file and returns a file object, which contains methods and attributes for working with the file.

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
```

## 3. with Statement - File Context

**Definition**: A statement that ensures a file is properly closed after the block of code using it is finished.

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
# File is automatically closed here
```

## 4. read() Method - File Content

**Definition**: A method that reads the entire contents of a file as a string.

```python
# Reading file contents
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents.rstrip())
```

**Exercise 10.1 - Learning Python:**
```python
# Exercise 10.1: Reading file contents in different ways
filename = 'learning_python.txt'

# First time: print the contents once by reading in the entire file
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# Second time: print the contents by looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Third time: print the contents by storing the lines in a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

## 5. readlines() Method - Line List

**Definition**: A method that reads each line from a file and stores them in a list.

```python
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

## 6. write() Method - File Writing

**Definition**: A method that writes a string to a file, overwriting the file's contents.

```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

## 7. append Mode - 'a' Parameter

**Definition**: A file mode that adds content to the end of a file instead of overwriting it.

```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
```

**Exercise 10.3 - Guest:**
```python
# Exercise 10.3: Writing guest names to a file
name = input("What is your name? ")

filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(name)
```

**Exercise 10.4 - Guest Book:**
```python
# Exercise 10.4: Appending guest names to a file
filename = 'guest_book.txt'

while True:
    name = input("What is your name? (or 'quit' to exit): ")
    if name == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")
    print(f"Hello {name}, you've been added to the guest book.")
```

**Exercise 10.5 - Programming Poll:**
```python
# Exercise 10.5: Collecting programming poll responses
filename = 'programming_poll.txt'

while True:
    reason = input("Why do you like programming? (or 'quit' to exit): ")
    if reason == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")
```

## 8. Exception - Error Handling

**Definition**: An error that occurs during program execution, which can be caught and handled.

```python
# Exception handling
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

## 9. try-except Block - Error Catching

**Definition**: A block of code that tries to run some code and catches any exceptions that occur.

```python
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
```

## 10. else Block - Success Handling

**Definition**: A block of code that runs only if the try block succeeds (no exceptions occur).

```python
try:
    answer = int(first_number) / int(second_number)
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)
```

## 11. FileNotFoundError - Missing File

**Definition**: An exception that occurs when trying to open a file that doesn't exist.

```python
# Handling missing files
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

## 12. ZeroDivisionError - Division by Zero

**Definition**: An exception that occurs when trying to divide by zero.

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

## 13. ValueError - Invalid Conversion

**Definition**: An exception that occurs when trying to convert a string to a number when the string doesn't contain a valid number.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")
```

**Exercise 10.6 - Addition:**
```python
# Exercise 10.6: Addition with exception handling
def addition(num1, num2):
    return num1 + num2

def get_input():
    num = input("Enter the number >> ")
    try:
        int(num)
    except ValueError:
        print("The input is not digit.\nPlease try again.")
        return None
    else:
        return int(num)

print("The first number:")
x = get_input()
print("The second number:")
y = get_input()

if (x and y) != False:
    print(f"{x} + {y} = {x + y}")
```

**Exercise 10.7 - Addition (Extended):**
```python
# Exercise 10.7: Extended addition with quit option
while True:
    x = input("Enter the first number (or enter 'q' to quit) >> ")
    if x.lower() == 'q':
        break
    y = input("Enter the second number (or enter 'q' to quit) >> ")
    if y.lower() == 'q':
        break

    try:
        int(x)
        int(y)
    except ValueError:
        print("One of the numbers are not integers.\nTry again.")
    else:
        print(f"{int(x)} + {int(y)} = {int(x) + int(y)}")
```

## 14. pass Statement - Silent Failure

**Definition**: A statement that tells Python to do nothing in a block, often used in exception handling.

```python
try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    pass  # Do nothing if file not found
```

## 15. JSON - Data Format

**Definition**: A lightweight data format that's easy for programs to parse and generate.

```python
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
```

**Exercise 10.11 - Favorite Number:**
```python
# Exercise 10.11: Storing favorite number in JSON
import json

favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print(f"I'll remember that your favorite number is {favorite_number}.")
```

**Exercise 10.12 - Favorite Number (Extended):**
```python
# Exercise 10.12: Extended favorite number with file checking
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f"I'll remember that your favorite number is {favorite_number}.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")
```

**Exercise 10.13 - Remember Me:**
```python
# Exercise 10.13: Remember me with exception handling
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

**Exercise 10.8 - Pets:**
```python
# Exercise 10.8: Reading from multiple files
def read_file(filename):
    """Read and print the contents of a file."""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"\n{filename}:")
        print(contents)

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    read_file(filename)
```

## Practical Examples from Chapter 10

### Working with Files and Exceptions

Chapter 10 introduces file handling and exception handling. Here are the key files:

**File Reading Operations:**
```python
# Chapter10/1001_pi/file_reader.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents.rstrip())
```

**Exception Handling:**
```python
# Chapter10/1004_division_calculator.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

**File Error Handling:**
```python
# Chapter10/1006_word_count.py
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
```

## Key Takeaways

- Files store data persistently
- `open()` creates file objects
- `with` ensures proper file closing
- `read()` gets entire file content
- `readlines()` gets list of lines
- `write()` overwrites file content
- `'a'` mode appends to files
- Exceptions handle errors gracefully
- `try-except` catches exceptions
- `else` runs on successful try
- `FileNotFoundError` for missing files
- `ZeroDivisionError` for division by zero
- `ValueError` for invalid conversions
- `pass` does nothing in a block
- JSON stores structured data 