class Person:
    def __init__(self, name: str= "John"):
        self._name = name

    def eating(self):
        print(f"{self._name} is eating")
    
    def __str__(self):
        return f"Hello I am {self._name}"
    
    def __repr__(self):
        return f'Person("{self._name}")'

class Employee(Person):
    def go_on_holiday(self):
        print(f"{self._name} is going on holiday")

p = Person("Yufei")
e = Employee("Alice")
e.eating()
e.go_on_holiday()  # This will raise an AttributeError since Person has no go_on_holiday method
