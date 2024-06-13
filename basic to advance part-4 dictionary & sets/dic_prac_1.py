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

print(dic1["name"])
print(dic1["topic"])
print(dic1["marks"])
print(dic1["marks"]["ai"])
print(type(dic1))
print(dic1)