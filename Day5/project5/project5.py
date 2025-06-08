# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")
pass_letters=int(input("how many letters would you like in your password? "))
pass_symbols=int(input("How many symbols would you like in your password? "))
pass_numbers=int(input("How many numbers would you like in your password? "))

password=[]
for i in range(1,pass_letters+1):
    ranl = random.choice(letters)
    password.append(ranl)
for s in range(1, pass_symbols + 1):
    rans = random.choice(symbols)
    password.append(rans)
for n in range(1, pass_numbers + 1):
    rann = random.choice(numbers)
    password.append(rann)

random.shuffle(password)
converted_list = map(str, password)
result = ''.join(converted_list)
print(result)

