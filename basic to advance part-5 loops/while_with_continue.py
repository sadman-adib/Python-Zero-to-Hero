# print even number

i = 1

while i <= 10:
    if(i%2!=0):
        i += 1
        continue #skip the following value
    
    print(i)
    i += 1