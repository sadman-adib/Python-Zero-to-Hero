coll = set() # empty set
print(coll)

coll2 = {1,1,1,2,2,2,3,4,5}
print(coll2)

coll2.add(6)
print(coll2)

coll2.remove(1)
print(coll2)

print(coll2.pop()) #remove a random value
print(coll2.pop()) #remove a random value
print(coll2.pop()) #remove a random value

coll2.clear()
print(len(coll2))