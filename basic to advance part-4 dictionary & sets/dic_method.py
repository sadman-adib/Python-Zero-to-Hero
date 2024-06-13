dic1 ={
     "keys" : "values",
     "name" : "sadman",
     "age" : 24,
     "gpa" : 3.5,
     "subject" : ("cn", "micro", "ai"), # tuple
     "marks" :{ # nested dictionary
         "cn" : 100,
         "micro" : 90,
         "ai" : 95
     },
     "topic" : ["c", "java", "python"] # list
}

print(dic1.keys()) 
c = list(dic1.keys())
print(c)
print(len(dic1))
print(dic1.values())
print(dic1.items()) # print the pair of key and values

pair = list(dic1.items()) # print the perticular list index in form of tuple
print(pair[5]) 

d = dic1.get("topic") # get the perticular values of the key from the get method
print(d)

dic1.update({"city" : ["dhaka", "khulna", "ctg"]}) # add new key and values in dic1
print(dic1)