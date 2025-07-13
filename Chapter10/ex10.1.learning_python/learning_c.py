# Python Crash Course, 2Ed, writtern by Eric Matthes

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print((line.replace("Python", "C")).rstrip())
