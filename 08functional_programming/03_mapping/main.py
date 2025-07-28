animals1 = ['cat', 'dog', 'ELEPHANT', 'rabbit']

animals2 = map(str.lower, animals1)
print(type(animals2))
for animal in animals2:
    print(animal)
print(list(animals2)) # This will print an empty list because the iterator has been exhausted.