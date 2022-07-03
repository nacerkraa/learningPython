# Define a function

class Person:
    def __init__(self, name):
        self.name = name


    def Talk(self):
        print("Hello")

person1 = Person("Nacer")

print(person1.name)

person1.Talk()