from random import randint

class Dice():
### attributes ###
# sides : no. of sides of the dice
    
    # _init_ : initialize the dice class
    def __init__(self, sides = 6):
        self.sides = sides

    # draw_dice : draw a dice, and then give out an result (integer)
    def roll_dice(self):
        return randint(1, self.sides)

    # show_dice : tell user how many sides this dice has
    def show_dice(self):
        print(f"This dice has {self.sides} sides.\n")

### End of class ###

dice1 = Dice();
dice1.show_dice();
for i in range(1,11):
    print(f"Draw # {i} : {dice1.roll_dice()}")

print("\n---\n")
dice2 = Dice(10)
dice2.show_dice();
for i in range(1,11):
    print(f"Draw # {i} : {dice2.roll_dice()}")

print("\n---\n")
dice3 = Dice(20)
dice3.show_dice();
for i in range(1,11):
    print(f"Draw # {i} : {dice3.roll_dice()}")

