animals1 = ['cat', 'dog', 'ELEPHANT', 'rabbit']

animals2 = map(lambda s: s[:3].lower(), animals1)

print(list(animals2))