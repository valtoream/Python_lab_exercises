listSize =int( input("Input size of the list: "))
example_List=[]
for i in range(listSize):
    i = int(input("Input numbers in the list: ")) 
    example_List.append(i)
    
print("Example list before additions",example_List)

zero_or_one = int(input("Input 0 or 1:"))
if zero_or_one == 0:
    for i in range(len(example_List)):
        if example_List[i] % 2 == 0:
            example_List[i] +=5
elif zero_or_one == 1:
    for i in range(len(example_List)):
        if example_List[i] %2 !=0:
            example_List[i] +=10
print("Example list after additions",example_List)

