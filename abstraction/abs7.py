from abc import ABC, abstractmethod

class Device(ABC):
    def brand(self):
        return "Generic Brand"
    
    @abstractmethod
    def type(self):
        pass

class Laptop(Device):
    def type(self):
        return "This is a Laptop"

d = Laptop()
print(d.brand(), "|", d.type())
