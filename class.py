# Exemple of code in here


class myClass():
    def method1(self):
        print("the first method1")

    def method2(self, myString):
        print("the first method2" + myString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("another class method1")

    def method2(self, myString):
        print("another class method2" + myString)

def main():
    c = myClass()
    c.method1()
    c.method2("nacer kraa")

    c2 = anotherClass()
    c2.method1()
    c2.method2("this is another class")
   

if __name__ == "__main__":
    main()
