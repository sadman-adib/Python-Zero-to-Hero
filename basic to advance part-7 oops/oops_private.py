class account:
    def __init__(self, number, password):
        self.number = number
        self.__password = password # private access
                                    #(can not access outside the class)

    def showPass(self):
        self.__password
        print("access to the password :", self.__password)                                

person1 = account("102C", "200341")
print(person1.number)

print(person1.showPass()) # by this we can access through the pass

# print(person1.__password) # will not show (throw error)

