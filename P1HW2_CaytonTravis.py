# Travis Cayton
# 9/26/2024
# P1HW2

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
budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gasCost = int(input("How much do you think you will spend on gas? "))
print()
hotelCost = int(input("Approximately, how much will you need for accomodation/hotel? "))
print()
foodCost = int(input("Last, how much do you need for food? "))
print()
# Get the total cost of the travel
totalCost = gasCost+hotelCost+foodCost
remainingBalance = budget-totalCost
print()
print("---------Travel Expenses---------")
print()
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gasCost)
print("Accomodation:", hotelCost)
print("Food:", foodCost)
print()
print("Remaining Balance:", remainingBalance)
