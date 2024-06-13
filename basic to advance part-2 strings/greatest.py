#WAP to find the greatest of 3 numbers entered by the user.

num1=float(input("enter 1st number :"))
num2=float(input("enter 2nd number :"))
num3=float(input("enter 3rd number :"))

if(num1>num2 and num1>num3):
    print("Number 1 is greatest")
elif(num2>num1 and num2>num3):
    print("Number 2 is greatest")
elif(num3>num1 and num3>num2):
    print("Number 3 is greatest")   
else:
    print("No number is greatest")
