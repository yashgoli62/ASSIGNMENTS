class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: {self.salary}")


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_employee()
        print(f"Department: {self.department}")


m = Manager("Shubham", 21, "M101", 75000, "IT")
m.display_manager()