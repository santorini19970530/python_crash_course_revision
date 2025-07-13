# Python Crash Course, 2Ed, writtern by Eric Matthes

from users import *
from privilages import *

class admin(users):

    # __init__ : initialize the class
    def __init__(self, first_name, last_name, gender, staff_no):
        super().__init__(first_name, last_name, gender, staff_no)
        self.privileges = privileges()

    # show_privileges : show admin's privileges
    def show_privileges(self):
        self.privileges.show_privileges()
