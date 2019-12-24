#stickman
#Joshua Johnson
#April 6, 2018

#The objective of this code was to draw a stickfigure and their pet using turtle.
#I drew the stickfigure along with a duck and a turtle.

#initialize turtle
import turtle

turtle.bgcolor("skyblue")   #sets background color

t = turtle.Pen()            #t set to a pen
t.speed(1)                  #speed of t
v = turtle.Pen()            #v set to a pen
v.speed(1)                  #speed of v
w = turtle.Pen()            #w set to a pen
w.speed(1)                  #speed of w
y = turtle.Pen()            #y set to a pen
y.speed(1)                  #speed of y

v.hideturtle()              #hide v
w.hideturtle()              #hide w
y.hideturtle()              #hide y

#functions in alphabetical order
def duck():
    #this function will draw a duck
    v.showturtle()
    v.penup()
    v.setpos(50,-40)
    v.pendown()
    v.fillcolor("gold")
    v.left(90)
    v.shape("circle")
    v.shapesize(5,4,2)
    w.showturtle()
    w.penup()
    w.setpos(20,-30)
    w.pensize(2)
    w.pendown()
    w.fillcolor("gold")
    w.begin_fill()
    w.circle(30)
    w.end_fill()
    w.penup()
    w.setpos(10,10)
    w.pendown()
    w.dot(8)
    w.penup()
    w.setpos(-10,5)
    w.right(90)
    w.pendown()
    w.fillcolor("orange")
    w.begin_fill()
    w.forward(10)
    w.right(90)
    w.forward(15)
    w.right(150)
    w.forward(18)
    w.right(120)
    w.end_fill()
    w.penup()
    w.setpos(40,-80)
    w.pensize(2)
    w.pendown()
    w.begin_fill()
    w.forward(20)
    w.right(90)
    w.forward(20)
    w.right(150)
    w.forward(23)
    w.right(120)
    w.end_fill()
    w.penup()
    w.setpos(65,-80)
    w.pendown()
    w.begin_fill()
    w.forward(20)
    w.right(90)
    w.forward(20)
    w.right(150)
    w.forward(23)
    w.end_fill()
    w.penup()
    w.setpos(95,-25)
    w.right(30)
    w.pendown()
    w.fillcolor("gold")
    w.begin_fill()
    w.circle(20,100)
    w.left(20)
    w.circle(30,-100)
    w.forward(5)
    w.end_fill()
    w.hideturtle()

def stickman():
    #this function will draw the stickman
    t.penup()
    t.setpos(-200,150)
    t.pensize(5)
    t.pendown()
    t.fillcolor("#D7A634")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
    t.setpos(-220,210)
    t.pendown()
    t.circle(2)
    t.penup()
    t.setpos(-180,210)
    t.pendown()
    t.circle(2)
    t.penup()
    t.setpos(-214,180)
    t.right(90)
    t.pendown()
    t.circle(16,180)
    t.penup()
    t.setpos(-200,150)
    t.right(180)
    t.pensize(10)
    t.pendown()
    t.forward(150)
    t.left(20)
    t.forward(100)
    t.penup()
    t.setpos(-200,0)
    t.right(40)
    t.pendown()
    t.forward(100)
    t.penup()
    t.setpos(-200,80)
    t.left(135)
    t.pendown()
    t.forward(80)
    t.penup()
    t.setpos(-200,80)
    t.left(130)
    t.pendown()
    t.forward(80)
    t.hideturtle()

def turtle():
    #this function will draw a turtle
    y.showturtle()
    y.penup()
    y.setpos(250,-50)
    y.left(180)
    y.fillcolor("green")
    y.pendown()
    y.shape("turtle")
    y.shapesize(5)

#calling the functions in correct order
stickman()
duck()
turtle()
