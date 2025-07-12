def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words =  contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = '1005_alice/alice.txt'
count_words(filename)

print("===============")

filenames = ['1005_alice/alice.txt', '1003_programming/programming.txt', '1001_pi/pi_digits.txt']
for filename in filenames:
    count_words(filename)

