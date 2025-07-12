# class number : simulate the number and include a count attribute of being selected

class number():

    # _init_ : initialize class
    def __init__(self, assigned_no, count = 0):
        self.assigned_no = assigned_no
        self.count = count

    # get_count : return the number of being selected
    def get_coun(self):
        return self.count
    
    # show_number : show the number and its properties
    def show_number(self):
        print(f"This number is {self.assigned_no}. This is being selected for {self.count} time.")
        
