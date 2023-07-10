import turtle
from turtle import *

# screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(0)


# functions to reduce some lines
def pos_change(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def right_forward(r, f):
    t.right(r)
    t.forward(f)


def left_forward(l, f):
    t.left(l)
    t.forward(f)


# initially penup()
pos_change(-250, 290)

# Create the stand
t.left(90)
t.color("brown")
t.begin_fill()
t.circle(12)
left_forward(90, 6)
t.end_fill()
t.color("brown")
t.begin_fill()
left_forward(90, 590)
left_forward(90, 40)
right_forward(90, 10)
right_forward(90, 90)
right_forward(90, 10)
right_forward(90, 40)
left_forward(90, 600)
right_forward(90, 10)
right_forward(90, 25)
t.left(90)
t.end_fill()

# Orange Rectangle + white rectangle
t.color("orange")
t.begin_fill()
t.forward(520)
right_forward(90, 97)
right_forward(90, 520)
t.end_fill()
left_forward(90, 97)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(97)
left_forward(90, 520)
left_forward(90, 97)
t.end_fill()

# Big Blue Circle

pos_change(52, 130)
t.color("navy")
t.begin_fill()
t.circle(45)
t.end_fill()

# Big White Circle

pos_change(47, 130)
t.color("white")
t.begin_fill()
t.circle(39.7)
t.end_fill()

# Mini Blue Circles
t.speed("fastest")
pos_change(-30.5, 125)
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.right(15)
    t.pendown()

# Small Blue Circle
t.speed("slow")
pos_change(27, 130)
t.begin_fill()
t.circle(20)
t.end_fill()

# Spokes
pos_change(10, 129)
t.pensize(2)
for i in range(24):
    t.forward(43)
    t.backward(42)
    t.left(15)

# Hold the output window
turtle.done()
