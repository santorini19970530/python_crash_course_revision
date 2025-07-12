squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    # or squares.append(value**2)

print(squares)

squares = [value ** 2 for value in range(1, 22)]
print(squares)
