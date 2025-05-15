class Employee:
    def __init__(self, name , salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("Employee", 50000, "123-45-634") 

print("Public - Name:", emp.name)

print("Protected - Salary:", emp._salary)


try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Cannot access directly Error", e)

print("Private - SSN (accessed using name mangling):", emp._Employee__ssn)    