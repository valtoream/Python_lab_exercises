def list_avg( lst = [],multiplier=1):
    if type(multiplier ) != int :
        return "Invalid input"
    current = 0
    avg = 0
    if multiplier > 1:
        for i in range(len(lst)):
            if type(lst[i]) == str:
                pass
            else:
                avg += lst[i] * multiplier
                current +=1
        avg_num = avg / current
        return avg_num
    else:
        for i in range(len(lst)):
            if type(lst[i]) == str:
                pass
            else:
                avg += lst[i] 
                current +=1
        avg_num = avg / current
        return avg_num
prob_list = [1,2,"Gosho",4,5]
prob_list2 = [1,2,3,4,5]

print(list_avg(prob_list,1))
print(list_avg(prob_list,2))
print(list_avg(prob_list))

