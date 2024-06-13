class employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    
    def showDetails(self):
        print("role :", self.role)
        print("dept :", self.dept)
        print("sal :", self.sal)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "tech", "45000")
        print("name :", name)
        print("age :", age)

e1 = engineer("nabila binte", 23)
e1.showDetails()

