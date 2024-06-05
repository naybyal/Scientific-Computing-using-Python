import turtle

t = turtle.Turtle()


t.setheading(60)
t.down()
for i in range(6):
    t.forward(100)
    t.right(60)

turtle.Screen().mainloop()