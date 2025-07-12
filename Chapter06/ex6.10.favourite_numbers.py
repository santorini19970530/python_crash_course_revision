favourite_numbers = {
    'sowon' : [1, 3, 4, 8],
    'yerin' : [2, 6, 9],
    'eunha' : [3, 7, 11],
    'yuju' : [4, 112, 1100],
    'sinb' : [5, 6, 7],
    'umji' : [1, 6]
}

for person, numbers in favourite_numbers.items():
    print(f"{person.title()}'s favourite numbers are:")
    for number in numbers:
        print(number)
