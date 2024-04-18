class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def disp(self):
        print("Name :", self.name)
        print("ID :", self.id)


class Manager(Employee):
    def __init__(self, name, id, salary):
        Employee.__init__(self, name, id)
        self.salary = salary

    def dispData(self):
        Employee.disp(self)
        print('Salary :', self.salary)


m1 = Manager("Jos Buttler", 9, 1200000)
m1.dispData()