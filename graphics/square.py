#   drawing a square using turtle

import turtle

t = turtle.Turtle()

t.setheading(90)
t.down()
for i in range(4):
    t.forward(100)
    t.right(90)


turtle.Screen().mainloop()