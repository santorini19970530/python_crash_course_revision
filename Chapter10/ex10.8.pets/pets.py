# Python Crash Course, 2Ed, writtern by Eric Matthes

pet_files = ['cats.txt', 'dogs.txt', 'mice.txt']

def print_pet(filename):
    try:
        with open(filename) as f:
            pet_names = f.read()
    except:
        print(f"There is no {filename}.")
        return None
    else:
        return pet_names
        
for pet_file in pet_files:
    message = print_pet(pet_file)
    if message != None:
        print(message)
