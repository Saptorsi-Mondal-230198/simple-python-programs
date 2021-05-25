# TODO: TO FIND THE DAY OF ANY YEAR BASED ON THE GIVEN INPUTS
import calendar

year = int(input("Enter the Year: "))
month = int(input("Enter the month between 1 - 12: "))
days = int(input("Enter the day: "))

# calendar.weekday(year, month, day)
# Returns the day of the week (0 is Monday) for year (1970–…), month (1–12), day (1–31).
day = calendar.weekday(year, month, days)
if day == 0:
    print("Day : Monday")
elif day == 1:
    print("Day : Tuesday")
elif day == 2:
    print("Day : Wednesday")
elif day == 3:
    print("Day : Thursday")
elif day == 4:
    print("Day : Friday")
elif day == 5:
    print("Day : Saturday")
elif day == 6:
    print("Day : Sunday")
else:
    print("Invalid")
