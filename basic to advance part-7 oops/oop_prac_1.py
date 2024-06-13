# Create Account class with 2 attributes - balance & account no. 
# Create methods for debit(balance minus), credit(balance plus) & 
# printing the balance.

class account:

    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def debit(self, amount): 
            self.balance = self.balance - amount
            print("after decrease", amount,"taka", "your balance is :", self.balance) 


    def credit(self, amount): 
            self.balance = self.balance + amount
            print("after increase", amount,"taka", "your balance is :", self.balance) 

    def final(self):
          print("your final balance is :", self.balance)        

p1 = account("1002C", 1000)  
print("your account number is :", p1.account)
p1.debit(200)
p1.credit(1000)
p1.final()
