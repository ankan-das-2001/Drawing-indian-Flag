import turtle as india
import time
screen = india.getscreen()
screen.title("INDIAN FLAG")

ak = india.Turtle()
ak.penup()
ak.setpos(-200,-300)
def rod():
    ak.pendown()
    ak.begin_fill()
    ak.fillcolor('grey')
    ak.left(90)
    ak.forward(500)
    ak.right(180)
    ak.circle(5)
    ak.left(90)
    ak.penup()
    ak.forward(10)
    ak.pendown()
    ak.right(90)
    ak.forward(500)
    ak.right(90)
    ak.forward(10)
    ak.end_fill()
    ak.penup()

def orange():
    ak.goto(-190,200)
    ak.pendown()
    ak.begin_fill()
    ak.fillcolor('orange')
    ak.right(180)
    ak.forward(250)
    ak.right(90)
    ak.forward(60)
    ak.right(90)
    ak.forward(250)
    ak.end_fill()
    ak.penup()

def ashok_chakra():
    ak.penup()
    ak.goto(-65,140)
    ak.pendown()
    ak.pencolor("blue")
    ak.circle(30)
    ak.penup()
    ak.goto(-65,110)
    ak.pendown()
    for i in range(24):
        ak.forward(30)
        ak.backward(30)
        ak.right(15)
    ak.penup()
    

def white():
    ak.goto(-190,140)
    ak.pendown()
    ak.left(90)
    ak.forward(60)
    ak.left(90)
    ak.forward(250)
    ak.left(90)
    ak.forward(60)
    ak.penup()
    


def green():
    ak.goto(-190,20)
    ak.begin_fill()
    ak.pendown()
    ak.fillcolor('green')
    ak.right(90)
    ak.forward(250)
    ak.left(90)
    ak.forward(60) 
    ak.left(90)
    ak.forward(250)   
    ak.end_fill()

def base():
    ak.goto(-200,-300)
    ak.pendown()
    ak.begin_fill()
    ak.pencolor("black")
    ak.fillcolor("saddle brown")
    ak.forward(90)
    ak.left(90)
    ak.forward(100)
    ak.left(90)
    ak.forward(200)
    ak.left(90)
    ak.forward(100)
    ak.left(90)
    ak.forward(110)
    ak.end_fill()


rod()
time.sleep(1)
orange()
time.sleep(1)
white()
time.sleep(1)
green()
time.sleep(1)
ashok_chakra()
time.sleep(1)
base()
time.sleep(1)
time.sleep(10)
