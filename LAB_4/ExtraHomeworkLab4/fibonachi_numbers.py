number = int(input("Input a number"))
a,b = 0 ,1
result = []
while a <= number+2:
        result.append(a)
        a,b = b,a+b

print(result)