# Chapter 9: Classes

## 1. Class - Object Blueprint

**Definition**: A blueprint for creating objects, defining what attributes and methods the objects will have.

```python
# Basic class definition
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

**Exercise 9.1 - Restaurant:**
```python
# Exercise 9.1: Basic class definition
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

sukiya = Restaurant('sukiya', 'japanese beef rice')
sukiya.describe_restaurant()
sukiya.open_restaurant()
```

## 2. Object - Class Instance

**Definition**: An instance of a class that contains data and behavior defined by the class.

```python
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
```

## 3. Attribute - Object Data

**Definition**: A variable that belongs to an object, accessed using dot notation.

```python
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

## 4. Method - Object Behavior

**Definition**: A function that belongs to a class, defining what an object can do.

```python
my_dog.sit()
my_dog.roll_over()
```

## 5. __init__() Method - Constructor

**Definition**: A special method that Python runs automatically whenever you create a new instance of a class.

```python
def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age
```

## 6. self Parameter - Object Reference

**Definition**: A reference to the instance of the class, allowing you to access attributes and methods.

```python
def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")
```

## 7. Instance - Class Object

**Definition**: An individual object created from a class, with its own set of attributes.

```python
my_dog = Dog('Willie', 6)  # my_dog is an instance
your_dog = Dog('Lucy', 3)  # your_dog is another instance
```

**Exercise 9.2 - Restaurants:**
```python
# Exercise 9.2: Multiple instances
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

sukiya = Restaurant('sukiya', 'japanese beef rice')
sukiya.describe_restaurant()
sukiya.open_restaurant()

hardees = Restaurant('hardees', 'hamburger')
hardees.describe_restaurant()

abc = Restaurant('abc', 'western food')
abc.describe_restaurant()
```

## 8. Inheritance - Class Relationship

**Definition**: A feature that allows you to model relationships between classes, where a child class inherits attributes and methods from a parent class.

```python
# Inheritance example
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

## 9. Parent Class - Base Class

**Definition**: A class that is inherited from, also called a base class or superclass.

```python
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
```

## 10. Child Class - Derived Class

**Definition**: A class that inherits from another class, also called a derived class or subclass.

```python
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
```

## 11. super() Function - Parent Access

**Definition**: A function that helps you make connections between parent and child classes.

```python
def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery = Battery()
```

## 12. Method Overriding - Custom Behavior

**Definition**: The ability to define a method in a child class that has the same name as a method in the parent class.

```python
def fill_gas_tank(self):
    """Electric cars don't have gas tanks."""
    print("This car doesn't need a gas tank!")
```

## 13. Instance as Attribute - Object Composition

**Definition**: Using an instance of one class as an attribute in another class.

```python
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # Instance as attribute
```

## 14. Importing Classes - Module Usage

**Definition**: Bringing classes from one module into another module for use.

```python
from car import Car
from electric_car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
```

**Exercise 9.3 - Users:**
```python
# Exercise 9.3: User class with attributes
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")

user1 = User('john', 'doe', 30, 'new york')
user2 = User('jane', 'smith', 25, 'los angeles')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
```

**Exercise 9.4 - Restaurants (Extended):**
```python
# Exercise 9.4: Restaurant with number served
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")
        print(f"Number Served: {self.number_served}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, additional):
        self.number_served += additional

restaurant = Restaurant('sukiya', 'japanese beef rice')
restaurant.describe_restaurant()

restaurant.set_number_served(100)
restaurant.describe_restaurant()

restaurant.increment_number_served(50)
restaurant.describe_restaurant()
```

**Exercise 9.5 - Users (Extended):**
```python
# Exercise 9.5: User with login attempts
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
        print(f"Login Attempts: {self.login_attempts}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('john', 'doe', 30, 'new york')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.describe_user()

user.reset_login_attempts()
user.describe_user()
```

**Exercise 9.6 - Restaurants (Inheritance):**
```python
# Exercise 9.6: Ice cream stand inheriting from restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open now.")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']
    
    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

ice_cream_stand = IceCreamStand('scoops')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
```

**Exercise 9.7 - Users (Admin):**
```python
# Exercise 9.7: Admin user inheriting from user
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('admin', 'user', 35, 'headquarters')
admin.describe_user()
admin.show_privileges()
```

**Exercise 9.8 - Users (Privileges):**
```python
# Exercise 9.8: Separate privileges class
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"\nUser Information:")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location.title()}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name.title()}! Welcome back.")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

admin = Admin('admin', 'user', 35, 'headquarters')
admin.describe_user()
admin.privileges.show_privileges()
```

**Exercise 9.13 - Dice:**
```python
# Exercise 9.13: Die class
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll(self):
        return randint(1, self.sides)

# Create a 6-sided die
die = Die()
results = []

for roll_num in range(10):
    result = die.roll()
    results.append(result)

print("10 rolls of a 6-sided die:")
print(results)

# Create a 10-sided die
die_10 = Die(10)
results_10 = []

for roll_num in range(10):
    result = die_10.roll()
    results_10.append(result)

print("\n10 rolls of a 10-sided die:")
print(results_10)
```

## Practical Examples from Chapter 9

### Working with Classes

Chapter 9 introduces object-oriented programming with classes. Here are the key files:

**Basic Class Definition:**
```python
# Chapter09/901_dog.py
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

**Advanced Class with Methods:**
```python
# Chapter09/902_car.py
class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

**Inheritance and Class Relationships:**
```python
# Chapter09/electric_car.py
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

## Key Takeaways

- Classes are blueprints for creating objects
- Objects are instances of classes
- Attributes store data in objects
- Methods define behavior of objects
- `__init__()` initializes new instances
- `self` refers to the current instance
- Inheritance creates class relationships
- Child classes inherit from parent classes
- `super()` calls parent class methods
- Method overriding customizes behavior
- Objects can contain other objects
- Import classes to use them in other modules
- Classes help organize and structure code 