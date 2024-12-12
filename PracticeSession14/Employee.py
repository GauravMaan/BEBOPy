from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def get_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self):
        return self.hourly_rate * self.hours_worked
full_time_employee = FullTimeEmployee(5000)
part_time_employee = PartTimeEmployee(20, 100)

print("Full-time employee salary:", full_time_employee.get_salary())
print("Part-time employee salary:", part_time_employee.get_salary())