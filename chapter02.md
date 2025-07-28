# Chapter 2: Variables and Simple Data Types

## Introduction

**Key Points**:
- Learn about different data types in Python
- Use variables to represent data in programs
- Understand how Python processes code

## What Really Happens When You Run hello_world.py

**Key Points**:
- `.py` extension indicates Python program
- Python interpreter reads and processes code
- Syntax highlighting helps identify code elements
- Interpreter determines meaning of each word

**Example**:
```python
print("Hello Python world!")
```

**Output**:
```
Hello Python world!
```

## Variables

**Key Points**:
- Variables store data values
- Use `=` to assign values to variables
- Variables can be changed during program execution
- Python keeps track of current variable values

**Example**:
```python
message = "Hello Python world!"
print(message)
```

**Output**:
```
Hello Python world!
```

**Changing Variables**:
```python
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
```

**Output**:
```
Hello Python world!
Hello Python Crash Course world!
```

## Naming and Using Variables

**Key Points**:
- Variable names can contain letters, numbers, and underscores
- Must start with letter or underscore (not number)
- No spaces allowed (use underscores)
- Avoid Python keywords and function names
- Use descriptive but short names
- Use lowercase for variables

**Naming Rules**:
- ✅ `message_1` (valid)
- ❌ `1_message` (invalid - starts with number)
- ✅ `greeting_message` (valid)
- ❌ `greeting message` (invalid - has space)
- ✅ `name` (better than `n`)
- ✅ `student_name` (better than `s_n`)

**Best Practices**:
- Use descriptive names
- Avoid single letters (except in loops)
- Be consistent with naming style
- Avoid confusing characters (l vs 1, O vs 0)

## Avoiding Name Errors When Using Variables

**Key Points**:
- Name errors are common programming mistakes
- Python provides helpful error messages
- Traceback shows where error occurred
- Check for spelling mistakes in variable names

**Common Error Example**:
```python
message = "Hello Python Crash Course reader!"
print(mesage)  # Typo: missing 's'
```

**Error Output**:
```
Traceback (most recent call last):
File "hello_world.py", line 2, in <module>
print(mesage)
NameError: name 'mesage' is not defined
```

**How to Fix**:
- Check variable name spelling
- Ensure variable is defined before use
- Look at line number in error message
- Common causes: typos, missing letters, wrong case

## Variables Are Labels

**Key Points**:
- Variables are labels that reference values
- Not boxes that store values
- Multiple variables can reference same value
- Important for understanding Python's behavior

## Strings

**Key Points**:
- Strings are series of characters
- Use single or double quotes
- Can contain quotes and apostrophes
- First data type to learn

**String Examples**:
```python
"This is a string."
'This is also a string.'
```

**Quotes in Strings**:
```python
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

### Changing Case in a String with Methods

**Key Points**:
- Methods are actions Python can perform on data
- Use dot notation: `string.method()`
- Methods often need parentheses (even if empty)
- Useful for data cleaning and formatting

**title() Method**:
```python
name = "ada lovelace"
print(name.title())
```

**Output**:
```
Ada Lovelace
```

**Other Case Methods**:
```python
name = "Ada Lovelace"
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace
```

**Common Uses**:
- `title()` - Capitalize first letter of each word
- `upper()` - Convert to all uppercase
- `lower()` - Convert to all lowercase (good for storing data)

### Using Variables in Strings

**Key Points**:
- Use f-strings to embed variables in strings
- Place `f` before opening quote
- Use braces `{}` around variable names
- Can use methods inside f-strings

**Basic f-string**:
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```

**Output**:
```
ada lovelace
```

**f-string with Methods**:
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
```

**Output**:
```
Hello, Ada Lovelace!
```

**f-string Features**:
- Embed variables directly in strings
- Can use methods inside braces
- More readable than concatenation
- Python 3.6+ feature

You can also use f-strings to compose a message, and then assign the entire message to a variable:

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
```

This code displays the message Hello, Ada Lovelace! as well, but by assigning the message to a variable we make the final print() call much simpler.

**Note:** F-strings were first introduced in Python 3.6. If you're using Python 3.5 or earlier, you'll need to use the format() method rather than this f syntax.

### Adding Whitespace to Strings with Tabs or Newlines

In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. You can use whitespace to organize your output so it's easier for users to read.

To add a tab to your text, use the character combination \t:

```python
>>> print("Python")
Python
>>> print("\tPython")
    Python
```

To add a newline in a string, use the character combination \n:

```python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab:

```python
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
```

Newlines and tabs will be very useful in the next two chapters when you start to produce many lines of output from just a few lines of code.

### Stripping Whitespace

Extra whitespace can be confusing in your programs. To programmers 'python' and 'python ' look pretty much the same. But to a program, they are two different strings. Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.

It's important to think about whitespace, because often you'll want to compare two strings to determine whether they are the same. For example, one important instance might involve checking people's usernames when they log in to a website. Extra whitespace can be confusing in much simpler situations as well. Fortunately, Python makes it easy to eliminate extraneous whitespace from data that people enter.

Python can look for extra whitespace on the right and left sides of a string. To ensure that no whitespace exists at the right end of a string, use the rstrip() method:

```python
>>> favorite_language = 'python '
>>> favorite_language
'python '
>>> favorite_language.rstrip()
'python'
>>> favorite_language
'python '
```

The value associated with favorite_language contains extra whitespace at the end of the string. When you ask Python for this value in a terminal session, you can see the space at the end of the value. When the rstrip() method acts on the variable favorite_language, this extra space is removed. However, it is only removed temporarily. If you ask for the value of favorite_language again, you can see that the string looks the same as when it was entered, including the extra whitespace.

To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:

```python
>>> favorite_language = 'python '
>>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'
```

To remove the whitespace from the string, you strip the whitespace from the right side of the string and then associate this new value with the original variable. Changing a variable's value is done often in programming. This is how a variable's value can be updated as a program is executed or in response to user input.

You can also strip whitespace from the left side of a string using the lstrip() method, or from both sides at once using strip():

```python
>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'
```

In this example, we start with a value that has whitespace at the beginning and the end. We then remove the extra space from the right side, from the left side, and from both sides. Experimenting with these stripping functions can help you become familiar with manipulating strings. In the real world, these stripping functions are used most often to clean up user input before it's stored in a program.

### Avoiding Syntax Errors with Strings

One kind of error that you might see with some regularity is a syntax error. A syntax error occurs when Python doesn't recognize a section of your program as valid Python code. For example, if you use an apostrophe within single quotes, you'll produce an error. This happens because Python interprets everything between the first single quote and the apostrophe as a string. It then tries to interpret the rest of the text as Python code, which causes errors.

Here's how to use single and double quotes correctly. Save this program as apostrophe.py and then run it:

```python
message = "One of Python's strengths is its diverse community."
print(message)
```

The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly:
```
One of Python's strengths is its diverse community.
```

However, if you use single quotes, Python can't identify where the string should end:

```python
message = 'One of Python's strengths is its diverse community.'
print(message)
```

You'll see the following output:
```
File "apostrophe.py", line 1
message = 'One of Python's strengths is its diverse community.'
^
SyntaxError: invalid syntax
```

In the output you can see that the error occurs right after the second single quote. This syntax error indicates that the interpreter doesn't recognize something in the code as valid Python code. Errors can come from a variety of sources, and I'll point out some common ones as they arise. You might see syntax errors often as you learn to write proper Python code. Syntax errors are also the least specific kind of error, so they can be difficult and frustrating to identify and correct.

**Note:** Your editor's syntax highlighting feature should help you spot some syntax errors quickly as you write your programs. If you see Python code highlighted as if it's English or English highlighted as if it's Python code, you probably have a mismatched quotation mark somewhere in your file.

## Numbers

Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on. Python treats numbers in several different ways, depending on how they're being used. Let's first look at how Python manages integers, because they're the simplest to work with.

### Integers

You can add (+), subtract (-), multiply (*), and divide (/) integers in Python:

```python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

In a terminal session, Python simply returns the result of the operation. Python uses two multiplication symbols to represent exponents:

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python supports the order of operations too, so you can use multiple operations in one expression. You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify:

```python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

The spacing in these examples has no effect on how Python evaluates the expressions; it simply helps you more quickly spot the operations that have priority when you're reading through the code.

### Floats

Python calls any number with a decimal point a float. This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number. Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately no matter where the decimal point appears.

For the most part, you can use decimals without worrying about how they behave. Simply enter the numbers you want to use, and Python will most likely do what you expect:

```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

But be aware that you can sometimes get an arbitrary number of decimal places in your answer:

```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

This happens in all languages and is of little concern. Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally. Just ignore the extra decimal places for now; you'll learn ways to deal with the extra places when you need to in the projects in Part II.

### Integers and Floats

When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float:

```python
>>> 4/2
2.0
```

If you mix an integer and a float in any other operation, you'll get a float as well:

```python
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

Python defaults to a float in any operation that uses a float, even if the output is a whole number.

### Underscores in Numbers

When you're writing long numbers, you can group digits using underscores to make large numbers more readable:

```python
>>> universe_age = 14_000_000_000
```

When you print a number that was defined using underscores, Python prints only the digits:

```python
>>> print(universe_age)
14000000000
```

Python ignores the underscores when storing these kinds of values. Even if you don't group the digits in threes, the value will still be unaffected. To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature works for integers and floats, but it's only available in Python 3.6 and later.

### Multiple Assignment

You can assign values to more than one variable using just a single line. This can help shorten your programs and make them easier to read; you'll use this technique most often when initializing a set of numbers.

For example, here's how you can initialize the variables x, y, and z to zero:

```python
>>> x, y, z = 0, 0, 0
```

You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respectively positioned variable. As long as the number of values matches the number of variables, Python will match them up correctly.

### Constants

A constant is like a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:

```python
MAX_CONNECTIONS = 5000
```

When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.

## Try It Yourself

Save each of the following exercises as a separate file with a name like name_cases.py. If you get stuck, take a break or see the suggestions in Appendix C.

1. **Simple Message**: Assign a message to a variable, and then print that message.
2. **Simple Messages**: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
3. **Personal Message**: Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"
4. **Name Cases**: Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case.
5. **Famous Quote**: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:
   ```
   Albert Einstein once said, "A person who never made a mistake never tried anything new."
   ```
6. **Famous Quote 2**: Repeat Exercise 2-5, but this time, represent the famous person's name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.
7. **Stripping Names**: Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
8. **Number Eight**: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results.

## Summary

In this chapter you learned to work with variables. You learned to use descriptive variable names and how to resolve name errors and syntax errors when they arise. You learned about strings and how to work with the individual characters in a string. You learned to use integers and floats, and some of the ways you can work with numerical data. You also learned to write explanatory comments to make your code easier for you and others to read. Finally, you read about the Zen of Python and how to approach your work as a programmer.

In Chapter 3 you'll learn to store collections of information in data structures called lists. You'll learn to work through a list, manipulating any piece of information in that list with just a few lines of code. 