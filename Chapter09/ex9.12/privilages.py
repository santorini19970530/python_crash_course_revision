class privileges():
    
    # __init__ : initialize the class
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    # show_privileges : show admin's privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege.title()}")
