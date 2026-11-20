import sys

class Employee:
    # Class variable to keep record of created objects
    count = 0

    def __init__(self, emp_no, name, dept, basic, da, hra):
        if basic < 0 or da < 0 or hra < 0:
            print("Error: Basic, DA, and HRA cannot be negative. Terminating program.")
            sys.exit(1)

        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.basic = basic
        self.da = da
        self.hra = hra
        Employee.count += 1

    def salary(self):
        return self.basic + self.da + self.hra

    def __str__(self):
        return (
            f"Employee No: {self.emp_no}\n"
            f"Name: {self.name}\n"
            f"Department: {self.dept}\n"
            f"Basic: {self.basic}, DA: {self.da}, HRA: {self.hra}\n"
            f"Total Salary: {self.salary()}"
        )

    def __del__(self):
        Employee.count -= 1


# --- Testing the class ---
emp1 = Employee(101, "Rupa", "IT", 50000, 10000, 8000)
emp2 = Employee(102, "Sana", "HR", 45000, 9000, 7500)
emp3 = Employee(103, "Manya", "Finance", 60000, 12000, 10000)
emp4 = Employee(104, "Ruhi", "Marketing", 60000, 12000, 10000)  # This will replace the previous emp3

print(emp1)
print("-" * 30)
print(emp2)
print("-" * 30)
print(emp3)
print("-" * 30)
print(emp4)
print("-" * 30)
print("Total Employees:", Employee.count)

# Deleting an object to test __del__
del emp1
print("Total Employees after deleting emp1:", Employee.count)