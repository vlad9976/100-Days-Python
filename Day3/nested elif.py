# if else elif

h = int(input("What is your height in CM? "))
bill = 0

if h >= 120:
    a = int(input("What is your age? "))
    if a <= 12: # age less or equal to 12
        bill = 5
        print("Child ticket will cost you $5")
    elif a <= 18: # Check age between 13-18
        bill = 7
        print("Youth ticket will cost you $7")
        print("Pay and Hope on")
    else: # All the rest
        bill = 12
        print("Adult ticket will cost you $12")
        print("Pay and Hope on")
    wants_photo = input("Do you want to have a photo taken? y for Yes n for No: ")
    if wants_photo == "y":
        # add 3 dollars to bill
        bill += 3
    print(f"Your final bill ${bill}")
else:
    print("Sorry You are under the available height")