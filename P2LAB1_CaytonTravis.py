# Travis Cayton
# 10/08/2024
# P2LAB1
# This program will calculate the diameter, circumference, and area of a circle.

import math

print("")

print(f"The value of pi is {math.pi}\n")

radius = float(input("What is the radius of the circle? "))

print("")

diameter = 2 * radius

circumference = 2 * (math.pi) * radius

area = (math.pi) * math.pow(radius,2)

print(f"The diameter of the circle is {round(diameter,2)}\n")

print(f"The circumference of the circle is {round(circumference,2)}\n")

print(f"The area of the circle is {round(area,3)}")

#(math.pi)
