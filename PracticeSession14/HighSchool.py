class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_school_info(self):
        return f"School Name: {self.name}, Location: {self.location}"

class Student(School):
    def __init__(self, name, location, student_name, grade):
        super().__init__(name, location)
        self.student_name = student_name
        self.grade = grade

    def display_student_info(self):
        return f"Student Name: {self.student_name}, Grade: {self.grade}"

class HighSchoolStudent(Student):
    def __init__(self, name, location, student_name, grade, subjects):
        super().__init__(name, location, student_name, grade)
        self.subjects = subjects

    def display_highschool_info(self):
        return f"High School Student: {self.student_name}, Grade: {self.grade}, Subjects: {', '.join(self.subjects)}"

# Test the program
school = HighSchoolStudent("Government High", "India", "Gaurav", "10th", ["Math", "Science", "English"])
print(school.display_school_info())
print(school.display_student_info())
print(school.display_highschool_info())