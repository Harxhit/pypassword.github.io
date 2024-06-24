import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("In today's digital age, a strong password is crucial to protect yourself from cybercriminals.")
print("--------------------------------------Welcome to pypassword generator!!--------------------------------------")

nr_letter = int(input("How many number of letter you would like to be in your password?\n"))
nr_number = int(input(f"How many number of numbers your would like in your password?\n"))
nr_symbols = int(input(f"How many numbers of symbol you would like in your password?\n"))

password_list = []

for char in range( 1 , nr_letter + 1)  :
  password_list.append(random.choice(letters))

for char in range(1 , nr_symbols + 1) : 
  password_list.append(random.choice(symbols))

for char in range(1 , nr_number + 1) : 
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list : 
    password += char

print(f"Your password is : {password}")