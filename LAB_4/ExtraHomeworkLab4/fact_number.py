number = int(input("Input a number: "))
factnum = 1
for i in range(1,number+1):
    factnum  *= i

print("Factoriel of %d is %d" % (number,factnum))

