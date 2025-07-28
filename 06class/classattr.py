class Machine:
    count = 0

    def __init__(self):
        Machine.count += 1

Machine()

print(Machine.count)

Machine()

print(Machine.count)