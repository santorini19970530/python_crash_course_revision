# Chapter 5: if Statements

## Introduction

**Key Points**:
- `if` statements examine conditions and respond accordingly
- Write conditional tests to check conditions
- Create simple and complex if statements
- Use if statements with lists in for loops

## A Simple Example

**Key Points**:
- `if` tests respond to special situations
- Check conditions and take different actions
- Combine with loops for conditional processing

**Example**:
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

**Output**:
```
Audi
BMW
Subaru
Toyota
```

**How it Works**:
- Loop checks each car name
- If car is 'bmw', print in uppercase
- Otherwise, print in title case

## Conditional Tests

**Key Points**:
- Conditional tests evaluate to True or False
- Python uses True/False to decide if code executes
- If True: execute code following if statement
- If False: ignore code following if statement

### Checking for Equality

**Key Points**:
- Use `==` to check equality (not `=`)
- `=` assigns values, `==` compares values
- Returns True if values match, False otherwise

**Example**:
```python
>>> car = 'bmw'
>>> car == 'bmw'
True
```

**Non-Equal Example**:
```python
>>> car = 'audi'
>>> car == 'bmw'
False
```

**Operators**:
- `==` - Equal to
- `!=` - Not equal to
- `=` - Assignment (not comparison)

### Ignoring Case When Making Comparisons

Testing for equality is case sensitive in Python. For example, two values with different capitalization are considered different:

```python
>>> car = 'Audi'
>>> car == 'audi'
False
```

If case matters, this behavior is advantageous. But if case doesn't matter and instead you just want to test the value of the variable, you can convert the variable's value to lowercase before doing the comparison:

```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
```

The test car.lower() == 'audi' converts the value of car to lowercase and then compares the lowercase value to the string 'audi'. The two strings match, so Python returns True. This approach is useful if you want to test the value of a variable regardless of the case in which it was entered.

The lower() method doesn't change the value that was originally stored in car, so you can do this kind of comparison without affecting the original variable:

```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car
'Audi'
```

### Checking for Inequality

When you want to determine whether two values are not equal, you can combine an exclamation point and an equal sign (!=). The exclamation point represents not, as it does in many programming languages.

Let's use another if statement to examine how to use the inequality operator. We'll store a requested pizza topping in a variable and then print a message if the person did not enter anchovies as their topping:

```python
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

This code compares the value of requested_topping to the value 'anchovies'. If these two values are not equal, Python returns True and executes the code following the if statement. If the two values are equal, Python returns False and does not run the code following the if statement.

Because the value of requested_topping is not 'anchovies', the print statement is executed:

```
Hold the anchovies!
```

Most of the conditional expressions you write will test for equality, but sometimes you'll find it more efficient to test for inequality.

### Numerical Comparisons

Testing numerical values is pretty straightforward. For example, the following code checks whether a person is 18 years old:

```python
>>> age = 18
>>> age == 18
True
```

You can also test to see if two numbers are not equal. For example, the following code prints a message if the given answer is not correct:

```python
answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")
```

The conditional test at u passes, because the value of answer (17) is not equal to 42. Because the test passes, the indented code block is executed:

```
That is not the correct answer. Please try again!
```

You can include various mathematical comparisons in your conditional statements as well, such as less than, less than or equal to, greater than, and greater than or equal to:

```python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

Each mathematical comparison can be used as part of an if statement, which can help you detect the exact conditions of interest to you.

### Checking Multiple Conditions

You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action. Other times you might be satisfied with one condition being True. The keywords and and or can help you in these situations.

#### Using and to Check Multiple Conditions

To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes, the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.

For example, to check whether two people are both over 21, you can use the following test:

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```

To improve readability, you can use parentheses around the individual tests, but they are not required. If you use parentheses, your test would look like this:

```python
(age_0 >= 21) and (age_1 >= 21)
```

#### Using or to Check Multiple Conditions

The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or expression fails only when both individual tests fail.

Let's consider two ages again, but this time we'll look for either person to be over 21:

```python
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

We start with two age variables, age_0 and age_1. Because the test for age_0 is True, the overall expression evaluates to True. We then lower age_0 to 18. In the second test, both conditions are now False, so the overall expression evaluates to False.

### Checking Whether a Value Is in a List

Sometimes it's important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a new username already exists in a list of current usernames before completing someone's registration on a website. In a mapping project, you might want to check whether a requested location is available before adding it to a map.

To find out whether a particular value is already in a list, use the keyword in. Let's consider some code you might write for a pizzeria. We'll make a list of toppings a customer has requested for a pizza and then check whether certain toppings are in the list.

```python
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
>>> 'mushrooms' in requested_toppings
True
>>> 'pepperoni' in requested_toppings
False
```

The keyword in tells Python to check for the existence of 'mushrooms' and 'pepperoni' in the list requested_toppings. This technique is quite powerful because you can easily create a list of essential values and then easily check whether the value you're testing matches one of the values in the list.

### Checking Whether a Value Is Not in a List

Other times you want to check that a value is not in a list before taking an action. You can use the keyword not in this situation. For example, consider a list of users who are banned from commenting in a forum. You can check whether a user has been banned before allowing that person to submit a comment:

```python
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
```

The if statement here reads quite clearly. If the value of user is not in the list banned_users, Python returns True and executes the indented print statement.

The user 'marie' is not in the list banned_users, so she sees a message that she can post a response:

```
Marie, you can post a response if you wish.
```

### Boolean Expressions

As you learn more about programming, you'll hear the term Boolean expression at some point. A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.

Boolean values are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website:

```python
game_active = True
can_edit = False
```

Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

## if Statements

When you understand conditional tests, you can start writing if statements. Several different kinds of if statements exist, and your choice of which to use depends on the number of conditions you need to test. You saw several examples of if statements in the discussion about conditional tests, but now let's dig deeper into the topic.

### Simple if Statements

The simplest kind of if statement has one test and one action:

```python
if conditional_test:
    do something
```

You can put any conditional test in the first line and just about any action in the indented block following the test. If the conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.

Let's say we have a variable representing a person's age, and we want to know if that person is old enough to vote:

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

Python checks to see whether the value of age is greater than or equal to 18. It is, so Python executes both print statements:

```
You are old enough to vote!
Have you registered to vote yet?
```

The indentation plays the same role in if statements as it did in for loops. All indented lines after an if statement will be executed if the test passes, and the entire block of indented lines will be ignored if the test does not pass.

You can have as many lines of code as you want in the block following the if statement. Let's add another line of output if the person is old enough to vote, asking if they have registered yet:

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

The conditional test passes, and both print statements are indented, so both lines are printed:

```
You are old enough to vote!
Have you registered to vote yet?
```

If the value of age were less than 18, this program would produce no output.

### if-else Statements

Often, you'll want to take one action when a conditional test passes and a different action in all other cases. Python's if-else syntax makes this possible. An if-else block is similar to a simple if statement, but the else statement allows you to define an action or set of actions that are executed when the conditional test fails.

We'll display the same message we had before if the person is old enough to vote, but this time we'll add a message for anyone who is not old enough to vote:

```python
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
```

If the conditional test at u passes, the first block of indented print statements is executed. If the test evaluates to False, the else block at v is executed. Because age is less than 18 this time, the conditional test fails and the code in the else block is executed:

```
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

This code works because there are always exactly two possibilities: either someone is old enough to vote or they aren't. The if-else structure works well in situations in which you want Python to always execute one of two possible actions. In a simple if-else chain like this, one of the two actions will always be executed.

### The if-elif-else Chain

Often, you'll need to test more than two possible situations, and to evaluate these you can use Python's if-elif-else syntax. Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code following that test is executed and Python skips the rest of the tests.

Many real-world situations involve more than two possible conditions. For example, consider an amusement park that charges different rates for different age groups:

- Admission for anyone under age 4 is free.
- Admission for anyone between the ages of 4 and 18 is $25.
- Admission for anyone age 18 or older is $40.

How can we use an if statement to determine a person's admission rate? The following code tests for the age group of a person and then prints an admission price message:

```python
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

The if test at u checks whether a person is under 4 years old. If the test passes, an appropriate message is printed and Python skips the rest of the tests. The elif line at v is really another if test, which runs only if the previous test failed. At this point in the chain, we know the person is at least 4 years old because the first test failed. If the person is under 18, an appropriate message is printed and Python skips the else block. If both the if and elif tests fail, Python runs the code in the else block at w.

In this example the test at v evaluates to True, so its code block is executed:

```
Your admission cost is $25.
```

Any age greater than 17 would cause the first two tests to fail. In these situations, the else block would be executed and the admission price would be $40.

Rather than printing the admission price within the if-elif-else block, it would be more concise to set just the price inside the if-elif-else chain and then have a simple print statement that runs after the chain has been evaluated:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")
```

This approach is more efficient than the previous version because it makes just one print statement call instead of three. It's also easier to modify: if you need to change the output message, you only need to change it in one place rather than three places.

### Using Multiple elif Blocks

You can use as many elif blocks in your code as you like. For example, if the amusement park were to implement a discount for seniors, you could add one more conditional test to the code to determine whether someone qualifies for the senior discount. Let's say that anyone 65 or older pays half the regular admission, or $20:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")
```

Most of this code is unchanged. The second elif block at u now checks to make sure a person is less than age 65 before assigning them the full admission rate of $40. Notice that the value assigned in the else block is now 20, which is the price for anyone 65 or older.

### Omitting the else Block

Python does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest:

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")
```

The extra elif block at u makes the code clearer, because it's more obvious that we only want to charge $20 for people 65 or older when we explicitly list that condition.

### Testing Multiple Conditions

The if-elif-else chain is powerful, but it's only appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, it skips the rest of the tests. This behavior is beneficial, because it's efficient and allows you to test for one specific condition.

However, sometimes it's important to check all of the conditions of interest. In this case, you should use a series of simple if statements with no elif or else blocks. This approach makes sense when more than one condition could be True, and you want to act on every condition that is True.

Let's reconsider the pizzeria example. If someone requests a two-topping pizza, you'll want to be sure to include both toppings on their pizza:

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

We start with a list containing the requested toppings. The if statement at u checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that topping. The test for pepperoni at v is a simple if statement, not an elif or else statement, so this test is run regardless of whether the previous test passed or not. The code at w checks whether extra cheese was requested regardless of the results from the first two tests. These three independent tests are executed every time this program runs.

Because every condition in this example is evaluated, both mushrooms and extra cheese are added to the pizza:

```
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes. Here's what it would look like with an if-elif-else block:

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

In this version, no cheese is added because the 'mushrooms' test is the first to pass, and the elif statements are skipped. The customer would not get their extra cheese:

```
Adding mushrooms.

Finished making your pizza!
```

In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

## Using if Statements with Lists

You can do some interesting work when you combine lists and if statements. You can watch for special values that need to be treated differently than other values in the list. You can manage changing conditions efficiently, such as the availability of certain items in a restaurant throughout a shift. You can also begin to prove that your code works as you expect it to in all possible situations.

### Checking for Special Items

This chapter began with a simple example that showed how to handle a special case like a BMW that needed to be printed in a different format than other cars. Now that you have a basic understanding of conditional tests and if statements, let's take a closer look at how you can watch for special values in a list and handle those values appropriately.

Let's continue with the pizzeria example. The pizzeria displays a message whenever a topping is added to your pizza, as it's being made. The code for this can be written very efficiently by making a list of toppings the customer has requested and using a loop to announce each topping as it's added to the pizza:

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

The output is straightforward because this code is just a simple for loop:

```
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!
```

But what if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

This time we check each requested item before adding it to the pizza. The code at u checks if the person requested green peppers. If so, we display a message informing them why they can't have green peppers. The else block at v ensures that all other toppings will be added to the pizza.

The output shows that each requested topping is handled appropriately:

```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### Checking That a List Is Not Empty

We've made a simple assumption about every list we've worked with so far; we've assumed that each list has at least one item in it. Soon we'll let users provide the information that's stored in a list, so we won't be able to assume that a list has any items in it each time a loop is run. In this case, it's a good idea to check whether a list is empty before running a for loop.

As an example, let's check whether the list of requested toppings is empty before building the pizza. If the list is empty, we'll prompt the user and make sure they want a plain pizza. If the list is not empty, we'll build the pizza as before:

```python
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

This time we start out with an empty list of requested toppings at u. Instead of jumping right into a for loop, we do a quick check at v. When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False. If requested_toppings passes the conditional test, we run the same for loop we used in the previous example. If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings.

The list is empty in this case, so the output asks if the user really wants a plain pizza:

```
Are you sure you want a plain pizza?
```

If the list had items in it, the output would show each requested topping being added to the pizza.

### Using Multiple Lists

People will ask for just about anything, especially when it comes to pizza toppings. What if a customer actually asks for french fries on their pizza? You can use lists and if statements to make sure your input makes sense before you act on it.

Let's watch out for unusual topping requests before we build a pizza. The following example defines two lists. The first is a list of available toppings at the pizzeria, and the second is the list of toppings that the user has requested. This time, each item in requested_toppings is checked against the list of available toppings before it's added to the pizza:

```python
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

At u we define a list of available toppings at this pizzeria. Note that this could be a tuple if the pizzeria has a stable selection of toppings. At v, we make a list of toppings that a customer has requested. Note the unusual request, 'french fries'. At w we loop through the list of requested toppings. Inside the loop, we first check to see if each requested topping is actually in the list of available toppings. If it is, we add it to the pizza. If the requested topping is not in the list of available toppings, the else block will run and print a message telling the user which toppings are unavailable.

This code syntax works whether the special value is 'mushrooms' or 'french fries'. Each requested topping is checked, and each topping is handled appropriately:

```
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

In just a few lines of code, we've managed to handle this situation realistically and efficiently!

## Try It Yourself

1. **Conditional Tests**: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:
   ```python
   car = 'subaru'
   print("Is car == 'subaru'? I predict True.")
   print(car == 'subaru')
   ```
   Look closely at your results, and make sure you understand why each line evaluates to True or False.

2. **More Conditional Tests**: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
   - Tests for equality and inequality with strings
   - Tests using the lower() method
   - Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
   - Tests using the and keyword and the or keyword
   - Test whether an item is in a list
   - Test whether an item is not in a list

3. **Alien Colors #1**: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
   - Write an if statement to test whether the alien's color is green. If it is, print a message that the player just earned 5 points.
   - Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

4. **Alien Colors #2**: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
   - If the alien's color is green, print a statement that the player just earned 5 points for shooting the alien.
   - If the alien's color isn't green, print a statement that the player just earned 10 points.
   - Write one version of this program that runs the if block and another that runs the else block.

5. **Alien Colors #3**: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
   - If the alien is green, print a message that the player earned 5 points.
   - If the alien is yellow, print a message that the player earned 10 points.
   - If the alien is red, print a message that the player earned 15 points.
   - Write three versions of this program, making sure each message is printed for the appropriate color alien.

6. **Stages of Life**: Write an if-elif-else chain that determines a person's stage of life. Set a value for the variable age, and then:
   - If the person is less than 2 years old, print a message that the person is a baby.
   - If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
   - If the person is at least 4 years old but less than 13, print a message that the person is a kid.
   - If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
   - If the person is at least 20 years old but less than 65, print a message that the person is an adult.
   - If the person is age 65 or older, print a message that the person is an elder.

7. **Favorite Fruit**: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
   - Make a list of your three favorite fruits and call it favorite_fruits.
   - Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

## Summary

In this chapter you learned how to write conditional tests, which always evaluate to True or False. You learned to write simple if statements, if-else chains, and if-elif-else chains. You began using these structures to identify particular conditions you need to test and to know when those conditions have been met in your programs.

You learned to handle certain items in a list differently than all other items while continuing to utilize the efficiency of a for loop. You also learned Python's style of formatting if statements, which helps ensure that your code is easy to read and understand.

In Chapter 6 you'll learn about Python's dictionaries. A dictionary is similar to a list, but it allows you to connect pieces of information. You'll learn to build dictionaries, loop through them, and use them in combination with lists and if statements. Learning about dictionaries will enable you to model a variety of real-world objects more accurately.

## Key Takeaways

**Conditional Tests**:
- Use `==` for equality (not `=`)
- Use `!=` for inequality
- Tests evaluate to True or False
- Case-sensitive by default

**if Statements**:
- `if condition:` - Simple if
- `if-else` - Two alternatives
- `if-elif-else` - Multiple alternatives
- Indent code blocks properly

**Comparison Operators**:
- `==` - Equal to
- `!=` - Not equal to
- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal
- `<=` - Less than or equal

**Logical Operators**:
- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `in` - Check if item in list
- `not in` - Check if item not in list

**Best Practices**:
- Use meaningful variable names
- Test for specific conditions
- Handle edge cases
- Keep code readable 