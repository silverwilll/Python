class Car:
    def start(self):
        print("Car is starting")

class Alarm:
    def on(self):
        print("Alarm is on")

class SafeCar(Car, Alarm):
    pass

s = SafeCar()
s.start()
s.on()