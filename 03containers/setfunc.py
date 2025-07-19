numbers1 = {2, 4, 6, 7, 8, 10}
numbers2 = {2, 4, 6, 1, 3, 5}

print(numbers1.union(numbers2))  # Union of two sets
print(numbers1.intersection(numbers2))  # Intersection of two sets
print(numbers1.difference(numbers2))
print(numbers1 - numbers2) # Difference using operator
print(numbers2.difference(numbers1))
print(numbers2 - numbers1) # Difference using operator
print(numbers1.symmetric_difference(numbers2)) 

print({1, 2, 3}.issuperset({1, 2, 3})) 
print({1, 2, 3}.issubset({1, 2, 3, 4}))
print({1, 2, 3}.isdisjoint({1, 5}))  # Disjoint sets

print(numbers1 | numbers2) # Union using operator
print(numbers1 & numbers2) # Intersection using operator
