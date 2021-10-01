from turtle import *
import turtle

ggf = turtle.Turtle()

ggf.pencolor('#078543')
ggf.width(2)

#Huruf G
def huruf_G() :
    ggf.fillcolor('#078543')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(110)
    ggf.circle(100,340)
    ggf.left(90)
    ggf.forward(100)
    ggf.left(90)
    ggf.circle(25,90)
    ggf.forward(20)
    ggf.left(240)
    ggf.circle(-50,300)
    ggf.left(60)
    ggf.forward(50)
    ggf.left(90)
    ggf.forward(7.5)
    ggf.end_fill()

#Huruf F
def huruf_F() :
    ggf.fillcolor('#078543')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(180)
    ggf.forward(130)
    ggf.left(90)
    ggf.forward(190)
    ggf.left(90)
    ggf.forward(50)
    ggf.left(90)
    ggf.forward(80)
    ggf.right(90)
    ggf.forward(40)
    ggf.circle(40,90)
    ggf.left(90)
    ggf.forward(80)
    ggf.right(90)
    ggf.forward(30)
    ggf.right(90)
    ggf.forward(40)
    ggf.circle(40,90)
    ggf.end_fill()

def icon_orange() :
    ggf.pencolor('#fbaa1a')
    ggf.fillcolor('#fbaa1a')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(110)
    ggf.circle(150,90)
    ggf.left(80)
    ggf.circle(150,35)
    ggf.left(10)
    ggf.circle(145,63)
    ggf.end_fill()

def icon_green() :
    ggf.pencolor('#a6ce38')
    ggf.fillcolor('#a6ce38')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(45)
    ggf.circle(90,80)
    ggf.circle(40,180)
    ggf.circle(170,18)
    ggf.circle(-50,40)
    ggf.end_fill()

def icon_greenyellow() :
    ggf.pencolor('#d6df22')
    ggf.fillcolor('#d6df22')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(70)
    ggf.circle(-160,40)
    ggf.circle(-40,220)
    ggf.right(10)
    ggf.circle(100,50)
    ggf.end_fill()

def icon_blue() :
    ggf.pencolor('#27aae2')
    ggf.fillcolor('#27aae2')
    ggf.begin_fill()
    ggf.pendown()
    ggf.setheading(90)
    ggf.circle(45,360)
    ggf.end_fill()

def ggftext() :
    ggf.setheading(0)
    ggf.pencolor('#078543')
    ggf.fillcolor('#078543')
    ggf.write('GREAT', move=False, align='left', font=('Arial Rounded MT', 35, 'bold'))
    ggf.sety(-18)
    ggf.write('GIANT', move=False, align='left', font=('Arial Rounded MT', 35, 'bold'))
    ggf.sety(-53)
    ggf.write('FOODS', move=False, align='left', font=('Arial Rounded MT', 35, 'bold'))

ggf.penup()
ggf.goto(-200,60)
huruf_G()

ggf.penup()
ggf.goto(20,60)
huruf_G()

ggf.penup()
ggf.goto(190,120)
huruf_F()

ggf.penup()
ggf.goto(200,160)
icon_orange()

ggf.penup()
ggf.goto(210,210)
icon_green()

ggf.penup()
ggf.goto(220,170)
icon_greenyellow()

ggf.penup()
ggf.goto(320,120)
icon_blue()

ggf.penup()
ggf.goto(230,20)
ggftext()

ggf.hideturtle()

turtle.done()
