class Employee:
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary
    def give_raise(self, percent):
        self.salary += self.salary * (percent / 100)
        print(f"Salary updated New salary of {self.name} is {self.salary:.2f}")
    def display(self):
        print(f"ID: {self.eid}, Name: {self.name}, Salary: {self.salary:.2f}")
    def __str__(self):
        return f"ID={self.eid}, Name={self.name}, Salary={self.salary:.2f}"
employee1 = Employee(101, "Gaurav", 50000)
employee1.display()
employee1.give_raise(10)
print(employee1)