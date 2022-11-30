class Vehicle():
    def __init__(self,brand,model,engine_vol,max_speed,total_km,max_passangers):
        if type(brand) != str or type(model) != str:
            return 
        else:
            self.brand = brand
            self.model = model
        if type(engine_vol) != float or type(max_speed) !=float or type(total_km) != float:
            return 
        else:
            self.engine_vol = engine_vol
            self.max_speed = max_speed 
            self.total_km = total_km
        if type(max_passangers) != int:
            return
        else:
            self.max_passangers = max_passangers
    def print_info(self):
        print(f"{__class__.__name__}({self.brand},{self.model},{self.engine_vol},{self.max_speed},{self.total_km},{self.max_passangers})")
        
class Motorbike(Vehicle):
    def __init__(self,brand,model,engine_vol,max_speed,total_km,price,has_a_basket):
        super().__init__(brand, model,engine_vol,max_speed,total_km,2)
        if type(price) != float:
            return
        else:
            self.price = price
        if type(has_a_basket) != bool:
            return
        else:
            self.has_a_basket = has_a_basket
    def print_info(self):
        print(f"{__class__.__name__}({self.brand},{self.model},{self.engine_vol},{self.max_speed},{self.max_passangers},{self.total_km},{self.price},{self.has_a_basket})")
        
        
        
class Car(Vehicle):
    def __init__(self,brand,model,engine_vol,max_speed,total_km,category,type_fuel):
        super().__init__(brand, model,engine_vol,max_speed,total_km,4)
        if type(category) != str:
            return
        else:
            self.category = category
        if type(type_fuel) != str:
            return
        else:
            self.type_fuel = type_fuel
    def print_info(self):
        print(f"{__class__.__name__}({self.brand},{self.model},{self.engine_vol},{self.max_speed},{self.max_passangers},{self.total_km},{self.category},{self.type_fuel})")
        
        
        
class Bus(Vehicle):
       def __init__(self,brand,model,engine_vol,max_speed,total_km,max_passangers,company,year_of_creation):
            super().__init__(brand, model,engine_vol,max_speed,total_km,max_passangers)
            if type(company) !=str:
                return
            else:
                self.company = company
            if type(year_of_creation) != int:
                return
            else:
                self.year_of_creation = year_of_creation
       def print_info(self):
            print(f"{__class__.__name__}({self.brand},{self.model},{self.engine_vol},{self.max_speed},{self.total_km},{self.max_passangers},{self.company},{self.year_of_creation})")

vehicles = []
vehicle1 = Vehicle("Opel","Astra",1.6,240.0,140.0,5)
car1 = Car("Audi","a4",2.0,220.0,230.000,"B","Diesel")
car2 = Car("Opel","Corsa",1.4,160.0,230.000,"B","Propane butane")
car3 = Car("Golf","4",2.0,280.0,270.000,"B","Diesel")
car4 = Car("CarType","Type",4.0,300.0,200.00,"B","Diesel")
motorbike1 = Motorbike("HONDA","XL700V ",500.0,330.0,100.000,550.000,False)
bus1 = Bus("Mercedes","Benz",120.0,160.000,140.00,40,"Mercedes",2020)
vehicles.append(car1)
vehicles.append(car2)
vehicles.append(car3)
vehicles.append(car4)
vehicles.append(motorbike1)
vehicles.append(bus1)
vehicles.append(vehicle1)
print(vehicles)
vehicle1.print_info()
bus1.print_info()
car2.print_info()
motorbike1.print_info()



