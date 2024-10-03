#import math
import math
import random

#Pythagorean Theorem

#Generate random values for side1 & side2
side1 = random.randint(1,100)

side2 = random.randint(1,10)
'''
#Get value of sides from the user
side1 = float(input("Enter the value for side one: "))

side2 = float(input("Enter the value for side two: "))
'''

#Calculate the Hypotenuse
hypotenuse = (side1**2)+(side2**2)

#Display the results to the user
print(f"The hypotenuse of a right triangle with the sides {side1} and {side2} is {math.sqrt(hypotenuse)}")

