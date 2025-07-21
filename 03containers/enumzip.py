fruits = ['apple', 'banana', 'cherry']
days = ['Monday', 'Tuesday', 'Wednesday']

for i, fruit in enumerate(fruits):
    print(i, fruit)

for fruit, day in zip(fruits, days):
    print(fruit, day)