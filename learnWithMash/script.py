# Define a function

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


Point2 = Point(10, 20)
print(Point2.x)