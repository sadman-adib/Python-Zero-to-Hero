class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod # method with  no attribute variable
    def stop():
        print("car stopped...") 

class ToyotaCar(car): # inheritance with super method accessing from parent
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type) # come from car class
        super().start() 
        

car1 = ToyotaCar("prado","petrol")
print(car1.brand)
print(car1.type)


