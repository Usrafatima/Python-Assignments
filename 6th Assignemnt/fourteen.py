class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(f"- {emp.name}")

emp1 = Employee("Yusra")
emp2 = Employee("Ali")

dept = Department("IT", [emp1, emp2])

dept.show_employees()
