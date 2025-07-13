# Python Crash Course, 2Ed, writtern by Eric Matthes

class users:

    # __init__ : initialize the class
    def __init__(self, first_name, last_name, gender, staff_no):
        self.first_name = first_name
        self.last_name = last_name
        self.title = 'staff'
        self.gender = gender
        self.staff_no = staff_no
        self.login_attempts = 0

    # describe_user : show descriptions of the user
    def describe_user(self):
        print("Staff Profile:\n-------")
        print(f"Name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Staff ID: {self.staff_no}")
        if self.gender == 'M':
            print("Gender: Male")
        elif self.gender == 'F':
            print("Gender: Female")
        elif self.gender == 'O':
            print("Gender: Other")
        print(f"Title: {self.title.title()}\n------")
    
    # greet_user : greet to user after login success
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} !!!")

    # increment_login_attempts : increase number of attempts by 1 for each failed login trials
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Now {self.staff_no}'s login attempt number is {self.login_attempts}.")

    # reset_login_attempts : set the login attempts to zero
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Now {self.staff_no}'s login attempt number is {self.login_attempts}.")

