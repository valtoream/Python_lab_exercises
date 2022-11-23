def operation(typea):
    typea = input("Input operation(+,-,*,/): ")
    
    if typea == '+':
        a = int(input("Input a:"))
        b = int(input("Input b:")) 
        addition(a,b)
    if typea == '-':
        a = int(input("Input a:"))
        b = int(input("Input b:")) 
        substraction(a,b)
    if typea == '*':
        a = int(input("Input a:"))
        b = int(input("Input b:")) 
        multiplication(a,b)
    if typea == '/':
        a = int(input("Input a:"))
        b = int(input("Input b:")) 
        division(a,b)



def addition(a,b):
    
    print("%d + %d = %d" %(a,b,(a +b)) )
    
def substraction(a,b):
    print("%d - %d = %d" %(a,b,(a -b)) )

    
def multiplication(a,b):
    print("%d * %d = %d" %(a,b,(a *b)) )

def division(a,b):
   print("%d / %d = %d" %(a,b,(a /b)) )




operation("")
 



