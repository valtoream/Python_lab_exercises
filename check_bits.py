number = int(input("Enter a number: "))
bit = int(input("Enter a bit: "))
print(number & (1 << bit) > 0 )
