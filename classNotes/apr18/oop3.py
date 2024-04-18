class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def disp(self):
        print("Name :", self.name)
        print("ID :", self.id)

class Department:
    def __init__(self, department):
        self.department = department

    def dispDepartment(self):
        print("Department :", self.department)

class Manager(Employee, Department):
    def __init__(self, name, id, salary, department):
        Employee.__init__(self, name, id)
        Department.__init__(self, department)
        self.salary = salary

    def dispData(self):
        Employee.disp(self)
        Department.dispDepartment(self)
        print('Salary :', self.salary)


m1 = Manager("Jos Buttler", 9, 1200000, "HR")
m1.dispData()
