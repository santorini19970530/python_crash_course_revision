# Python Crash Course, 2Ed, writtern by Eric Matthes

def make_shirt(size = 'M', message = 'Wie heißen Sie?'):
    print(f"We will make {size} T-shirt with a slogen of \"{message}.\"\n")

make_shirt()

make_shirt('S')

# make_shirt(, 'Ich heiße hihi.')
# cannot empty the first argument.

make_shirt(message = 'Und Sie?', size = 'L')

make_shirt('XL', 'Ich heiße Stefan.')
