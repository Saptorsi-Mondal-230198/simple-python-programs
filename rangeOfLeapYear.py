startYear = int(input("Enter the starting year: "))
endYear = int(input("Enter the ending year: "))
counter = 0
for i in range(startYear, endYear+1):
    if (i % 400 == 0) or (i % 4 == 0) and i % 100 != 0:
        counter +=1
        print(i, ' is a Leap year')
    else:
        print(i, ' is not a Leap Year')
print('The total number of leap years between the range', startYear, ' and ', endYear, ' is ', counter)