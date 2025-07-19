animals = ("cat", "dog", "fish", "giarffe", "elephant", "lion")

print(animals[2])
print(animals[1:4]) # slicing from index 1 to 3 (4 is not included)
print(animals[-1]) # last element
print(animals[-4:-1]) # slicing from the third last element to the end

print(animals[0:-1:2]) # slicing with step, from index 0 to the second last element, taking every second element
print(animals[:3])
print(animals[::3])
print(animals[::])
print(animals[:])
