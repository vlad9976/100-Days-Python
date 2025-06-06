h = int(input("What is your height in CM? "))
bill = 0

if h >= 120:
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket will cost you $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket will cost you $7")
    elif 45 <= age <= 55:
        bill = 0
        print("Seniors Aged 45-55 ticket costs Free Ride")
    else:
        bill = 12
        print("Adult ticket costs $12")

    wants_photo = input("Do you want to have a photo taken (Extra $3)? y for Yes n for No: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill ${bill}")
else:
    print("Sorry You are under the available height")
