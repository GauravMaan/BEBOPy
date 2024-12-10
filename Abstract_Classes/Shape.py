from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self, w, h):
        pass
    @abstractmethod
    def perimeter(self, b, height):
        pass
class Rectangle(Shape):
    def Area(self, w, h):
        print("Area of Rectangle:", w * h)

    def perimeter(self, b, height):
        print("Perimeter of Rectangle:", 2 * (b + height))
obj1 = Rectangle()
obj1.Area(2, 3)
obj1.perimeter(2, 3)

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def Area(self):
        print("Area of Rectangle:", self.width * self.height)
    def perimeter(self):
        print("Perimeter of Rectangle:", 2 * (self.width + self.height))
obj1 = Rectangle(2, 3)
obj1.Area()
obj1.perimeter()