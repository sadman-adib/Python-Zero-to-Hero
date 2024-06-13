class person:
    name = "anonymous"
    name2 = "anonymous2"
    print(name,"," ,name2)

    def changeName(self, name, name2):
        person.name = name # change the name from the original name
        self.__class__.name2 = name2 # another way for the same

p1 = person()
p1.name
p1.name2
p1.changeName("nabila binte", "nabila binte haque")
print(person.name, end=" , ")
print(person.name2)