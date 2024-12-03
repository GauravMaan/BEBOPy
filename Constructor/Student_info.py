class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def update(self, amarks):
        self.marks += amarks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student = Student("gaurav", 85)
student.display()
student.update(5)
student.display()