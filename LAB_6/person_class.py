class Person():
    def __init__(self,name,family,age,nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
        
    def print_person(self):
        print(f"Name:{self.name}, Family:{self.family}, Age:{self.age}, Nationality:{self.nationality}")
        
class Student(Person):
 def __init__(self, name, family, age,nationality,university,year_of_study):
        super().__init__(name, family,age,nationality)
        self.university = university
        self.year_of_study = year_of_study
 def print_person(self):
        print(f"Name:{self.name},Family:{self.family}, Age:{self.age},"
              f"Nationality:{self.nationality},University:{self.university},Year of study:{self.year_of_study}")
        
    
        
class Lecturer(Person):
     def __init__(self,name,family,age,nationality,university,experience):
         super().__init__(name, family,age,nationality)
         self.university = university
         self.experience = experience
     def print_person(self):     
        print(f"Name:{self.name},Family:{self.family}, Age:{self.age}, Nationality:{self.nationality},"
              f"University:{self.university},Years of experience:{self.experience}")
        
Gosho = Person('Gosho',"Goshev",23,"bulgarian")
Gosho.print_person()
print()
Pesho = Student('Goshev','Ivanov',23,'bulgarian','TU',3)
Pesho.print_person()
print()
Georgi = Lecturer('Georgi','Petkov',30,'bulgaria','TU',20)
Georgi.print_person()
