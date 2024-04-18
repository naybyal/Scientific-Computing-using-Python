class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        print("Name : ", self.name)
        print("Age : ", self.age)


class Teacher(Person):
    def __init__(self, name, age, course, exp):
        Person.__init__(self, name,age)
        self.course = course
        self.exp = exp

    def disData(self):
        Person.disp(self)
        print("Course :", self.course)
        print("Experience : ", self.exp, "yrs")


t1 = Teacher("xyz", 38, "OOP", 10)
t1.disData()