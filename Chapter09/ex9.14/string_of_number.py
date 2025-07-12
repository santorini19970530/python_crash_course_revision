### class String_of_number :  simulates a string of seven numbers ###

class String_of_number():
    
    # _init_ : initialize the class
    def __init__(self, numbers = [0,0,0,0,0,0,0], win = 0)
        self.numbers = numbers[:]

    # add_win : add the number of wins
    def set_win(self, add_no):
        self.win += add_no

    # show_numbers ; show the numbers in the string
    def show_numbers(self):
        print("This string include the following numbers:")
        for number in self.numbers:
            print(list, sep = ", ")

    # show_win : show the numbers of won
    def show_win(self)
        print(f"This string has the number of wins : {self.win}.")
