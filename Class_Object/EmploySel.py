class Employee:
    def set_details(self, name, salary):
        self.name = name
        self.salary = salary
    def update_salary(self, new_salary):
        self.salary = new_salary
    def display_salary(self):
        print(f"{self.name}'s updated salary is: {self.salary}")
emp = Employee()
emp.set_details("John", 50000)
emp.update_salary(60000)
emp.display_salary()
