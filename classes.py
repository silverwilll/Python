class Person:
    def __init__(self, name: str= "John"):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating")
    
    def __str__(self):
        return f"Hello I am {self._name}"

p = Person("Yufei")
text = str(p)
print(f"text: {text}")
p.eating()
print(p)