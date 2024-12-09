# import math
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method")
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius**2
# rectangle = Rectangle(4, 5)
# print(f"Rectangle Area: {rectangle.area()}")
# circle = Circle(3)
# print(f"Circle Area: {circle.area():.2f}")

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

# Array of shapes
shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(6, 7),
    Circle(2)
]
for shape in shapes:
    print(shape.area())