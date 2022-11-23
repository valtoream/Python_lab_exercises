
def get_collection_builder(col_type):
    if type(col_type) != str:
        return "Invalid input"
    if col_type == "set":
        def set_builder(a,b,c,d):
            set1 = set ([])
            a = (input("Input a set value:"))
            set1.add(a)
            b = input("Input a set value:")
            set1.add(b)
            c = input("Input a set value:")
            set1.add(c)
            d = input("Input a set value:")
            set1.add(d)
            return set1 
        return (set_builder(1,1,1,1))  
        
    if col_type == "tuple":
        def tuple_builder(a,b,c,d):
            
            return (a,b,c,d)
        a = input("Input a tuple value:")
        b = input("Input a tuple value:")
        c = input("Input a tuple value:")
        d = input("Input a tuple value:")
       
        return ((tuple_builder(a,b,c,d)))
    if col_type == "list":
     def list_builder(a,b,c,d):
        lst = []
        a = input("Input a list value:")
        lst.append(a)
        b = input("Input a list value:")
        lst.append(b)
        c = input("Input a list value:")
        lst.append(c)
        d = input("Input a list value:")
        lst.append(d)
        return lst
       
     return ((list_builder(1,1,1,1)))
   
    # change to list/tuple/set
a = get_collection_builder("tuple")
print(a)