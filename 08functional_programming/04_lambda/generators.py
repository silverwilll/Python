letters = (chr(x) for x in range(65, 91)) # A generator expression to create letters A-Z

#print(list(letters)) # get them one at a time, not generate them until needed
for s in letters:
    print(s, end=' ')