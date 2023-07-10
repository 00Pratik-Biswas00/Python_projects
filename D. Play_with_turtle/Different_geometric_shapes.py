import random
import turtle as t

turtle = t.Turtle()
turtle.shape("arrow")
turtle.penup()    # Change the position
turtle.goto(-50, 200)
turtle.pendown()
color_name = ["cyan", "spring green", "tomato", "saddle brown", "dark violet"]


def draw_shapes(side_number):
    angle = 360 / side_number
    for i in range(side_number):
        turtle.forward(100)
        turtle.right(angle)


for number_of_side in range(3, 13):		# Different side number give different shapes
    turtle.color(random.choice(color_name))
    draw_shapes(number_of_side)

screen = t.Screen()
screen.exitonclick()
