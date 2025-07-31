value = 0

while value < 5:
    print("While loop iteration:", value)
    value += 1

    if value == 2:
        continue

    if value > 3:
        print("Value is greater than 3, breaking the loop.")
        break
else:
    print("Finished")