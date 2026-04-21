import math 
import turtle 

screen = turtle.Screen()
screen.bgcolor("black") 

heart = turtle.Turtle()
heart.speed(0)
heart.color("red")
heart.width(2)
heart.hideturtle()

def draw_heart():
    heart.penup()
    for t in range(0,360):
        x =16*math.sin(math.radians(t))**3
        y= (13*math.cos(math.radians(t))
        -5*math.cos(2*math.radians(t))
        -2*math.cos(3*math.radians(t))
        -math.cos(4*math.radians(t)))
        heart.goto(x*15,y*15)
        heart.pendown()

draw_heart()
turtle.done()