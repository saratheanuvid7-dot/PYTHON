# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child class (inherits from Animal)
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks ")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows ")

# Objects
dog1 = Dog("Tommy")
cat1 = Cat("Kitty")

dog1.speak()
cat1.speak()
