number_of_stars = int(input("Input number of stars:"))

for i in range (1,number_of_stars + 1):
    for j in range (1,i+1):
        print("*",end="")
    print('')