n = int(input("Input a number: "))
k = n
sum = 0
for i in range(1,n+1):
    print(n,end='+')
    sum+=n
    n = n * 10 + k
    


print("= %d" %(sum))
   
