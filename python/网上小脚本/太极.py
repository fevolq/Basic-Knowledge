import turtle

t = turtle.Turtle()


t.penup()
t.goto(0,-50)   #起始坐标
t.pendown()
t.begin_fill()
t.fillcolor('black')
t.circle(150,extent=180)
t.circle(75,extent=180)

t.circle(-75,extent=180)
t.end_fill()
t.circle(-150,extent=180)
t.penup()
t.goto(0,160)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.circle(30,extent=360)
t.end_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.begin_fill()
t.fillcolor('black')
t.circle(30,extent=360)
t.end_fill()
turtle.done()
