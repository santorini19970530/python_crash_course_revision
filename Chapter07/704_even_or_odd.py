# Python Crash Course, 2Ed, writtern by Eric Matthes

number = input("Enter a number, and I'll tell you if it's eve or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
