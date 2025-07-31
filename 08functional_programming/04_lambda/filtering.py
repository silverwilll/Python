fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits_filtered = filter(lambda fruit: 'e' in fruit, fruits)
print(type(fruits_filtered))
print(list(fruits_filtered))