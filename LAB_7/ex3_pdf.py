import math


    
def read_console_num(num):   
    try:
        num =int(input('Input a number: '))
    
    except TypeError :
        print('Invalid input')
    except ValueError :
      print("Invalid input")
      
    finally:
        print(math.sqrt(num)) 
        print('Goodbye ')
        
       
read_console_num(0)


