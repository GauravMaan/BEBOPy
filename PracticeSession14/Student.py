class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# Test the program
student = Student("gaurav", 23)
print("Name:", student.get_name())
print("Age:", student.get_age())

student.set_name("Vivek")
student.set_age(109)
print("Updated Name:", student.get_name())
print("Updated Age:", student.get_age())