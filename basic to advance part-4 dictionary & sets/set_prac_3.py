# Figure out a way to store 9 & 9.0 as separate values in the set. 
# (You can take help of built-in data types) 

a = int(input("enter int num :"))
b = float(input("enter same int as float number :"))
c= str(b)

set1 = {a, c}
print(set1)