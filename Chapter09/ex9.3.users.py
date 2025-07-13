# Python Crash Course, 2Ed, writtern by Eric Matthes

class users:
    def __init__(self, first_name, last_name, gender, staff_no):
        self.first_name = first_name
        self.last_name = last_name
        self.title = 'staff'
        self.gender = gender
        self.staff_no = staff_no

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
        print(f"Title: {self.title.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()} !!!")

sowon = users('sowon', 'kim', 'F', '1234567')
sowon.describe_user()
sowon.greet_user()

pyo = users('pyo', 'pyo', 'O', '23456')
pyo.describe_user()
pyo.greet_user()

daniel = users('daniel', 'kang', 'M', '2134123')
daniel.describe_user()
daniel.greet_user()
