import turtle

t = turtle.Turtle()

t.setheading(72)
t.down()
for i in range(5):
    t.forward(300)
    t.right(144)


turtle.Screen().mainloop()