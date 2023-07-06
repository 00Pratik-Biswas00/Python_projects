import random
# Database to generate a password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like in your password?\n"))

# password = ""
# for p in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for p in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for p in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

blank_password = []

for l in range(1, nr_letters + 1):
    blank_password.append(random.choice(letters)) # Append function -> To append the data into the list
for l in range(1, nr_symbols + 1):
    blank_password.append(random.choice(symbols)) # Choice function -> To select a random item from a specified sequence
for l in range(1, nr_numbers + 1):
    blank_password.append(random.choice(numbers))

random.shuffle(blank_password) # Shuffle function -> To shuffle the list elements

new_password = ""
for result in blank_password:
    new_password += result # String concatenation

print(f"Your new password is: {new_password}") # F string -> To embed expressions inside string literals, using a minimal syntax
