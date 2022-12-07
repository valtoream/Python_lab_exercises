class InvalidParameterError(Exception):
    pass
class NutrientError(Exception):
    pass
class InvalidFoodError(Exception):
    pass
class Food():
    def __init__(self,carbs,protein,fats,salt):
        try:
            self.carbs = carbs
            self.protein = protein
            self.fats = fats
            self.salt = salt
        
            if(type(carbs) != float or type(protein)!=float or type(fats)!= float or type(salt)!= float):
                raise InvalidParameterError
            if carbs + protein + fats + salt > 100.0:
                raise NutrientError
            if carbs == 0 and protein == 0 and fats == 0 and salt == 0:
                raise InvalidFoodError
            
        except InvalidParameterError:
            print("Type must be float")
            
        except NutrientError:
            print("The sum of all the macronutrients must be smaller or equal to 100")
            
        except InvalidFoodError:
            print("All the parameters values must be higher than 0")  
        else:
            self.print_label()   
        

        
    def print_label(self):
        print(f'{__class__.__name__}({self.carbs}/{self.protein}/{self.fats}/{self.salt})')
        
        




for i in range(0,120,10):
    food = Food(float(i),float(i),float(i),float(i))

print("-------")
    
for i in range(0,120,10):
    food1 = Food(i,i,i,i)
    
print("-------")   

food3 = Food(0.0,0.0,0.0,0.0)

    
   




