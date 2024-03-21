import turtle
from turtle import *

t = Turtle()
my_window = Screen()
my_window.bgcolor('black')
t.speed(1)
t.width(3)
t.color('red')

def drawSquare(t, x, y, length):
    t.up()
    t.goto(x,y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)

drawSquare(t,50,50,100) 

my_window.mainloop()

