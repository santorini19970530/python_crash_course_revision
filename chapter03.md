# Chapter 3: Introducing Lists

## Introduction

**Key Points**:
- Lists store sets of information in one place
- Can contain few or millions of items
- One of Python's most powerful features
- Accessible to new programmers

## What Is a List?

**Key Points**:
- Collection of items in particular order
- Can contain any type of data
- Items don't need to be related
- Use plural names for lists
- Square brackets `[]` indicate lists
- Elements separated by commas

**Example**:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```

**Output**:
```
['trek', 'cannondale', 'redline', 'specialized']
```

## Accessing Elements in a List

**Key Points**:
- Lists are ordered collections
- Access elements by index position
- Use square brackets with index: `list[index]`
- Can use string methods on list elements

**Basic Access**:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```

**Output**:
```
trek
```

**Using Methods on Elements**:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
```

**Output**:
```
Trek
```

### Index Positions Start at 0, Not 1

**Key Points**:
- First item is at index 0, not 1
- Common source of off-by-one errors
- Subtract 1 from position to get index
- Use negative indices for end of list

**Index Examples**:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])  # Second item
print(bicycles[3])  # Fourth item
```

**Output**:
```
cannondale
specialized
```

**Negative Indices**:
```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])  # Last item
print(bicycles[-2])  # Second from end
```

**Index Rules**:
- `list[0]` - First item
- `list[1]` - Second item
- `list[-1]` - Last item
- `list[-2]` - Second from end

### Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list.

Let's try pulling the first bicycle from the list and composing a message using that value:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
```

We build a sentence using the value at bicycles[0] and assign it to the variable message. The output is a simple sentence about the first bicycle in the list:
```
My first bicycle was a Trek.
```

## Changing, Adding, and Removing Elements

Most lists you create will be dynamic, meaning you'll build a list and then add and remove elements from it as your program runs its course. For example, you might create a game in which a player has to shoot aliens out of the sky. You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. Each time a new alien appears on the screen, you add it to the list. Your list of aliens will increase and decrease in length throughout the course of the game.

### Modifying Elements in a List

The syntax for modifying an element is similar to the syntax for accessing an element in a list. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

For example, let's say we have a list of motorcycles, and the first item in the list is 'honda'. How would we change the value of this first item?

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
```

The code defines the original list, with 'honda' as the first element. The code changes the value of the first item to 'ducati'. The output shows that the first item has indeed been changed, and the rest of the list stays the same:
```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

You can change the value of any item in a list, not just the first item.

### Adding Elements to a List

You might want to add a new element to a list for many reasons. For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you've built. Python provides several ways to add new data to existing lists.

#### Appending Elements to the End of a List

The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list. Using the same list we had in the previous example, we'll add the new element 'ducati' to the end of the list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
```

The append() method adds 'ducati' to the end of the list without affecting any of the other elements in the list:
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

The append() method makes it easy to build lists dynamically. For example, you can start with an empty list and then add items to the list using a series of append() calls:

```python
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
```

The resulting list looks exactly the same as the lists in the previous examples:
```
['honda', 'yamaha', 'suzuki']
```

Building lists this way is very common, because you often won't know the data your users want to store in a program until after the program is running. To put your users in control, start by defining an empty list that will hold the users' values. Then append each new value provided to the list you just created.

#### Inserting Elements into a List

You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```

In this example, the code inserts the value 'ducati' at the beginning of the list. The insert() method opens a space at position 0 and stores the value 'ducati' at that location. This operation shifts every other value in the list one position to the right:
```
['ducati', 'honda', 'yamaha', 'suzuki']
```

### Removing Elements from a List

Often, you'll want to remove an item or a set of items from a list. For example, when a player shoots down an alien from the sky, you'll most likely want to remove it from the list of active aliens. Or when a user decides to cancel their account on a web application you created, you'll want to remove that user from the list of active users. You can remove an item according to its position in the list or according to its value.

#### Removing an Item Using the del Statement

If you know the position of the item you want to remove from a list, you can use the del statement.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
```

The code uses del to remove the first item, 'honda', from the list of motorcycles:
```
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```

You can remove an item from any position in a list using the del statement if you know its index. For example, here's how to remove the second item, 'yamaha', in the list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
```

The second motorcycle is deleted from the list:
```
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
```

In both examples, you can no longer access the value that was removed from the list after the del statement is used.

#### Removing an Item Using the pop() Method

Sometimes you'll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.

The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.

Let's pop a motorcycle from the list of motorcycles:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```

We start by defining and printing the list motorcycles. We pop a value from the list and store that value in the variable popped_motorcycle. We print the list to show that a value has been removed from the list. Then we print the popped value to prove that we still have access to the value that was removed.

The output shows that the value 'suzuki' was removed from the end of the list and is now assigned to the variable popped_motorcycle:
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```

How might this pop() method be useful? Imagine that the motorcycles in the list are stored in chronological order according to when we owned them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought:

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
```

The output is a simple sentence about the most recent motorcycle we owned:
```
The last motorcycle I owned was a Suzuki.
```

#### Popping Items from any Position in a List

You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```

We start by popping the first motorcycle in the list, and then we print a message about that motorcycle. The output is a simple sentence describing the first motorcycle I ever owned:
```
The first motorcycle I owned was a Honda.
```

Remember that each time you use pop(), the item you work with is no longer stored in the list.

If you're unsure whether to use the del statement or the pop() method, here's a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

#### Removing an Item by Value

Sometimes you won't know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method.

For example, let's say we want to remove the value 'ducati' from the list of motorcycles:

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
```

The code tells Python to figure out where 'ducati' appears in the list and remove that element:
```
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

You can also use the remove() method to work with a value that's being removed from a list. Let's remove the value 'ducati' and print a reason for removing it from the list:

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
```

After defining the list, we assign the value 'ducati' to a variable called too_expensive. We then use this variable to tell Python which value to remove from the list. The value 'ducati' has been removed from the list but is still accessible through the variable too_expensive, allowing us to print a statement about why we removed 'ducati' from the list of motorcycles:
```
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.
```

**Note:** The remove() method deletes only the first occurrence of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurrences of the value are removed. You'll learn how to do this in Chapter 7.

## Try It Yourself

Try these short programs to get some firsthand experience with Python's lists. You might want to create a new folder for each chapter's exercises to keep them organized.

1. **Names**: Store the names of a few of your friends in a list called names. Print each person's name by accessing each element in the list, one at a time.
2. **Greetings**: Start with the list you used in Exercise 3-1, but instead of just printing each person's name, print a message to them. The text of each message should be the same, but each message should be personalized with the person's name.
3. **Your Own List**: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle."

The following exercises are a bit more complex than those in Chapter 2, but they give you an opportunity to use lists in all of the ways described.

## Summary

In this chapter you learned what lists are and how to work with the individual items in a list. You learned how to define a list and how to add and remove elements. You learned to sort lists permanently and temporarily for display purposes. You also learned to determine the length of a list and how to avoid index errors when you're working with lists.

In Chapter 4 you'll learn how to work with items in a list more efficiently. By looping through each item in a list using just a few lines of code you'll be able to work efficiently even when your list contains thousands or millions of items.

## Key Takeaways

**List Basics**:
- Lists store collections of items in order
- Use square brackets `[]` to create lists
- Access elements by index: `list[index]`
- Index positions start at 0, not 1
- Use negative indices to access from end

**List Operations**:
- `append()` adds items to end of list
- `insert()` adds items at specific position
- `del` removes items by index
- `pop()` removes and returns item
- `remove()` removes by value

**List Methods**:
- `sort()` sorts list in place
- `sorted()` returns sorted copy
- `reverse()` reverses list order
- `len()` returns list length

**Best Practices**:
- Lists can contain any data type
- Use plural names for list variables 