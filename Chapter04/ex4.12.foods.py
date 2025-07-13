# Python Crash Course, 2Ed, writtern by Eric Matthes

my_foods = ['pizza', 'falafel', 'carrpt cake']
friend_foods = my_foods[:]

print("My favouried foods are :")
for food in my_foods:
    print(f"{food.title()}")

print("My friends's favouried foods are :")
for food in friend_foods:
    print(f"{food.title()}")

print("\n---------")
print("Adding one food for each of mine and friend's list:\n")
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Now, my favouried foods are :")
for food in my_foods:
    print(f"{food.title()}")

print("My friends's favouried foods are :")
for food in friend_foods:
    print(f"{food.title()}")

