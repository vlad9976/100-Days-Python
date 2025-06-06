# Python pizza prices
# Small pizza: $15
# Medium pizza: $20
# Large Pizza: 25
# add peperoni small pizza: $2
# add peperoni medium large pizza: $3
# Add extra cheese for any pizza: $1
from traceback import print_tb

print("Welcome to python pizza deliveries! :)")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill+=20
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill+=1
elif size == "L":
    bill+=25
    if pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your Total bill is ${bill}")
