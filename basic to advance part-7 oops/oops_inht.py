class car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...") 

class bmwCar(car): # inheritance
    def __init__(self, name):
        self.name = name
        print(name) 

car1 = bmwCar("prado")

car1.start()
car1.stop()

