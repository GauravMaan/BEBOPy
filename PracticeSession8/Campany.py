class Company:
    company_name = "BEBO"
    def __init__(self, employee_name, designation):
        self.employee_name = employee_name
        self.designation = designation
    def display_info(self):
        print(f"Employee Name: {self.employee_name}, Designation: {self.designation}, Company: {Company.company_name}")
employee1 = Company("Gaurav", "Tester")
employee2 = Company("Vivek", "Developer")
employee3 = Company("Girl", "Manager")
employee1.display_info()
employee2.display_info()
employee3.display_info()