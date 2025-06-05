# Tip Calculator

print("Welcome to Tip calculator :)")
total_bill=int(input("What is the total bill? "))
tip=int(input("How much tip would you like to give 10,12,15? "))
people=int(input("How many people to split the bill? "))

# calculate tip

calc_tip=((total_bill*tip)/100)
total=(calc_tip+total_bill)
print(f"Each person have to pay: ${round(total/people, 2)}")