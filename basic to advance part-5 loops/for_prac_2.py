# Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 

tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
print(tup1)

x = int(input("enter the num you want to search :"))
index = 0
for i in tup1:
    if(i == x):
        print("found at index :", index)
        break
    else:
        print("finding")

    index += 1    
