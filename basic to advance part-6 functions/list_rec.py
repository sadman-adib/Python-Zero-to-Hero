def list(l, idx=0):
    if(idx == len(l)):
        return
    print(list[idx])
    list(l, idx+1)   


numbers = [1,2,3,4,5]
print(numbers, end=" ")

        