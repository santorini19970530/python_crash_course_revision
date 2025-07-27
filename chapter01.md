# Chapter 1: Getting Started

## Introduction

In this chapter, you'll run your first Python program and learn how to set up your programming environment. You'll install Python on your system if it isn't already there, and you'll install a text editor to make it easier to write Python code.

## What Really Happens When You Run hello_world.py

Let's take a closer look at what Python does when you run hello_world.py. As it turns out, Python does a fair amount of work, even when it runs a simple program:

```python
print("Hello Python world!")
```

When you run this code, you should see this output:
```
Hello Python world!
```

When you run the file hello_world.py, the ending .py indicates that the file is a Python program. Your editor then runs the file through the Python interpreter, which reads through the program and determines what each word in the program means. For example, when the interpreter sees the word print followed by parentheses, it prints to the screen whatever is inside the parentheses.

As you write your programs, your editor highlights different parts of your program in different ways. For example, it recognizes that print() is the name of a function and displays that word in one color. It recognizes that "Hello Python world!" is not Python code and displays that phrase in a different color. This feature is called syntax highlighting and is quite useful as you start to write your own programs.

## Setting Up Your Programming Environment

### Python on Different Operating Systems

Python is a cross-platform programming language, which means it runs on all the major operating systems. Any Python program you write should run on any modern computer that has Python installed. However, the methods for setting up Python on different operating systems vary slightly.

In this section, you'll learn how to set up Python on your system. You'll first check whether a recent version of Python is installed on your system and install it if it's not. Then you'll install Sublime Text. These are the only two steps that are different for each operating system.

### Python on Windows

Windows doesn't always come with Python, so you'll probably need to install it, and then install Sublime Text.

**Installing Python:**
1. Check whether Python is installed on your system by opening a command window
2. Enter `python` in lowercase
3. If you get a Python prompt (>>>), Python is installed
4. If you see an error message, download Python from https://python.org/
5. Make sure to select "Add Python to PATH" during installation

**Running Python in a Terminal Session:**
```bash
C:\> python
Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Installing Sublime Text:**
Download from https://sublimetext.com/ and run the installer.

### Python on macOS

Python is already installed on most macOS systems, but it's most likely an outdated version.

**Checking Whether Python 3 Is Installed:**
```bash
$ python
Python 2.7.15 (default, Aug 17 2018, 22:39:05)
[GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.2)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>
```

To check for Python 3, use:
```bash
$ python3 --version
Python 3.7.2
```

**Installing the Latest Version of Python:**
Download from https://python.org/ and run the installer.

**Installing Sublime Text:**
Download from https://sublimetext.com/ and drag to Applications folder.

### Python on Linux

Linux systems are designed for programming, so Python is already installed on most Linux computers.

**Checking Your Version of Python:**
```bash
$ python3
Python 3.7.2 (default, Dec 27 2018, 04:01:51)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

**Installing Sublime Text:**
Install from Ubuntu Software Center or equivalent.

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