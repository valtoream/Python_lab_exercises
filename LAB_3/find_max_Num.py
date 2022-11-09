import sys
max = -sys.maxsize -1
length = int(input("Input length: "))
for i in range(length):
    temp = (int(input("Input number: ")))
    if(temp > max):
        max = temp
print("Biggest number: %d " % (max))
