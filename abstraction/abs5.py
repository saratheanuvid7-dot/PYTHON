from abc import ABC, abstractmethod

class Person(ABC):
    @property
    @abstractmethod
    def profession(self):
        pass

class Doctor(Person):
    @property
    def profession(self):
        return "Doctor"

p = Doctor()
print(p.profession)
