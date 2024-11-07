#Travis Cayton
#11/7/2024
#P4LAB2
#For loop a base value a 12 times and multiply it each time

loopCount = 0
loop = True
validAnswer = True

while loop == True:
    print()
    baseValue = int(input("Enter an integer: "))
    print()
    if baseValue >=0:
        for loopCount in range(1,13):
            print(f"{baseValue} * {loopCount} = {baseValue * loopCount}")
    else:
        print("This program does not handle negative numbers")
    print()
    answer = input("Would you like to run the program again? (y/n) ")
    if answer == "y":
        loop = True
        
    elif answer == "n":
        loop = False

    else:
        validAnswer = False

    while validAnswer == False:
        print()
        print("INVALID ANSWER, TRY AGAIN")
        print()
        answer = input("Would you like to run the program again? (y/n) ")
        if answer == "y":
            loop = True
            validAnswer = True
        elif answer == "n":
            loop = False
            validAnswer = True
        else:
            validAnswer = False
            
print()
print("Exiting program...")

