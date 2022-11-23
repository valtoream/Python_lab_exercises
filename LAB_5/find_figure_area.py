def area_of_geo_shapes(typea= input("Input shape(square/rectangle/triangle):")):
    
    if(typea == 'square'):
        print("Area of square = %d" % (square_area()))
    if(typea == 'rectangle'):
        print("Area of rectangle = %d" % rectangle_area())
    if(typea == 'triangle'):
        print("Area of right angled trinagle = %.2f " % r_a_triangle())
        
        


def square_area():
    a=int(input("Input value of a:"))
    return(a*a)

def rectangle_area():
    a=int(input("Input value of a:"))
    b=int(input("Input value of b:"))
    return (a*b)

def r_a_triangle():
    b=float(input("Input value of b:"))
    h=int(input("Input value of h:"))
    return ( (b * h ) /2)



area_of_geo_shapes()




