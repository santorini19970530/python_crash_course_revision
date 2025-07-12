first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
# this is f-strings (f = format)
# concatenate variables into a string
print(full_name)
print(f"Hello, {full_name.title()}")
message = f"Hello, {full_name.title()}"
print(message)
full_name = "{} von {}".format(first_name, last_name)
print(full_name)
