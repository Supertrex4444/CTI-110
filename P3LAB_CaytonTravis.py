#Travis Cayton
#10/24/2024
#P3LAB
#This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money

change = float(input("Enter the amount of money as a float: $"))

if change <= 0:
    print("No Change")

change = int(change * 100)

#Get Dollars needed
numDollars = change // 100
change = change - (numDollars * 100)

if numDollars > 0:
    if numDollars == 1:
        print(f"{numDollars} Dollar")
    else:
        print(f"{numDollars} Dollars")

#Get Quarters needed
numQuarters = change // 25
change = change - (numQuarters * 25)

if numQuarters > 0:
    if numQuarters == 1:
        print(f"{numQuarters} Quarter")
    else:
        print(f"{numQuarters} Quarters")

#Get Dimes needed
numDimes = change // 10
change = change - (numDimes * 10)

if numDimes > 0:
    if numDimes == 1:
        print(f"{numDimes} Dime")
    else:
        print(f"{numDimes} Dimes")

#Get Nickels needed
numNickels = change // 5
change = change - (numNickels * 5)

if numNickels > 0:
    if numNickels == 1:
        print(f"{numNickels} Nickel")
    else:
        print(f"{numNickels} Nickels")

#Get Pennies needed
numPennies = change // 1
change = change - (numPennies * 1)

if numPennies > 0:
    if numPennies == 1:
        print(f"{numPennies} Penny")
    else:
        print(f"{numPennies} Pennies")
        
