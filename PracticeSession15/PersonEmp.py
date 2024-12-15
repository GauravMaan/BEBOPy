class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, salary):
        self.salary = salary
class Manager(Person, Employee):
    def __init__(self, name, age, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, salary)
        self.department = department
manager = Manager("Gaurav", 23, 7500000, "HR")
print(manager.name)
print(manager.age)
print(manager.salary)
print(manager.department)