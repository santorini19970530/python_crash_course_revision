alien_car = ['green', 'yellow', 'red']

points = 0

print(f"Now you have {points} points.\n")

guess = input("Guess the car's color (green / yellow / red): ").lower()

if guess in alien_car:
    print("Congratulations: Your guess is correct. You get five points!\n")
    points += 5
    print(f"Now you have {points} points.")
else:
    print("Wrong guess.")
