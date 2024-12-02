class Student:
    name = ""
    grade = ""
    def display_info(self, name, grade):
        print(name, grade)
student1 = Student()
student2 = Student()
student1.display_info("gaurav", 67)
student2.display_info("vivek", 90)
