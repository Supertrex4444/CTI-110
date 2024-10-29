#Travis Cayton
#10/29/2024
#P3HW2
# This program calculates paycheck based on overtime or no overtime

'''
Input Get employee name from user - string (name)
Input Get number of hours worked - float (hours)
Input Get employee's pay rate (payRate)

Output: print dotted line and employee name

If hours is grater than 40 (employee has overtime)
    variable for hours worked already exists (don't have to create)
    (don't have to create pay rate, it already exists)
    create a variable (overtime) that holds only the overtime hours (hours - 40)
    create a variable for overtimePayRate (payRate * 1.5)
    calculate pay for overtime hours (overtime * (payRate * 1.5))
    calculate regular pay (payRate * 40)
    calculate grossPay (pay for overtimePay + regularPay)
else (NO overtime - hours has to be 40 or less)
    create a variable (overtime) that holds only the overtime hours (WHICH IS ZERO)
    create a variable (overtime) that holds only the overtime hours (WHICH IS ZERO)
    calculate regular pay (payRate * hours)
    Calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("-"*65)
print(f"{hours:<15}{payRate:<10}{overtime:<10}${overtimePay:<15}${regularPay:<15}${grossPay}")
'''

name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
payRate = float(input("Enter employee's pay rate: "))



if hours > 40:
    overtime = hours - 40
    overtimePay = overtime *(payRate * 1.5)
else:
    overtime = 0
    overtimePay = 0

regularPay = (hours - overtime) * payRate

grossPay = regularPay + overtimePay

print("-"*71)

print(f"{'Employee name:':<20} {name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
print("-"*71)
print(f"{hours:<15}{payRate:<10}{overtime:<10}${overtimePay:<15}${regularPay:<15}${grossPay}")
