# Python Crash Course, 2Ed, writtern by Eric Matthes

# guess_number.py
# system randomally define a number between 1 and 100
# let user guess the number
# if user's guess is out of range, warning will be issued (only three out-of-range guess allowed)
# if user's guess is in the range but not matching the answer, user need to guess again
# if the guess is correct, exit the program

import random

number = random.randint(1, 100)
out_of_range_chance = 3
guessRange = list(range(1, 101))

while True:
    guess = int(input(f"Input an integer between {guessRange[0]} and {guessRange[-1]}: "))
    if (guess > guessRange[-1]) or (guess < guessRange[0]):
        out_of_range_chance = out_of_range_chance - 1
        if out_of_range_chance > 0:
            print("Your guess is out of the range of available gueese. Try again!")
            continue
        else:
            print("There are too many out of range guesses. Get out of the game!")
            break
    elif guess == number:
        print("Congradulations! You have got a correct guess.")
        break
    else:
        if guess > number:
            print("Your guess is too large. Please try again.")
            guessRange = guessRange[:guessRange.index(guess)]
            continue
        else:
            print("Your guess is too small. Please try again.")
            guessRange = guessRange[guessRange.index(guess+1):]
            continue
