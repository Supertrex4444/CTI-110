# Travis Cayton
#10/17/2024
#P2HW1

"""
Prompt the user to enter their travel budget

Prompt the user to enter their travel destination 

Prompt the user to enter their gas cost

Prompt the user to enter the cost of the hotel 

Prompt the user to enter the cost of food

Preform a calculation and collect the total expenses

Display costs and their travel information
"""

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gasCost = float(input("How much do you think you will spend on gas? "))
print()
hotelCost = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
foodCost = float(input("Last, how much do you need for food? "))
print()

# Get the total cost of the travel
totalCost = gasCost+hotelCost+foodCost
remainingBalance = budget-totalCost
print()
print(f"{'-'*12}Travel Expenses{'-'*12}")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gasCost:,.2f}")
print(f"{'Accomodation:':<20} ${hotelCost:,.2f}")
print(f"{'Food:':<20} ${foodCost:,.2f}")
print(f"{'-'*39}\n")

print(f"{'Remaining Balance:':<20} ${remainingBalance:,.2f}")
