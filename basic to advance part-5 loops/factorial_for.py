n = int(input("enter number :"))

fact = 1

for i in range(1, n+1):
    fact *= i
    # print(fact)

print("fact of the number :", fact)