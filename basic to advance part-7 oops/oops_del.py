class student:
    def __init__(self, name):
        self.name = name
        

s1 = student("sadman")
print(s1.name)

s2 = student("shraboni") 
print(s2.name)

s4 = student("nabila")
print(s4.name)

s3 = student("robin")
del s3.name #deleted 
# print(s3.name) #throw error
    