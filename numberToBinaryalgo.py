number = int(input("Input a number: "))
binaryNum = ""


while number != 0:
    binaryNum +=str(number%2)
    number //=2

print(binaryNum[::-1])

