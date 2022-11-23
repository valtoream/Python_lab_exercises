def is_valid_triangle(a,b,c):
    if a > 0 and b > 0 and c > 0 and type(a) == int and type(b) == int and type(c) == int and (a + b > c and a + c > b and b + c > a ): 
         return True
    else:
        return False
            
    

def can_triangle_exist(a,b,c):
    return is_valid_triangle(a,b,c)

print(can_triangle_exist(1.1,1,1))
print(can_triangle_exist(0,1,1))
print(can_triangle_exist(1,1,1))
