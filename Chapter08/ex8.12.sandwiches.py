def order_sandwich(*ingridents):
    print("Your order is:")
    for ingrident in ingridents:
        print(f"{ingrident.title()}")

order_sandwich('subway series', 'classic sandwiches')
order_sandwich('wraps', 'fresh melts')
order_sandwich('breakfast')
