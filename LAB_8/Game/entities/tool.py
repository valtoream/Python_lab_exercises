class tool():
    def __init__(self,name,durability):
       self.name = name
       self.durability = durability
       
    
class weopon(tool):
    def __init__(self, name, durability,attack):
        super().__init__(name, durability)
        self.attack = attack