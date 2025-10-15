from abc import ABC, abstractmethod

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    def fly(self):
        return "Bird is flying"

class Airplane(Flyable):
    def fly(self):
        return "Airplane is flying"

objects = [Bird(), Airplane()]
for obj in objects:
    print(obj.fly())
