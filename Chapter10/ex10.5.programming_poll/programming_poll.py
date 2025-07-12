filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
    while True:
        name = input("Input your name >> ")
        if (name[:].lower() == 'q') :
            break
        else :
            reason = input(f"{name}, why do you like programming? >> ")
            file_object.write(f"{name} : {reason}\n")

