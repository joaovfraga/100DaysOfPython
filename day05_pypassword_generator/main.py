import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nb_letters = int(input("How many letters would you like in your password?\n "))
nb_symbols = int(input("How many symbols would you like?\n "))
nb_numbers = int(input("How many numbers would you like?\n "))

#Eazy Level - Order not randomised: 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for char in range(1, nb_letters + 1):
    ran_char = random.choice(letters)
    password += ran_char

for symbol in range(0, nb_symbols):
    ran_symbol = random.choice(symbols)
    password += ran_symbol

for number in range(0, nb_numbers ):
    ran_number = random.choice(numbers)
    password += ran_number

print(f"Your password is: {password}")


#Hard Level - Order of characters randomised: 4 letter, 2 symbol, 2 number = g^2jk8&P

password_in_list = list(password)
random.shuffle(password_in_list)

final_password = ""
for char in password_in_list:
    final_password += char

print(f"Your password is: {final_password}")