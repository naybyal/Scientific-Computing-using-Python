import turtle
from turtle import *

t = Turtle()
my_window = Screen()
my_window.bgcolor('black')
t.speed(1)
t.width(3)
t.color('red')
# t.hideturtle()

def drawPolygon(t, vertices):
    t.up()
    (x,y) = vertices[-1]
    t.goto(x,y)
    t.down()
    for (x,y) in vertices:
        t.goto(x,y)

drawPolygon(t,[(20,20), (-20,20), (-20,-20), [20, -20]])
my_window.mainloop()