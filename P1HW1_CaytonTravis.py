# Travis Cayton
# 9/26/2024
# P1HW1
# Get input from user and perform math calculations
print()
print("-----Calculating Exponents-----")
print()
print()
#Get info from user
baseValue = int(input("Enter an integer as the base value: "))
exponentValue = int(input("Enter an integer as the exponent: "))
print()
#Calculate the answer
exponentAnswer = int(baseValue ** exponentValue)
print(baseValue, "raised to the power of", exponentValue, "is", exponentAnswer, "!!")
print()
print("-----Addition and Subtraction-----")
print()
print()
startingValue = int(input("Enter a starting integer: "))
additionValue = int(input("Enter an integer to add: "))
subtractionValue = int(input("Enter an integer to subtract: "))
print()
additionAnswer = int(startingValue+additionValue-subtractionValue)
print(startingValue, "+", additionValue, "-", subtractionValue, "is equal to", additionAnswer)
