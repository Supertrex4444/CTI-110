#Travis Cayton
#10/17/2024
#P2HW2
#This program will calculate the average of six grades that are entered by the user

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))
print()

grades = [module1,module2,module3,module4,module5,module6]

lowestGrade = min(grades)

highestGrade = max(grades)

gradeSum = module1+module2+module3+module4+module5+module6

average = gradeSum/len(grades)

print(f"{'-'*12}Results{'-'*12}")
print(f"{'Lowest Grade:':<20} {lowestGrade}")
print(f"{'Highest Grade:':<20} {highestGrade}")
print(f"{'Sum of Grades:':<20} {gradeSum}")
print(f"{'Average:':<20} {round(average,2)}")
print(f"{'-'*31}")
