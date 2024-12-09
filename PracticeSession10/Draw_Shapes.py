class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses must implement the draw method")

class Square(Shape):
    def draw(self):
        print("Drawing a Square.")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle.")

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle.")
shapes = [
    Square(),
    Triangle(),
    Circle(),
    Square(),
    Circle()
]
for shape in shapes:
    shape.draw()