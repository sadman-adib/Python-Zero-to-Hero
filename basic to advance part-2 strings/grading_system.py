# grading system

num = int(input("Enter your number :"))

if (num < 0 or num > 100):
    print("Enter a valid number")
elif(num>=90):
    print(4)
elif(86<=num<90):
    print(3.67)
elif(55<=num<86):
    print("pass")
else:
    print("fail")
       
