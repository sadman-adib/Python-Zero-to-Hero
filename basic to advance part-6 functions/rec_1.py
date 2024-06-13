# print 5 to 1

def des(n):
    if(n==0):
        return
    print(n, end=" ")
    des(n-1)

des(5)


