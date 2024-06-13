class person:
    __name = "anonymous" # private variable

    def __hello(self):   # private method
        print("hello person ,", self.__name)

    def welcome(self):
        self.__hello()
        print("you are accessing private name & method")


p1= person()
print(p1.welcome())        
       