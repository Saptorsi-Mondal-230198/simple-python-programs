"""
TODO: TO TAKE LIST OF NUMBERS INPUT FROM USER, i.e., TO TAKE LIST
      OR ARRAY VALUES FROM USER.
"""
listOfNumbers = []

length = int(input("How many numbers you want to enter in the list: "))
for i in range(length):
    number = int(input(f'Enter number {i+1}: '))
    listOfNumbers.append(number)

print(f'Displaying the List: {listOfNumbers}')
