class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print('Area =', self.l*self.w)

    def disp(self):
        print("This is a rectangle")

class Shape:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print('Area =', self.l*self.w)
   
    def disp(self):
        print("This is a geometric shape")


r = Rectangle(12,10)
s = Shape(10, 13)

s.disp()
r.disp()

s.area()
r.area()

'''
This is a geometric shape
This is a rectangle
Area = 130
Area = 120
'''

# some code can be reused. Here, we can use polymorphism