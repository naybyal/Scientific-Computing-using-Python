import turtle
import sys
n = int(input("enter the number of sides.... "))

if n<3:
    sys.exit()

#   computing angles...
theta1 = 360/n
theta2 = abs(180 - theta1)

t = turtle.Turtle()

t.setheading(theta2)

for i in range(n):
    t.forward(200)
    t.right(theta1)


turtle.Screen().mainloop()