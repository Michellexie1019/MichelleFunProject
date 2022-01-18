#=======Tips Calculator - Michelle Yan Xie=======

print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12 or 15?"))
people=int(input("how many people to slit the bill?"))
bill_with_tip=tip/100*bill+bill
bill_per_person=bill_with_tip/people
print(f"Each person should pay ${bill_per_person}")
