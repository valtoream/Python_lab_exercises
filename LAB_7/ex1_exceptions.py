
#KeyError example-Извикваме ключ,който не съществува в речника
cats = {'Princess':1,'Goshko':2}
try:
   print(cats['Ivancho'])  
except KeyError:
    print("Key doesnt exist")
    
# AtrributeError-При извикване на атрибут,който даден обект не съдържа
class Cats():
    def __init__(self,name,age):
        self.name = name
        self.age = age

cat = Cats('Gosho',12)

try:
    print(cat.color)
except AttributeError:
    print('Cat has no such attribute')
    
# ValueError-Когато е зададен правилен аргумент,но неправилна стойност

import math
num = -10

try:
    math.sqrt(num)
except ValueError:
    print('Number must be positive')
    
    
#NameError-Когато глобалното или локалното име не се намира
def sum_of_two(x,y):
    result = x + y
    return(result)
try:
    ss = sum_of_tw(5,10)
    print(ss)
except NameError:
    print('Names of methods dont match')
    
    
#TypeError-Опитваме се да добавим число към лист
def sum_of_two(num1,num2):
    result = num1 + num2
    return(result)
try:
    ss = sum_of_two(1,[2,3,4])
    print(ss)
except TypeError:
    print('Types dont match')
    
    
#IndexError-При извикване на индекс,който не съществува 
num_list = [1,3,4,123,1] 
try:
    print(num_list[5])
except IndexError:
    print('Index doesnt exist')


# ModuleNotFoundError-При извикване на модул,който не е достъпен
try:
    import numpy as np
except ModuleNotFoundError:
    print("Module isnt located")  


# ZeroDevisionError-При делене на 0
try:
    print(10/0)
except ZeroDivisionError:
    print("Cant devide to 0")

 
        
# RuntimeError-Грешка която се изпълнява по време на изпълнение на програмата
# Пример за това са  примерите за ZeroDevisionError и IndexError в този файл

 
#FileNotFoundError
try:
    fo = open("myfile.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")   
    
# OSError
import os
try:
    os.close(50)
except OSError:
    print("OSError")