# Define a function

class Person:
    def __init__(self, name):
        self.name = name


    def Talk(self):
        print(f"Hello, I'm {self.name}")

person1 = Person("Ahmed")

print(person1.name)

person1.Talk()