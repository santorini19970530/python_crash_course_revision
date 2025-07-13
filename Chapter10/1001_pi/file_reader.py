# Python Crash Course, 2Ed, writtern by Eric Matthes

def print_H():
    print("==================")

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

print_H()

file_path = 'd:/CSS.md'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

print_H()

file_path = 'd:/Pandoc.md'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print_H()

filename = 'd:/Markdown.md'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print_H()

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
