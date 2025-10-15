class Vehicle:
    def type(self):
        print("This is a vehicle")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels")

c = Car()
b = Bike()

c.type(); c.wheels()
b.type(); b.wheels()
