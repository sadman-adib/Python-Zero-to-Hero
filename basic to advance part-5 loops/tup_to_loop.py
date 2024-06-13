#  Search for a number x in this tuple using loop:
#  [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

index = 0
x = int(input("the value you want to search :"))

while index <= len(tup)-1:
    if(tup[index]==x):
        print("number found at index :", index)
        break
    else:
        print("still finding, wait please...")  
    index += 1      