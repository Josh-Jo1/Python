#initials
#Joshua Johnson
#April 6, 2018

#The objective of this code was to draw my initials using turtle.
#I drew my initials along with a flower and a star.

#initialize turtle
import turtle           

turtle.bgcolor("#3DDBFA")   #sets background color

t = turtle.Pen()            #t set to a pen
t.pencolor("#FA5050")       #pen color of t
t.pensize(15)               #pen size of t
t.speed(1)                  #speed of t
t.penup()

#functions in alphabetical order

def dot():
    #this function will draw the dot
    t.home()
    t.dot(30)

def flower(x,y):
    #initialize
    t.setpos(x,y)       #position based on input
    t.left(10)
    
    for x in range(4):
        #this loop will draw a flower
        t.pencolor("orange")
        t.pendown()
        t.circle(-40,180)
        t.right(90)
        t.penup()

def initialFirst():
    #this function will draw the first "J"
    t.setpos(-150,100)
    t.pendown()
    t.forward(100)
    t.setpos(-100,100)
    t.right(90)
    t.forward(80)
    t.circle(-25,180)
    t.penup()

def initialLast():
    #this function will draw the last "J"
    t.setpos(80,100)
    t.pendown()
    t.forward(100)
    t.setpos(130,100)
    t.right(90)
    t.forward(80)
    t.circle(-25,180)
    t.penup()

def star(x,y):
    #initialize
    t.setpos(x,y)       #position based on input
    t.right(40)

    for x in range(5):
        #this loop will draw a star
        t.pencolor("gold")
        t.pendown()
        t.forward(150)
        t.right(144)
        t.penup()

#calling the functions in correct order
initialFirst()
dot()
initialLast()
flower(-270,100)
star(250,50)

#hide t when finished
t.hideturtle()
