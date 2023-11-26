class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Name: {self.name}, Employee ID: {self.employee_id}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def display_info(self):
        info = super().display_info()
        return f"{info}, Role: Manager, Salary: ${self.salary}"

    def project_leave(self):
        return "Project approved by Manager"

class Engineer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def display_info(self):
        info = super().display_info()
        return f"{info}, Role: Engineer, Salary: ${self.salary}"

    def code(self):
        return "Engineer coding"

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, commission):
        super().__init__(name, employee_id)
        self.salary = salary
        self.commission = commission

    def display_info(self):
        info = super().display_info()
        return f"{info}, Role: Salesperson, Salary: ${self.salary}, Commission: {self.commission}%"

    def make_sale(self):
        return "Salesperson made a sale"

if __name__ == "__main__":
    manager = Manager("Robert", "manager321", 80000)
    engineer = Engineer("Alice Smith", "engineer12", 70000)
    salesperson = Salesperson("Bob Johnson", "sales_person33224", 60000, 10)

    print(manager.display_info())
    print(manager.project_leave())

    print(engineer.display_info())
    print(engineer.code())

    print(salesperson.display_info())
    print(salesperson.make_sale())