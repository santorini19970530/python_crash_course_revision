import json

filename = 'data.json'

while True:
    str = input("Input your favourite number >> ")
    try:
        fav_num = int(str)
    except ValueError:
        print("You have not input integer.\nPlease enter again.")
        continue;
    else:
        print("Your favourite number has been recorded.")
        break

with open(filename, 'w') as f:
    json.dump(fav_num, f)
