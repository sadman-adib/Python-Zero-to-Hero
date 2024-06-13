class person:
    name = "anonymous"
    print(name)

    @classmethod
    def chngName(cls, name):
        cls.name = name

  

p1 = person()
p1.name
p1.chngName("nabila binte")
print(person.name)
