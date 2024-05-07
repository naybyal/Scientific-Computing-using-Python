from turtle import Turtle


t = Turtle()
t.pencolor('white')
t.screen.bgcolor('black')
for i in range(4):
    t.forward(90)
    t.right(90)

t.hideturtle()

t.screen.mainloop()