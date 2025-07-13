# Python Crash Course, 2Ed, writtern by Eric Matthes

pets = []

pet= {
    'type' : 'cat',
    'name' : 'david',
    'owner' : 'lawrence',
    'weight' : 44,
    'food' : "meat"
}
pets.append(pet)

pet= {
    'type' : 'dog',
    'name' : 'alan',
    'owner' : 'steve',
    'weight' : 29,
    'food' : "sausage"
}
pets.append(pet)

pet= {
    'type' : 'parrot',
    'name' : 'baga',
    'owner' : 'sarah',
    'weight' : 3,
    'food' : "peanuts"
}
pets.append(pet)
for pet in pets:
    print(f"{pet['type'].title()}'s names is {pet['name']}, owner is {pet['owner'].title()}.")
    print(f"Weight is {pet['weight']}, and it eats {pet['food']}.")
