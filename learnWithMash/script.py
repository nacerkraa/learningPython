# Define a function

class Animal:
    def walk(self):
        print("Walking")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

ca1 = Cat()
ca1.walk()