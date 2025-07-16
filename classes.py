class Person:
    def __init__(self, name: str= "John"):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating")

p = Person("Yufei")
p.eating()
print(p)