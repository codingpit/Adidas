import turtle
t=turtle.Turtle()
t.speed(10)

def leaf():
    t.begin_fill()
    t.circle(200,90)
    t.right(270)
    t.circle(200,90)
    t.end_fill()

leaf()

t.penup()
t.goto(-20,0)
t.pendown()
t.seth(45)
leaf()

t.penup()
t.goto(-40,0)
t.pendown()
t.seth(90)
leaf()

t.color("white")
t.pensize(15)
def lines(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.forward(400)

lines(-220,110)
lines(-220,75)
lines(-220,40)

t.pencolor("black")
t.penup()
t.goto(-160,-130)
t.pendown()
t.write("adidas", font=("Comic Sans MS",80))
t.hideturtle()
turtle.done()