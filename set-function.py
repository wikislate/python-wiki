set1 =  {1, 2, 3, 4, 5}
set2 =  {3, 4, 5, 6, 7}
print("Union:",set.union(set1,set2))
print("Intersection:",set.intersection(set1,set2))
print("Difference:",set.difference(set1, set2))
print(set1)
print(set2)

print("Union:",set1.union(set2))
print(set1)

print("set1.union(set2): returns:")
set1.union(set2)
print("set.union(set1,set2): returns:")
set.union(set1,set2)
print("set1:",set1)

set3 = set1.union(set2)
print("set3:",set3)
