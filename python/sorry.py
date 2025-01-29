import turtle

vr= turtle.Turtle()

turtle.Screen().bgcolor('black')
turtle.pensize(4)
vr.speed(10)

def drowcarve():
    for i in range(200):
        vr.right(1)
        vr.forward(1)

def txt():
    vr.up()
    vr.setpos(-68,88)
    vr.down()
    vr.color('white')
    vr.write("I Am So So Sorry", font=("Verdana",18,"bold"))


    vr.color('red')
    vr.begin_fill()
    vr.left(140)
    vr.forward(111.65)
    drowcarve()
    vr.left(120)
    drowcarve()
    vr.forward(111.65)
    vr.end_fill()
    vr.penup()
    vr.goto(77,-40)
    vr.pendown()
    vr.hideturtle()
    txt()
    turtle.done()
