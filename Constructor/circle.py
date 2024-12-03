import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(5)
print(f"Area of the circle: {circle.calculate_area():.2f}")
print(f"Circumference of the circle: {circle.calculate_circumference():.2f}")