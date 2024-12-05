import sys
sys.path.append("/Users/gauravmaan/Desktop/BEBOPy/Shapes")

from Shapes import circle, rectangle
radius = 5
print(f"Circle with radius {radius}:")
print(f"Area: {circle.area(radius):.2f}")
print(f"Perimeter: {circle.perimeter(radius):.2f}")

length = 10
width = 4
print(f"\nRectangle with length {length} and width {width}:")
print(f"Area: {rectangle.area(length, width):.2f}")
print(f"Perimeter: {rectangle.perimeter(length, width):.2f}")


