alien_car = ['green', 'yellow', 'red']
awards = [5, 10, 10]

points = 0

print(f"Now you have {points} points.\n")

guess = input("Guess the car's color (green / yellow / red): ").lower()

if guess in alien_car:
    print("Congratulations: Your guess is correct.\n")
    award = awards[alien_car.index(guess)]
    print(f"You get {award} points!\n")
    points += award
    print(f"Now you have {points} points.")
else:
    print("Wrong guess.")
