# Chapter 7: User Input and while Loops

## 1. input() Function - User Input

**Definition**: A function that pauses your program and waits for the user to enter some text, which is then stored as a string.

```python
# Basic user input
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

**Exercise 7.1 - Rental Car:**
```python
# Exercise 7.1: Basic user input
car = input("Which tell me what kind of rental car you would like to have: ")
print(f"Let me see if I can find you a {car.title()}.\n")
```

## 2. while Loop - Conditional Repetition

**Definition**: A loop that runs as long as, or while, a certain condition is true.

```python
# while loop with user input
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

## 3. int() Function - String to Integer

**Definition**: A function that converts a string containing a number to an integer.

```python
# Converting string input to integer
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

**Exercise 7.2 - Restaurant:**
```python
# Exercise 7.2: Converting input to integer
no_of_ppl = int(input("Please tell me how many of people in your dinner group: "))

if no_of_ppl > 8:
    print("Sorry, please wait for a while.\n")
else:
    print("Your table is ready.\n")
```

**Exercise 7.3 - Multiple of Ten:**
```python
# Exercise 7.3: Checking if number is multiple of ten
number = int(input("Please enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
```

## 4. Flag - Loop Control Variable

**Definition**: A variable that acts as a signal to the program, often used to control while loops.

```python
active = True
while active:
    message = input("Enter 'quit' to end: ")
    if message == 'quit':
        active = False
    else:
        print(message)
```

## 5. break Statement - Immediate Exit

**Definition**: A statement that immediately exits a loop without running any remaining code in the loop.

```python
while True:
    city = input("Enter a city name (or 'quit' to exit): ")
    if city == 'quit':
        break
    print(f"I'd love to go to {city.title()}!")
```

## 6. continue Statement - Skip Iteration

**Definition**: A statement that skips the rest of the current iteration and returns to the beginning of the loop.

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

## 7. Modulo Operator - %

**Definition**: An operator that divides one number by another and returns the remainder.

```python
number = 4 % 2  # 0 (even)
number = 5 % 2  # 1 (odd)
```

## 8. Moving Items Between Lists - List Operations

**Definition**: The process of removing items from one list and adding them to another list.

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
```

## 9. Removing All Instances - List Cleanup

**Definition**: Removing all occurrences of a specific value from a list.

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

## 10. Filling Dictionary with User Input - Dynamic Data

**Definition**: Building a dictionary by collecting user input in a loop.

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
```

**Exercise 7.4 - Pizza Toppings:**
```python
# Exercise 7.4: Building a pizza with user input
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
```

**Exercise 7.5 - Movie Tickets:**
```python
# Exercise 7.5: Complex ticket pricing with while loops
customers = []
group = {
    'baby': 0,
    'child': 0,
    'adult': 0
}
unit_price = {
    'baby': 0,
    'child': 10,
    'adult': 15
}
total_customers = 0
total_cost = 0
active = True

# input the ages
while active:
    customer = int(input("Please enter customer's age (input \'0\' to quit): "))
    if customer == 0:
        active = False
    else:
        customers.append(customer)

# divide the customers into groups
if len(customers) == 0:
    print("There is no one watching the movie.")
else:
    for customer in customers:
        if customer < 3:
            group['baby'] += 1
        elif (customer >= 3) and (customer < 12):
            group['child'] += 1
        else:
            group['adult'] += 1
        
    # calculate the cost
    print("\nNumber of customers: ")
    for item, value in group.items():
        total_customers += value
        cost = value * unit_price[item]
        total_cost += cost
        print(f"{item.title()}\t:\t{value} customers\t\tSubtotal: ${cost}")
    print(f"------------\nTotal\t:\t{total_customers} customers\t\tGrand Total: ${total_cost}")
```

**Exercise 7.8 - Deli:**
```python
# Exercise 7.8: Building a sandwich order
sandwich_orders = ['pastrami', 'veggie', 'grilled cheese', 'pastrami', 'turkey', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")
```

**Exercise 7.9 - Deli (Extended):**
```python
# Exercise 7.9: Extended deli with user input
sandwich_orders = []
finished_sandwiches = []

print("Enter 'quit' when you are finished.")
while True:
    sandwich = input("What kind of sandwich would you like? ")
    if sandwich != 'quit':
        sandwich_orders.append(sandwich)
    else:
        break

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")
```

## Practical Examples from Chapter 7

### Working with User Input and Loops

Chapter 7 introduces user input and while loops. Here are the key files:

**Basic User Input:**
```python
# Chapter07/702_greeter.py
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

**while Loops with User Input:**
```python
# Chapter07/701_parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

**Numerical Input and Type Conversion:**
```python
# Chapter07/703_rollercoster.py
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

## Key Takeaways

- `input()` gets user input as a string
- `int()` converts string to integer
- `while` loops run while condition is True
- Use flags to control while loops
- `break` exits a loop immediately
- `continue` skips to next iteration
- `%` operator gives remainder
- Use while loops to move items between lists
- `remove()` removes first occurrence of value
- Build dictionaries with user input
- Always provide clear prompts to users 