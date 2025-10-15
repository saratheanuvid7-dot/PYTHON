from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def role(self):
        pass

class Manager(Employee):
    def role(self):
        return "Manages Team"

class Developer(Employee):
    def role(self):
        return "Writes Code"

staff = [Manager(), Developer()]
for s in staff:
    print(s.role())
