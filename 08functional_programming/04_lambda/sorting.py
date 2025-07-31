animals1 = ["dog", "cat", "elephant", "ant", "zebra"]
animals2 = sorted(animals1, reverse=True, key=lambda s: len(s))

print(animals2)