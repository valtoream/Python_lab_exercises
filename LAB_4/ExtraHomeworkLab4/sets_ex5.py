s1 = {1, 7, 5}
s2 = {1, 2, 3, 4}
# s1 = {2, 3}
# s2 = {1, 2, 3, 4}


if s1.issubset(s2):
    s3= s1.symmetric_difference(s2)
    print(s3)
   
else:
    s4=s1.union(s2)
    print(s4)