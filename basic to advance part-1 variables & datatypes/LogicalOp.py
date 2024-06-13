print("not start:-")
print(not True)
print(not False)

a=50
b=3
c= not (a<b) # true
d= not (a>b) # false
print(c)
print(d)

print("and start:-")
print((a==b) and (a>=b)) # false
val1 = True
val2 = True
val3 = False
print("ans of and :", val1 and val2) # true
print("ans2 of and :", val2 and val3) # false

print("or start:-")
print((a==b) or (a>=b)) # true
print("ans3 of or :", val1 or val3)