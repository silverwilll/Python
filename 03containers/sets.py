numbers = {1, 3, 6, 4}
print(numbers)

for x in numbers:
    print(x) # order is not guaranteed

print(3 in numbers) # True
numbers.add(7)
print(numbers)

numbers.update([9, 8, 10]) # add multiple items
print(numbers)

numbers.remove(8)
print(numbers)

numbers.discard(0)
print(numbers) # does not raise an error if the item is not found
numbers.discard(1)
print(numbers)

print(set(["1, 2", "3", "4"])) # set with string elements
print(set(n for n in range(5)))

x = [n for n in range(5)]
print(x) # generator expression, not a set