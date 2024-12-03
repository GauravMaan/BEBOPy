class Shape:
    def __init__(self):
        self.type = "Generic"

    def display(self):
        print(f"Shape type: {self.type}")
shape = Shape()
shape.display()