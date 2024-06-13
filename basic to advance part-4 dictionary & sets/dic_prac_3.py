# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
#  an empty dictionary & add one by one. Use subject name as key & marks as value

a = str(input("enter the 1st subject :"))
b = str(input("enter the 2nd subject :"))
c = str(input("enter the 3rd subject :"))
d= int(input("enter the marks of 1st subject :"))
e= int(input("enter the marks of 2nd subject :"))
f= int(input("enter the marks of 3rd subject :"))

dic1={
    a : d,
    b : e,
    c : f
}

print(dic1)
