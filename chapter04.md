# Chapter 4: Working with Lists

## Introduction

**Key Points**:
- Learn to loop through entire lists efficiently
- Use `for` loops to perform actions on every item
- Work with lists of any length (thousands to millions)
- Automate repetitive tasks

## Looping Through an Entire List

**Key Points**:
- Use `for` loops to iterate through lists
- Avoid repetitive code for long lists
- Code adapts to list length changes
- Python manages iteration internally

**Basic for Loop**:
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

**Output**:
```
alice
david
carolina
```

**Loop Structure**:
- `for item in list:` - Loop header
- Indented code block - Loop body
- Executes once for each item
- Variable name should be meaningful

### A Closer Look at Looping

**Key Points**:
- Looping automates repetitive tasks
- Python retrieves each value sequentially
- Steps repeat for each item in list
- Choose meaningful variable names

**Loop Execution**:
1. Python retrieves first value from list
2. Associates value with loop variable
3. Executes indented code block
4. Repeats for each remaining item
5. Moves to code after loop

**Naming Conventions**:
```python
for cat in cats:        # Good
for dog in dogs:        # Good
for item in list_of_items:  # Good
for x in y:             # Avoid
```

**Best Practices**:
- Use singular names for loop variables
- Use plural names for lists
- Choose descriptive names
- Loop executes regardless of list length

### Doing More Work Within a for Loop

You can do just about anything with each item in a for loop. Let's build on the previous example by printing a message to each magician, telling them that they performed a great trick:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

The only difference in this code is at u where we compose a message to each magician, starting with that magician's name. The first time through the loop the value of magician is 'alice', so Python starts the first message with the name 'Alice'. The second time through the message will begin with 'David', and the third time through the message will begin with 'Carolina'.

The output shows a personalized message for each magician in the list:

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
```

You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list. Therefore, you can do as much work as you like with each value in the list.

Let's add a second line to our message, telling each magician that we're looking forward to their next trick:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

Because we have two print statements, each person in the list gets two personalized messages, and the newline (\n) in the second print statement inserts a blank line after each pass through the loop. This creates a set of messages that are nicely grouped for each person in the list:

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

You can use as many lines as you like in your for loops. In practice you'll often find it useful to do a number of different operations with each item in a list when you use a for loop.

### Doing Something After a for Loop

What happens once a for loop has finished executing? Usually, you'll want to summarize a block of output or move on to other work that your program must accomplish.

Any lines of code after the for loop that are not indented are executed once without repetition. Let's write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show. To display this group message after all of the individual messages have been printed, we place the thank you message after the for loop, without indentation:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

The first two calls to print() are repeated once for each magician in the list, as you saw earlier. However, because the third print() call is not indented, it's executed only once:

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!
```

When you're processing data using a for loop, you'll find that this is a good way to summarize an operation that was performed on an entire dataset. For example, you might use a for loop to initialize a game by running through a list of characters and displaying each character on the screen. You might then write some additional code after the loop that displays a "Play Now" button only once after all the characters have been drawn to the screen.

## Avoiding Indentation Errors

Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the lines that printed messages to individual magicians were part of the for loop because they were indented. Python's use of indentation makes code very readable. In most other programming languages, indentation is used only to help make code easier to read. In Python, indentation is required to make the code run. This is one of the ways Python forces you to write clean, readable code.

### Forgetting to Indent

Always indent the line after the for statement in a loop. If you forget, Python will remind you:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```

The call to print() should be indented, but it's not. When Python expects an indented block and doesn't find one, it lets you know which line it had a problem with:

```
File "magicians.py", line 3
    print(magician)
    ^
IndentationError: expected an indented block
```

You can usually resolve this kind of indentation error by indenting the line or lines immediately after the for statement.

### Forgetting to Indent Additional Lines

Sometimes your loop will run without any errors but won't produce the expected result. This can happen when you're trying to do several tasks in a loop and you forget to indent some of its lines.

For example, this is what happens when we forget to indent the second line in the loop that tells each magician we're looking forward to their next trick:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
```

The second print() call is missing indentation, so it's not part of the loop and will execute only once after the loop has finished running. Because the final value associated with magician is 'carolina', she is the only one who receives the "looking forward to the next trick" message:

```
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
```

This is a logical error. The syntax is valid Python code, but the code doesn't produce the desired result because a problem occurs in its logic. If you expect to see a certain action repeated once for each item in a list and it's executed only once, determine whether you need to indent one or more lines.

### Indenting Unnecessarily

If you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indentation:

```python
message = "Hello Python world!"
    print(message)
```

We don't need to indent the print() call, because it doesn't belong to a line above it; hence, Python reports that error:

```
File "hello_world.py", line 2
    print(message)
    ^
IndentationError: unexpected indent
```

You can avoid unexpected indentation errors by indenting only when you have a specific reason to do so. In the programs you're writing at this point, the only lines you should indent are the actions you want to repeat for each item in a for loop.

### Indenting Unnecessarily After the Loop

If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. Sometimes this prompts Python to report an error, but often you'll get a logical error that can be difficult to spot.

For example, let's see what happens when we accidentally indent the line that thanked the magicians as a group:

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")
```

Because the last line is indented, it's printed once for each person in the list:

```
Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you everyone, that was a great magic show!
```

This is another logical error, similar to the one in "Forgetting to Indent Additional Lines" on page 56. Because Python doesn't know what you're trying to accomplish with your code, it will run all valid code and produce the output you asked for, even if it's not what you intended when you wrote the code.

### Forgetting the Colon

The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)
```

If you accidentally forget the colon, as shown at u, you'll get a syntax error because Python doesn't know what you're trying to do. Although this is an easy error to fix, it's not always an easy error to spot. You'll see more examples of this kind of error in the next few chapters, and remembering to include the colon will help you avoid them.

## Making Numerical Lists

Many reasons exist to store a set of numbers. For example, you'll need to keep track of the positions of each character in a game, and you might want to keep track of a player's high scores as well. In data visualizations, you'll almost always work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude values, among other types of numerical sets.

Lists are ideal for storing sets of numbers, and Python provides a number of tools to help you work efficiently with lists of numbers. Once you understand how to use these tools effectively, your code will work well even when your lists contain millions of items.

### Using the range() Function

Python's range() function makes it easy to generate a series of numbers. For example, you can use the range() function to print a series of numbers like this:

```python
for value in range(1, 5):
    print(value)
```

Although this code looks like it should print the numbers from 1 to 5, it doesn't print the number 5:

```
1
2
3
4
```

In this example, range() prints only the numbers 1 through 4. This is another result of the off-by-one behavior you'll see often in programming languages. The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide. Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.

To print the numbers 1 through 5, you would use range(1, 6):

```python
for value in range(1, 6):
    print(value)
```

This time the output starts at 1 and ends at 5:

```
1
2
3
4
5
```

If your output is different than what you expect when you're using range(), try adjusting your end value by 1.

### Using range() to Make a List of Numbers

If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.

In the example in the previous section, we simply printed out a series of numbers. The same numbers can be converted to a list by wrapping range() with list():

```python
numbers = list(range(1, 6))
print(numbers)
```

And this is the result:

```
[1, 2, 3, 4, 5]
```

We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), Python uses that value as a step size when generating numbers.

For example, here's how to list the even numbers between 1 and 10:

```python
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```

In this example, the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11, and produces this result:

```
[2, 4, 6, 8, 10]
```

You can create almost any set of numbers you want to using the range() function. For example, consider how you might make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents. Here's how you might put the first 10 square numbers into a list:

```python
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
```

We start with an empty list called squares at u. We tell Python to loop through each value from 1 to 10 using the range() function. Inside the loop, the current value is raised to the second power and assigned to the variable square at v. Each new value of square is appended to the list squares at w. Finally, when the loop has finished running, the list of squares is printed at x:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

To write this code more concisely, omit the temporary variable square and append each new value directly to the list:

```python
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)
```

The code at u does the same work as the lines at v and w in the previous example. Each value in the loop is raised to the second power and then immediately appended to the list of squares.

You can use either of these approaches when you want to write more readable code. Sometimes using a temporary variable makes your code easier to read; other times it makes the code unnecessarily long. Focus first on writing code that you understand clearly, which does what you want it to do. Then look for more efficient approaches as you review your code.

### Simple Statistics with a List of Numbers

A few Python functions are helpful when working with lists of numbers. For example, you can easily find the minimum, maximum, and sum of a list of numbers:

```python
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

### List Comprehensions

The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. The following example builds the same list of square numbers you saw earlier but uses a list comprehension:

```python
squares = [value**2 for value in range(1, 11)]
print(squares)
```

To use this syntax, begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. Notice that no colon is used at the end of the for statement.

The result is the same list of square numbers you saw earlier:

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

It takes practice to write your own list comprehensions, but you'll find them worthwhile once you become comfortable creating ordinary for loops. When you're writing three or four lines of code to generate lists and it begins to feel repetitive, consider writing a list comprehension instead.

## Working with Part of a List

In Chapter 3 you learned how to access single elements in a list, and in this chapter you've been learning how to work with all the elements in a list. You can also work with a specific group of items in a list (which Python calls a slice).

### Slicing a List

To make a slice, you specify the index of the first and last elements you want to work with. As with the range() function, Python stops one item before the second index you specify. To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.

The following example involves a list of players on a team:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```

The code at u prints a slice of this list, which includes just the first three players. The output retains the structure of the list, but includes only the first three players:

```
['charles', 'martina', 'michael']
```

You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
```

This time the slice starts with 'martina' and ends with 'florence':

```
['martina', 'michael', 'florence']
```

If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
```

Without a starting index, Python starts at the beginning of the list:

```
['charles', 'martina', 'michael', 'florence']
```

A similar syntax works if you want a slice that includes the end of a list. For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
```

Python returns all items from the third item through the end of the list:

```
['michael', 'florence', 'eli']
```

This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list. Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can slice any list by including a negative index:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
```

This prints the names of the last three players and would continue to work even if the list of players had a different length.

### Looping Through a Slice

You can use a slice in a for loop if you want to loop through a subset of the elements in a list. In the next example we loop through the first three players and print their names as part of a simple roster:

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
```

Instead of looping through the entire list of players, Python loops through only the first three names:

```
Here are the first three players on my team:
Charles
Martina
Michael
```

Slices are very useful in a number of situations. For instance, when you're creating a game, you could add a player's final score to a list every time that player finishes playing. You could then get a player's top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores. When you're working with data, you can use slices to process your data in chunks of a specific size. Or when you're building a web application, you could use slices to display information in a series of pages with an appropriate amount of information on each page.

### Copying a List

Often, you'll want to start with an existing list and make an entirely new list based on the first one. Let's explore how copying a list works and examine one situation where copying a list is useful.

To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.

For example, imagine we have a list of our favorite foods and want to make a separate list of foods that a friend likes. This friend likes everything in our original list so far, so we can create their list by copying ours:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

We make a copy of my_foods by asking for a slice of my_foods without specifying any indices and store the copy in friend_foods. When we print each list, we see that they both contain the same foods:

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```

To prove that we actually have two separate lists, we'll add a new food to each list and show that each list keeps track of the appropriate person's favorite foods:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

My_foods gets 'cannoli' added to it, and friend_foods gets 'ice cream' added to it:

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'ice cream']
```

The output shows that 'cannoli' now appears in my list of favorite foods but 'ice cream' doesn't. At the same time, 'ice cream' appears in my friend's list but 'cannoli' doesn't. If we had simply set friend_foods = my_foods, we would not produce two separate lists. For example, here's what happens when you try to copy a list without using a slice:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

# This doesn't work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

Instead of storing a copy of my_foods in friend_foods at u, we set friend_foods equal to my_foods. This syntax actually tells Python to associate the new variable friend_foods with the list that's already contained in my_foods, so both variables point to the same list. As a result, when we add 'cannoli' to my_foods, we'll also see it in friend_foods. Similarly, 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.

The output shows that both lists are the same now, which is not what we wanted:

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```

**Note:** Don't worry about the details yet, but this behavior is because when you set friend_foods = my_foods, you're asking Python to connect the new variable friend_foods to the list that's already stored in my_foods, so both variables point to the same list. You'll see this behavior again when you work with more complex data structures, and you'll learn how to control it when you need to.

## Try It Yourself

The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.

1. **Counting to Twenty**: Use a for loop to print the numbers from 1 to 20, inclusive.
2. **One Million**: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
3. **Summing a Million**: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
4. **Odd Numbers**: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
5. **Threes**: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
6. **Cubes**: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
7. **Cube Comprehension**: Use a list comprehension to generate a list of the first 10 cubes.

## Summary

In this chapter you learned how to work efficiently with the elements in a list. You learned how to work through a list using a for loop, how Python uses indentation to structure a program, and how to avoid some common indentation errors. You learned to make simple numerical lists, as well as a few operations you can perform on numerical lists. You learned how to slice a list to work with only part of it, and how to copy lists properly using a slice. You also learned about tuples, which provide some advantages over lists in terms of data integrity.

In Chapter 5 you'll learn to use if statements to automatically respond to different conditions in your data. You'll learn to string together relatively complex sets of conditional tests so that your programs will respond appropriately to exactly the kind of situation or data you expect.

## Key Takeaways

**for Loops**:
- Use `for item in list:` to iterate through lists
- Indented code block executes for each item
- Choose meaningful variable names
- Loop adapts to list length automatically

**List Operations**:
- `range()` creates sequences of numbers
- `list()` converts range to list
- `min()`, `max()`, `sum()` work on lists
- List comprehensions create lists efficiently

**Slicing**:
- `list[start:end]` gets subset of list
- `list[:]` creates copy of entire list
- `list[start:]` from start to end
- `list[:end]` from beginning to end

**Tuples**:
- Use parentheses `()` to create tuples
- Immutable (cannot be changed)
- Use for data that shouldn't change
- Access elements like lists with `[]` 