str1 = "Sadman"
str2 = "Adib"

print(str1+str2) # concatination
print(str1+" "+str2) # concat with space
print(len(str1)) #length of string
print(len(str1+" "+str2)) # length of concat string

# indexing
print(str1[0]) # S
print(str2[2]) # i

# index slicing ([starting index + ending index])
print(str1[0:4]) # Sadm (ending not included) (0123)
print(str2[0:2]) # Ad (ending not included) (01)
print(str2[0:]) # full 
print(str2[0:4]) # full 
print(str2[0:len(str2)]) # full 
print(str1[:6]) # full
print(str1[:len(str1)]) # full

#  negative index with slicing
print(str2[-4], str2[-3], str2[-2], str2[-1])
print(str2[-4:-1])

# string_functions
str3 = "my name is sadman_adib"
print(str3.endswith("dib")) #true or false
print(str3.endswith("di")) #true or false
print(str3.startswith("di")) #true or false
print(str3.startswith("my")) #true or false
print(str3.capitalize()) # m to M
print(str3.replace("a", "o")) # all a to o
print(str3.replace("sadman", "superman")) # all sadman to superman
print(str3.find("i")) # index number of first i
print(str3.find("h")) # index number of not available letter
print(str3.count("a")) # how many a's available



