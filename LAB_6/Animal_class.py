class Animal():
    def __init__(self,name,years,type_of_food):
        if type(name) != str or type(type_of_food) !=str:
            return
        else:
            self.name = name
            self.type_of_food = type_of_food
        if type(years) != int:
            return
        else:
            self.years = years 
                     
    def make_sound(self):
        pass
    def eat_food(self,avaible_food):
        pass

class Cat(Animal):
    def __init__(self, name, years, type_of_food):
        super().__init__(name, years, type_of_food)
        
    def make_sound(self):
        print("Meow")
    def eat_food(self, avaible_food):
        if avaible_food == 0 :
            for meow in range(4):
                Cat.make_sound(self) 
            
            return avaible_food
            
        if avaible_food > 0 and avaible_food <= 10:
            for meow in range(2):
                return 0
            
        if avaible_food > 10:
            avaible_food -=10
            return avaible_food
          
        
            
   


class Dog(Animal):
    def __init__(self, name, years, type_of_food):
        super().__init__(name, years, type_of_food)
        
    def make_sound(self):
        print("Bark")
        
    def eat_food(self, avaible_food,eat_quantity=5):
        
        if eat_quantity > avaible_food:
            return 0
        else:
            avaible_food -= eat_quantity
            return avaible_food
    
class Duck(Animal):
    def __init__(self, name, years, type_of_food):
        super().__init__(name, years, type_of_food)
    def eat_food(self, avaible_food):
        import random
        Duck.make_sound(self)
        avaible_food -= random.randrange(10)
        return avaible_food
            
    def make_sound(self):
        print("Quack")

class Horse(Animal):
    def __init__(self, name, years, type_of_food):
        super().__init__(name, years, type_of_food)
        
    def eat_food(self, avaible_food):
          if avaible_food - 15 < 15:
              avaible_food -=8
              return avaible_food
          else:
              avaible_food -=15
              return avaible_food
              
    def make_sound(self):
        print("Neigh")
    
        
        
cat = Cat("Mecho",10,"fish")
cat2 = Cat("Tom",2,"fish")
horse1 = Horse("Vihur",5,"hay")
dog1 = Dog("Buddy",2,"dog_food")
dog2 = Dog("Chichi",5,"dog_food")
cat3= Cat("Aurora",7,"fish")
duck = Duck("Bin",3,"frog")
horse2 = Horse("Vihur2",5,"hay")
dog3 = Dog("Buddy2",2,"dog food")
dog4 = Dog("Rit",5,"dog food")
animals = [cat,cat2,cat3,horse1,horse2,dog1,dog2,dog3,dog4,duck]
food = {"fish":200,"dog_food":100,"frog":20,"hay":50}

