
class User():
    users = []
    def __init__(self,names,EGN):
        self.names = names
        self.EGN = EGN
    def print(self):
        print(f'{self.names}/{self.EGN}')