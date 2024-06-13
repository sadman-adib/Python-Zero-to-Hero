#  Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

class student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        print("name and avg marks of 3 subjects:")

    @staticmethod   #decorator (when the function need no changes)
    def clgName():
         print("your varsity name is uiu.")    

    def avg(self):
            sum = self.marks1 + self.marks2 + self.marks3
            print("hi,", self.name, ".", "your avg marks is :", sum/3)

s1 = student("sadman", 10, 25, 30)   
s1.avg()    
s1.clgName()