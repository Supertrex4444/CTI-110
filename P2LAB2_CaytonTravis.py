# Travis Cayton
# 10/10/2024
# P2LAB2
# This program uses a dictionary to store user input and displays output to the user

cars = {"Camaro":18.21,"Prius":52.36,"Model S":110,"Silverado":26};
#Prius = {"rose_color":"purple","price":32.98,"max_height":60,"isPerennial":True};

keys = cars.keys()
print()
print(keys)
print()
selectedCar = input("Enter a vehicle to see it's mpg: ")
print()
print(f"The {selectedCar} gets {cars[selectedCar]} mpg.")
print()
miles = int(input(f"How many miles will you drive the {selectedCar}? "))
print()
gasNeeded = miles / cars[selectedCar]
print(f"{round(gasNeeded,2)} gallon(s) of gas are needed to drive the {selectedCar} {miles} miles.")

