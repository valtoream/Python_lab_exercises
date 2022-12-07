"""Exceptions""" 
class InvalidParameterError(Exception):
    def __init__(self,name):
        self.name = name
        
class InvalidAgeError(InvalidParameterError):
    def __init__(self,age):
        self.age = age

class InvalidSoundError(InvalidParameterError):
   def __init__(self,sound):
        self.sound = sound
"""Exceptions""" 


       
        

"""JUNGLE ANIMAL"""   
class JungleAnimal():
    def __init__(self,name,age,sound):
        try:
            self.name = name
            
            if type(name) != str:
                raise InvalidParameterError(name)
        except InvalidParameterError as IP:
            print(f'Invalid parameter:{IP}') 
        
        try:
           self.age = age 
           if type(age) != int:
                raise InvalidAgeError(age)
        except InvalidAgeError as IE:
            print(f'Invalid age error:{IE}') 
            
        
        try:
           self.sound = sound
           if type(sound) != str:
                raise InvalidSoundError(sound)
        except InvalidSoundError as ISE:
            print(f'Invalid sound error:{ISE}')
                
    def make_sound(self):
        print(f'{self.name} says {self.sound}!')
        
    def print(self):
        pass
    def daily_task(self):
        pass
    
"""JUNGLE ANIMAL"""    
    
    






"""Jaguar"""
class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name,age,sound)
        try:
            if age > 15:
                raise InvalidAgeError(age)
        except InvalidAgeError as IE:
            print(f'Invalid age error:{IE}')
       
        try:
            if sound.count("r") < 2:
                raise InvalidSoundError(sound)
        except InvalidSoundError as ISE:
            print(f'Invalid sound error:{ISE}')
            
    def print(self):
        print(f'{__class__.__name__}({self.name},{self.age},{self.sound})')     
    
   
    def daily_task(self,animals):
        # to do
        pass
          
            
"""Jaguar"""




            
"""Lemur"""
class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name,age,sound)
        try:
            if age > 10:
                raise InvalidAgeError(age)
        except InvalidAgeError as IE:
            print(f'Invalid age error:{IE}')
       
        try:
            if not 'e' in sound:
                raise InvalidSoundError(sound)
        except InvalidSoundError as ISE:
            print(f'Invalid sound error:{ISE}')

    def print(self):
        print(f'{__class__.__name__}({self.name},{self.age},{self.sound})')    
    
    def daily_task(self):
        # to do
        pass
"""Lemur"""




"""Human"""
class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name,age,sound)
        try:
            if age > 10:
                raise InvalidAgeError(age)
        except InvalidAgeError as IE:
            print(f'Invalid age error:{IE}')
       
        try:
            if not 'e' in sound:
                raise InvalidSoundError(sound)
        except InvalidSoundError as ISE:
            print(f'Invalid sound error:{ISE}')

    def print(self):
        print(f'{__class__.__name__}({self.name},{self.age},{self.sound})') 

    def daily_task(self):
        # to do
            
        pass
"""Human"""




class Building():
    def __init__(self,type):
        self.type = type
        
        
        
fruits = 100
animals = []
# lem = Lemur('Lemu',5,"Shriek")
# lem1 = Human('Goshko',7,"Eeee")
# lem2 = Human('Pesho',10,"Beeee")
# lem3 = Jaguar('Jaguar1',12,"Grr")
# lem4 = Jaguar('Jaguar2',13,"Grrr")
# lem5 = Lemur('Lamur',7,"Shriek")
# animals.append(lem)
# animals.append(lem1)
# animals.append(lem2)
# animals.append(lem3)
# animals.append(lem4)
# animals.append(lem5)
# print(animals)
# buildings = []
# a = Jaguar('Jaguar3',12,"Grrr")
# a.daily_task(animals)

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]