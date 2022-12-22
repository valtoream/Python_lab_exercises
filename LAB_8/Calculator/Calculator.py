import Operations
import sys
try:
    a = int(input("Input a: "))
    b = int(input("Input a: "))
except ValueError:
    print('Type must be int')
    sys.exit(1) 
 

operation = input("+ - / * :")



if operation == '+':
    print(Operations.add(a,b))
elif operation == '-':
    print(Operations.substract(a,b))
elif operation == '/':
    print(Operations.devide(a,b))
elif operation == '*':
    print(Operations.multiplicate(a,b))
else:
    print('Invalid input')

