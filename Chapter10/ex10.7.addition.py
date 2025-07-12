while True:
    x = input("Enter the first number (or enter \'q\' to quit) >> ")
    if x.lower() == 'q':
        break
    y = input("Enter the second number (or enter\'q\' to quit) >> ")
    if y.lower() == 'q':
        break

    try:
        int(x)
        int(y)
    except ValueError:
        print("One of the numbers are not integers.\nTry again.")
    else:
        print(f"{int(x)} + {int(y)} = {int(x) + int(y)}")
