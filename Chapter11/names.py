# Python Crash Course, 2Ed, writtern by Eric Matthes

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Plesae give me a last name: ")
    if last == 'q':
        break

    formatter_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatter_name}.")
