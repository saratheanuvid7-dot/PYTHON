from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car started"
    def stop(self):
        return "Car stopped"

c = Car()
print(c.start(), "|", c.stop())
