import math
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

discriminant = b*b - 4*a*c
ansPositive = (-b + math.sqrt(discriminant))/(2*a)
ansNegative = (-b - math.sqrt(discriminant))/(2*a)
print('The roots are: ', ansPositive,' ', ansNegative)