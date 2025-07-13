# Python Crash Course, 2Ed, writtern by Eric Matthes

def addition (num1 , num2):
    return num1 + num2

def get_input():
    num = input("Enter the number >> ")
    try:
        int(num)
    except ValueError:
        print("The input is not digit.\nPlease try again.")
        return None
    else:
        return int(num)

print("The first number:")
x = get_input()
print("The second number:")
y = get_input()

if (x and y) != False :
    print(f"{x} + {y} = {x + y}")
