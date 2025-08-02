with open('test2.bin', 'rb') as file:
    data = file.read(5) # read 5 bytes
    print(data)

print(data[0])
print(data[1])
