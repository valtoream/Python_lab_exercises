def digitize(num):
    if type(num) != int:
        return "Incorrect input"
    list1 = list(str(num))
    list1 = tuple(list1)
    return (list1)
    
a,b,c,d = digitize(1202)
print(digitize(204020))
print(a,b,c,d)
