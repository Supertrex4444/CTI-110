# This program is used to simulate a shopping list and display receipt
print()
itemNumber = int(input(f"How many different items are there? (up to 3): "))

if itemNumber > 3:
    itemNumber = 3

itemOneQuantity = 0
itemOnePrice = 0
itemTwoQuantity = 0
itemTwoPrice = 0
itemThreeQuantity = 0
itemThreePrice = 0
print()

if itemNumber >=1:


    itemOne = input("Enter first item: ")
    itemOneQuantity = int(input(f"Enter the quantity of {itemOne}: " ))
    itemOnePrice = int(input(f"Enter the quantity of {itemOne}: " ))
    
    print()
        
if itemNumber >=2:
    
    itemTwo = input("Enter second item: ")
    itemTwoQuantity = int(input(f"Enter the quantity of {itemTwo}: " ))
    itemTwoPrice = float(input(f"Enter the price of the {itemTwo} cost: $"))
    
    print()

if itemNumber >=3:
    itemThree = input("Enter third item: ")
    itemThreeQuantity = int(input(f"Enter the quantity of {itemThree}: " ))
    itemThreePrice = float(input(f"Enter the price of {itemThree} cost: $"))
    
    print()


print("Thanks for shopping!")

print("-"*40)
subtotal = (itemOnePrice*itemOneQuantity)+(itemTwoPrice*itemTwoQuantity)+(itemThreePrice*itemThreeQuantity)
tax = subtotal*0.07
print()
item = "ITEM"
quantity = "QUANTITY"
price = "ITEM TOTAL"


print(f"{item:<20}{quantity:<15}{price:<15}\n")

if itemNumber >=1:
    print(f"{itemOne:<20}{itemOneQuantity:<15}${itemOnePrice:.2f}\n")

if itemNumber >=2:
    print(f"{itemTwo:<20}{itemTwoQuantity:<15}${itemTwoPrice:.2f}\n")
if itemNumber >=3:
    print(f"{itemThree:<20}{itemThreeQuantity:<15}${itemThreePrice:.2f}\n")

print()

print(f"SUBTOTAL: ${subtotal:.2f}\n")

print(f"TAX: ${tax:.2f}\n")

print(f"TOTAL: ${subtotal+tax:.2f}")
#0.07
