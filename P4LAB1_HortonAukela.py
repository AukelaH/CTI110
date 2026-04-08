import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("brown")
pen.pensize(3)
pen.speed(3)
pen.penup()
pen.goto(-50, -50)
pen.pendown()
for i in range(4):
    pen.forward(100)
    pen.left(90)
pen.penup()
pen.goto(-50, 50)
pen.pendown()
count = 0
while count < 3:
    pen.forward(100)
    pen.left(120)
    count += 1
pen.penup()
pen.goto(-10, -50)
pen.pendown()

for i in range(2):
    pen.forward(20)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
turtle.done()        