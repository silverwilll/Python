numbers = [0, 1, 2, 3, 4, 5, 6, 7]
print(id(numbers))
numbers.remove(4) # remove the first occurrence of 4, python has to search the whole list to find the item
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

numbers = [7, 6, 5, 4, 3, 2, 1]
numbers.pop(1) # remove the item at index 1
print(numbers)

del numbers[2] # delete the item at index 2
print(numbers)


value = numbers.pop(1) 
print(value, numbers)
numbers.clear()
