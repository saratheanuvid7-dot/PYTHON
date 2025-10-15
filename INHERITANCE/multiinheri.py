class Father:
    def skills(self):
        print("Father: Knows driving")

class Mother:
    def skills(self):
        print("Mother: Knows cooking")

class Child(Father, Mother):
    def skills(self):
        print("Child: Learns both driving and cooking")

c = Child()
c.skills()
