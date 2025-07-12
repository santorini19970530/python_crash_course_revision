filename = 'guest.txt'

with open(filename, 'w') as file_object:
    name = input("Input your name >> ")
    file_object.write(name)

