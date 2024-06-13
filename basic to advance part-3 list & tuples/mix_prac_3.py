#  WAP to count the number of students with the “A” grade in the following tuple.
#  [”C”, “D”, “A”, “A”, “B”, “B”, “A”]
#  Store the above values in a list & sort them from “A” to “D”

tup1= ("c", "d", "a", "a", "b", "b", "a")
print("students count with a grade :", tup1.count("a"))

l1 = tup1[0]
l2 = tup1[1]
l3 = tup1[2]
l4 = tup1[3]
l5 = tup1[4]
l6 = tup1[5]
l7 = tup1[6]

list1 = [l1, l2, l3, l4, l5, l6, l7]
print(list1)

list1.sort()
print(list1)
