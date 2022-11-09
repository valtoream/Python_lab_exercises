import sys
# num = 27102022
# devisor =2
# # binary
# result = ""

# while num  > 0:
#     result +=str(num %2)
#     num //=2
# if num >=0:
#     print(result[::-1])


# max = -sys.maxsize -1
# number = []
# length = int(input("Input length: "))
# for i in range(length):
#     number.append(int(input("Input number: ")))
#     if(number[i] > max):
#         max = number[i]        
# print("Biggest number: %d " % (max))



# max = -sys.maxsize -1
# length = int(input("Input length: "))
# for i in range(length):
#     temp = (int(input("Input number: ")))
#     if(temp > max):
#         max = temp
# print("Biggest number: %d " % (max))


# number = int(input("Input number: "))
# for i in range(0,10):
#     print("%d * %d = %d " % (number,i,number*i))



number = str(input("Input number: "))
arr = []
for i in range(len(number)):
    arr.append(number[i])

number2 = str(input("Enter number 2: "))
new_array = []
converted = ""
sum = 0
for i in range(len(number)):
    new_array.append(arr[int(number2[i])-1])
    converted +=new_array[i]
    sum +=int(new_array[i])
    
print(converted)
print(sum)





    

