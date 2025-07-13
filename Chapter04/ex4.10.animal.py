# Python Crash Course, 2Ed, writtern by Eric Matthes

animals = ['cats', 'dogs', 'lions']

for animal in animals:
    print(f"{animal.title()} have four legs.")

print("Any of them can be a great pet.")

print("\n----")
animals.append('elephant')
print(f"Adding {animals[-1]}.\nNow we have the following animals:")
for animal in animals:
    print(f"{animal.title()}")

print("\n----")
print("Picking up the first three animals:")
for animal in animals[:3]:
    print(f"{animal.title()}")

print("\n----")
animals.append('sharks')
print(f"Adding {animals[-1]}.\nNow we have the following animals:")
for animal in animals:
    print(f"{animal.title()}")

print("\n----")
print("Picking up the middle three animals:")
for animal in animals[(int)(len(animals)/2-1):(int)(len(animals)/2+2)]:
    print(f"{animal.title()}")

print("\n----")
print("Picking up the last three animals:")
for animal in animals[-3:]:
    print(f"{animal.title()}")

