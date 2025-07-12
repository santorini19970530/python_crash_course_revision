def print_H():
    print("========================")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print_H()

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide bu 0!")
    else:
        print(answer)

