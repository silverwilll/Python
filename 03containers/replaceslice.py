numbers = list((0, 1, 2, 3, 4, 5, 6, 7))

numbers[2:4] = [0, 0 , 0 , 0]  # replace slice from index 2 to 3 with new values
print(numbers)

print(numbers[2:6])

numbers[2:6] = [] 
print(numbers)

print(numbers[1::2])
numbers[1::2] = ["hello", "world", "python"]
print(numbers)
