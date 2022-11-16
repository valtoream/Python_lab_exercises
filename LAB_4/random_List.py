import random 
s = []
for i in range(10):
    s.append(random.randint(1,200))

print (s)
s1 =[]
for x, y in zip(s, s[1::1]):
    value = x,y,x+y
    s1.append(value)

print(s1)