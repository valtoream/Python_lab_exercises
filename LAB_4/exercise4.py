n = int(input("Input a number"))
dict1={}
list1=[]
for i in range(1,n):
    list1.append(i)

for i in list1:
    dict1[i] = list1[len(list1)-i]

print(list1)
print(dict1)

