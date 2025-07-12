#### CLASS SETUP ####

### User Class : 
# attributes
# first_name : first name of the user
# last_name : last name of the user
# gender : gender of the user ; 'M' is male, 'F' is female, 'O' is others / transgender
# staff_no : staff ID
# login_attempts : number of trials for login

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

### Admin Class :
# inheritance of user class
# privileges : the abilities of an admin

class admin(users):

    # __init__ : initialize the class
    def __init__(self, first_name, last_name, gender, staff_no):
        super().__init__(first_name, last_name, gender, staff_no)
        self.privileges = privileges()

    # show_privileges : show admin's privileges
    def show_privileges(self):
        self.privileges.show_privileges()

### Privileges Class : 
# privileges : stor the abilities

class privileges():
    
    # __init__ : initialize the class
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    # show_privileges : show admin's privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege.title()}")

### END OF CLASS SETUP ####

sowon = users('sowon', 'kim', 'F', '1234567')
sowon.describe_user()
sowon.greet_user()

print('\n')

pyo = users('pyo', 'pyo', 'O', '23456')
pyo.describe_user()
pyo.greet_user()
for value in range(0,3):
    print(f"\n{pyo.staff_no} login failed:")
    pyo.increment_login_attempts()
print("Finally login successed:")
pyo.reset_login_attempts()

print('\n')
daniel = users('daniel', 'kang', 'M', '2134123')
daniel.describe_user()
daniel.greet_user()

yerin = admin('yerin', 'jung', 'F', '23141234')
yerin.describe_user()
yerin.greet_user()
yerin.show_privileges()
