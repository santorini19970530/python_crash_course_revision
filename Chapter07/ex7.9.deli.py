sandwich_orders = ['hamburger', 'club sandwich', 'doner sandwich', 'chicken breast sandwich', 'porilainen', 'pastrami a', 'pastrami b', 'pastrami c']
finished_orders = []

def make_sandwich(sandwich):
    print(f"I make your {sandwich.title()}.")

def finished_sandwich(sandwich):
    print(f"{sandwich.title()} has been finished.")

def no_pastrami(sandwich):
    print(f"Sorry, there is no pastrami, so {sandwich.title()} will be skipped.")

print("Sorry, there is no pastrami available now.\n")
print("Sandwich orders:")
for sandwich in sandwich_orders:
    print(f"{sandwich.title()}")
print("\n------\n")

while len(sandwich_orders) != 0:
    processing = sandwich_orders.pop(0)
    make_sandwich(processing)
    if 'pastrami' in processing:
        no_pastrami(processing)
        continue
    finished_orders.append(processing)
    finished_sandwich(processing)

print("\n-------\nFinished sandwich orders:")
for sandwich in finished_orders:
    print(f"{sandwich.title()}")
