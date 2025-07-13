# Python Crash Course, 2Ed, writtern by Eric Matthes

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Input your name >> ")
        if (name[:].lower() == 'q') :
            break
        else :
            file_object.write(f"{name}\n")

