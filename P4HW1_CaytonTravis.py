#Travis Cayton
#11/8/2024
#P4HW1

'''
Ask the user for the amount of scores they want to enter, then store it in a variable called "scoreAmount"

For loop over "scoreAmount" and collect a score from the user each time, it will be stored in a variable called "score"

Check if the "score" they entered was invalid and if it is then the user will enter a while loop that displays "INVALID Score entered!!!!" followed by "Score should be between 0 and 100:

Have the user enter a score again and check if its valid this time

Append the current value for "score" into a list called "scoreList"

Repeat until for loop is complete

Calculate the average of "scoreList"

Display the Lowest Score, "scoreList" after removing the lowest score, the average, and lastly a letter grade that is determined by the average

'''

scoreList = []

invalidScore = False

scoreAmount = int(input("How many scores do you want to enter? "))


for i in range(scoreAmount):
    score = int(input(f"Enter score #{i+1}: "))
    if score < 0 or score > 100:
        invalidScore = True
        while invalidScore == True:
            print()
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            score = int(input(f"Enter score #{i+1} again: "))
            if score >= 0 and score <= 100:
                invalidScore = False
            
    scoreList.append(score)



print()
print(f"{'-'*15}Results{'-'*15}")
print(f"{'Lowest Score':<15}  : {min(scoreList)}")
scoreList.remove(min(scoreList))
average = sum(scoreList)/len(scoreList)
print(f"{'Modified List':<15}  : {scoreList}")
print(f"{'Scores Average':<15}  : {average}")

# Determine letter grade based off the average

if average > 100:
    myGrade = "A+, Nice!" 

elif average >= 90:
    myGrade = "A"    

elif average >= 80:
    myGrade = "B"    

elif average >= 70:
    myGrade = "C"

elif average >= 60:
    myGrade = "D"
    
elif average < 60:
    myGrade = "F"   

print(f"{'Grade:':<15}  : {myGrade}")
print(f"{'-'*22}{'-'*15}")
