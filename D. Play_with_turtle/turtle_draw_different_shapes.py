import random
import turtle as t

turtle = t.Turtle()
turtle.shape("arrow")
turtle.penup()
turtle.goto(-50, 200)
turtle.pendown()
color_name = ["cyan", "spring green", "tomato", "saddle brown", "dark violet"]


def draw_shapes(slide_number):
    angle = 360 / slide_number
    for i in range(slide_number):
        turtle.forward(100)
        turtle.right(angle)


for number_of_side in range(3, 13):
    turtle.color(random.choice(color_name))
    draw_shapes(number_of_side)

screen = t.Screen()
screen.exitonclick()
