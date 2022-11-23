

def sum_list(lst = []):
    sum = 0
    for i in range(len(lst)):
        if type(lst[i]) == str :
            pass
        
        else:
            sum += lst[i]
    return sum


def max_of_two(a,b):
    if type(a) ==str  and type(b) ==str:
        return ""
    if type(a) ==str and type(b) != str :
        return b
    if type(a) !=str and type(b) == str :
        return a
    if a > b or a == b:
        return a
    if b > a:
        return b


print(max_of_two(sum_list([3,4,5,1]),sum_list([15,'b'])))