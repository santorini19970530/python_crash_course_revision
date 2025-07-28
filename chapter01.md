# Chapter 1: Getting Started

## Introduction

**Key Points**:
- Run your first Python program
- Set up your programming environment
- Install Python if needed
- Install a text editor for writing code

## What Really Happens When You Run hello_world.py

**Key Points**:
- `.py` extension indicates Python program
- Python interpreter reads and processes code
- Syntax highlighting helps identify code elements
- Interpreter determines meaning of each word

**First Program**:
```python
print("Hello Python world!")
```

**Output**:
```
Hello Python world!
```

**How it Works**:
- Editor runs file through Python interpreter
- Interpreter reads program line by line
- `print()` function displays text to screen
- Syntax highlighting shows different code elements

## Setting Up Your Programming Environment

**Key Points**:
- Python is cross-platform (runs on all major OS)
- Setup varies by operating system
- Check if Python is installed first
- Install text editor (Sublime Text recommended)

### Python on Different Operating Systems

**Key Points**:
- Python runs on Windows, macOS, and Linux
- Programs work on any system with Python
- Setup methods vary by OS
- Two main steps: install Python, install text editor

### Python on Windows

**Key Points**:
- Windows doesn't come with Python by default
- Need to install Python manually
- Install Sublime Text for editing

**Installing Python**:
1. Open command window
2. Type `python` to check if installed
3. If error, download from https://python.org/
4. Select "Add Python to PATH" during installation

**Running Python**:
```bash
C:\> python
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Installing Sublime Text**:
- Download from https://sublimetext.com/
- Run the installer

### Python on macOS

**Key Points**:
- Python comes pre-installed but may be outdated
- Check for Python 3 specifically
- Install latest version if needed

**Checking Python 3**:
```bash
$ python3 --version
Python 3.7.2
```

**Installing Python**:
- Download from https://python.org/
- Run the installer

**Installing Sublime Text**:
- Download from https://sublimetext.com/
- Drag to Applications folder

### Python on Linux

**Key Points**:
- Python usually pre-installed on Linux
- Designed for programming
- Use `python3` command

**Checking Python**:
```bash
$ python3
Python 3.7.2 (default, Dec 27 2018, 04:01:51)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Installing Sublime Text**:
- Install from Ubuntu Software Center
- Or use package manager

## Running a Hello World Program

### Configuring Sublime Text to Use the Correct Python Version

If you use the `python3` command, you'll need to configure Sublime Text:

1. Go to Tools → Build System → New Build System
2. Enter the following configuration:
```json
{
"cmd": ["python3", "-u", "$file"],
}
```
3. Save as `Python3.sublime-build`

### Running hello_world.py

1. Create a folder called `python_work` for your projects
2. Open Sublime Text and save an empty file as `hello_world.py`
3. Enter the following code:
```python
print("Hello Python world!")
```
4. Run the program using Tools → Build or CTRL-B

You should see:
```
Hello Python world!
[Finished in 0.1s]
```

## Troubleshooting

If you can't get hello_world.py to run, here are some remedies:

- Check the traceback for error messages
- Step away from your computer, take a short break, and try again
- Remember that syntax is very important in programming
- Start over again if needed
- Ask someone else to follow the steps
- Find someone who knows Python and ask for help
- Check the book's companion website
- Ask for help online (see Appendix C)

## Running Python Programs from a Terminal

### On Windows
```bash
C:\> cd Desktop\python_work
C:\Desktop\python_work> dir
hello_world.py
C:\Desktop\python_work> python hello_world.py
Hello Python world!
```

### On macOS and Linux
```bash
~$ cd Desktop/python_work/
~/Desktop/python_work$ ls
hello_world.py
~/Desktop/python_work$ python hello_world.py
Hello Python world!
```

## Try It Yourself

The exercises in this chapter are exploratory in nature. Starting in Chapter 2, the challenges you'll solve will be based on what you've learned.

1. **python.org**: Explore the Python home page (https://python.org/) to find topics that interest you.
2. **Hello World Typos**: Open the hello_world.py file you just created. Make a typo somewhere in the line and run the program again. Can you make a typo that generates an error? Can you make sense of the error message? Can you make a typo that doesn't generate an error?
3. **Infinite Skills**: If you had infinite programming skills, what would you build? Take a few minutes now to describe three programs you want to create.

## Summary

In this chapter, you learned a bit about Python in general, and you installed Python on your system if it wasn't already there. You also installed a text editor to make it easier to write Python code. You ran snippets of Python code in a terminal session, and you ran your first program, hello_world.py. You probably learned a bit about troubleshooting as well.

In the next chapter, you'll learn about the different kinds of data you can work with in your Python programs, and you'll use variables as well.

## Key Takeaways

**Getting Started**:
- Install Python on your system
- Install a text editor (Sublime Text recommended)
- Create your first Python program
- Learn to run programs from terminal

**Python Installation**:
- **Windows**: Download from python.org, add to PATH
- **macOS**: Check for Python 3, install if needed
- **Linux**: Usually pre-installed, use `python3` command

**First Program**:
- Use `.py` extension for Python files
- `print()` function displays text
- Run with `python filename.py`
- Syntax highlighting helps identify code

**Troubleshooting**:
- Check error messages carefully
- Verify Python installation
- Use correct file extensions
- Ask for help when needed 