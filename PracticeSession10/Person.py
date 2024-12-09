class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

class Employee(Person):
    def emp_details(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display(self):
        super().display()
        print(self.employee_id,self.salary)
employee = Employee()
employee.set_details("Gaurav", 23)
employee.emp_details("E123", 50000)
employee.display()