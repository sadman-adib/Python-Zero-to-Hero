class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...") 

class ToyotaCar(car): # inheritance
    def __init__(self, brand):
        self.brand = brand

class Prado(ToyotaCar): # multi level inheritance
    def __init__(self, type):
        self.type = type
        print(type)
        

car1 = Prado("petrol")
car1.start()
car1.stop()

