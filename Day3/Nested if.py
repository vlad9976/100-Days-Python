# if else elif

h = int(input("What is your height in CM? "))
if h >= 120:
    a = int(input("What is your age? "))
    if a <= 18:
        print("The ticket will cost you 7$")
        print("Pay and Hope on")
    else:
        print("The ticket will cost you 12$")
        print("Pay and Hope on")
else:
    print("Sorry You are under the available height")