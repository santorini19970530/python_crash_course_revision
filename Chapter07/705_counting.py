# Python Crash Course, 2Ed, writtern by Eric Matthes

def print_H()
    print("--------------")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print_H()

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

print_H()

x = 1
while x <= 5:
    print(x)
    x += 1
