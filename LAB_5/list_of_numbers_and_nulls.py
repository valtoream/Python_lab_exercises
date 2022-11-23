def change_list(lst = [],number = 1):
    for i in range(len(lst)):
        if lst[i] > number:
            lst[i] = 0
    return(lst)
listt = [10,30,5,7,3]
listt2 = [2,3,4,5,7,8,10]

print(listt)
print(change_list(listt,7))
print(listt2)
print(change_list(listt2,4))


