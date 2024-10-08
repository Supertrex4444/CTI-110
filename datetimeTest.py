#Experimenting with time

import datetime


time = datetime.datetime.now()
month = time.month
month_word = time.strftime("%B")
today = datetime.datetime.today()
weekday = int(today.weekday())
dayofweek = str("")

print("")
print(f"The current date and time is {time}\n")
print(f"The current month is {month}\n")
print(f"The current month is {month_word}\n")

print(f"Today is {today}\n")


if weekday == 0:
    dayofweek = str("Monday")

elif weekday == 1:
    dayofweek = str("Tuesday")
    
elif weekday == 2:
    dayofweek = str("Wednesday")

elif weekday == 3:
    dayofweek = str("Thursday")

elif weekday == 4:
    dayofweek = str("Friday")

elif weekday == 5:
    dayofweek = str("Saturday")

elif weekday == 6:
    dayofweek = str("Sunday")

else:
    dayofweek = str("INVALID")


print(f"The day of the week is {dayofweek}")

