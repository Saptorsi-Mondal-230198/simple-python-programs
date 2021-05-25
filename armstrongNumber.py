number = int(input("Enter a number: "))
sum = 0
num = number
while num>0:
    digit = num % 10
    num //= 10
    sum += digit*digit*digit
if sum == number:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')