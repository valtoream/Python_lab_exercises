import Figures
print('Figures:square,rectangle,rhombus,ratriangle,trapezoid,triangle')
figure = input("Input a figure: ")
if figure == 'square':
    a = float(input('Input the side of a square: '))
    print(Figures.square_area(a))
elif figure == 'rectangle':
    a = float(input("Input the a side of a rectangle:"))
    b = float(input("Input the b side of a rectangle:"))
    print(Figures.rectangle_area(a,b))
elif figure == 'rhombus':
    a = float(input("Input the a side of a rhombus:"))
    h = float(input("Input the h side of a rhombus:"))
    print(Figures.rhombhus_area(a,h))
elif figure == 'ratriangle':
    b = float(input("Input the a side of a ratriangle:"))
    h = float(input("Input the b side of a ratrinangle:"))
    print(Figures.r_a_triangle(b,h))
elif figure == 'trapezoid':
    a = float(input("Input the a side of a trapezoid:"))
    b = float(input("Input the b side of a trapezoid:"))
    h = float(input("Input the h side of a trapezoid:"))
    print(Figures.trapezoid_area(a,b,h))
elif figure == 'triangle':
    a = float(input("Input the a side of a triangle:"))
    ha = float(input("Input the ha side of a triangle:"))
    print(Figures.triangle_area(a,ha))
    