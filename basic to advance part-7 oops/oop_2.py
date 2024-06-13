class student:

    varsity_name = "uiu"

    def __init__(self, name, age, dept): # constructors
        self.name = name
        self.age = age
        self.dept = dept
        print("adding new student in record :")

    def hello(self):
        print("welcome:", self.name)    

s1= student("sadman haque", 21, "cse")
s1.hello()
print(s1.age)
print(s1.dept)
print(s1.varsity_name)

s2= student("binte nabila", 22, "cse")
s2.hello()
print(s2.age)
print(s2.dept)
print(s2.varsity_name)

s3= student("jannatul atoshe", 25, "cse")
s3.hello()
print(s3.age)
print(s3.dept)
print(s3.varsity_name)
       