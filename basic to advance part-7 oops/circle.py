# circle, area, perimeter

class circle:
    def __init__(self, r):
        self.r = r
        print(r)
    
    def area(self):
        print("area :", (3.1416 * self.r ** 2))

    def perimeter(self):
        print("perimeter :", 2 * 3.1416 * self.r)   


c1 = circle(21)   
c1.area()
c1.perimeter()   


