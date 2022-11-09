n = int(input("Imput how many numbers you would like to enter: "))

sum = 0
for i in range (n):
    entered_numbers = int(input("Enter a number: "))
    sum += entered_numbers

print("Sum of all numbers is %d " % (sum))
