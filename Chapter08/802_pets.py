def describe_pet (animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')

describe_pet(animal_type = 'cat', pet_name = 'happy')

def describe_pet_a (pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"\nMy {animal_type}'s name is {pet_name.title()}.")

# below funciton calling methods are valid
describe_pet_a(pet_name = 'silly')
describe_pet_a(pet_name = 'hihi', animal_type = 'cat')
describe_pet_a('willie')
describe_pet_a('harry', 'willie')
describe_pet_a(pet_name = 'harry', animal_type = 'hamster')
describe_pet_a(animal_type = 'hamster', pet_name = 'harry')
