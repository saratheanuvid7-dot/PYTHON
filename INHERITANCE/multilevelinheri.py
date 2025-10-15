class Grandparent:
    def show(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show(self):
        print("I am Parent")

class Child(Parent):
    def show(self):
        print("I am Child")

c = Child()
c.show()
