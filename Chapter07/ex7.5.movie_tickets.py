customers = []
group = {
    'baby' : 0,
    'child' : 0,
    'adult' : 0
}
unit_price = {
    'baby' : 0,
    'child' : 10,
    'adult' : 15
}
total_customers = 0
total_cost = 0
active = True

# input the ages

while active:
    customer = int(input("Please enter customer's age (input \'0\' to quit): "))
    if customer == 0:
        active = False
    else:
        customers.append(customer)

# divide the customers into groups

if len(customers) == 0:
    print("There is no one watching the movie.")
else:
    for customer in customers:
        if customer < 3:
            group['baby'] += 1
        elif (customer >= 3) and (customer < 12):
            group['child'] += 1
        else:
            group['adult'] += 1
        
    # calculate the cost
    print("\nNumber of customers: ")
    for item, value in group.items():
        total_customers += value
        cost = value * unit_price[item]
        total_cost += cost
        print(f"{item.title()}\t:\t{value} customers\t\tSubtotal: ${cost}")
    print(f"------------\nTotal\t:\t{total_customers} customers\t\tGrand Total: ${total_cost}") 
