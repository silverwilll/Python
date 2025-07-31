def PowersOfTwo():
    for i in range(8):
        yield 2 ** i

for x in PowersOfTwo():
    print(x, end=' ')

print()
print(type(PowersOfTwo()))