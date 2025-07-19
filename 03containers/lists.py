fruits = ["apple", "banana", "cherry"]
print(id(fruits)) # check ID of the list
fruits += ["melon", "kiwi"]

print(fruits)
fruits[0] = "blueberry" 
print(id(fruits))

fruits.append("orange")
fruits.extend(["grape"])

print(fruits)
fruits.insert(2, "pineapple") # insert at index 2
print(fruits)

fruits_tuple = tuple(fruits) # convert to tuple
print(fruits_tuple)

fruits_list = list(fruits_tuple) # convert back to list
print(fruits_list)
