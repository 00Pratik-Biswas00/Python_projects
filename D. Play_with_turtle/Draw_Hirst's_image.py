import turtle as t
import random

my_colour = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129),
             (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46),
             (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42),
             (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85),
             (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]	# Color database

t.colormode(255)
play_turtle = t.Turtle()

play_turtle.penup()
play_turtle.hideturtle()
play_turtle.goto(-600,-200)
play_turtle.forward(400)
play_turtle.setheading(0)

dot_number = 100
play_turtle.speed("fastest")

for dot_count in range(1, dot_number+1): 
    play_turtle.dot(15, random.choice(my_colour))
    play_turtle.penup()
    play_turtle.forward(50)
    if dot_count % 10 == 0:
        play_turtle.left(90)
        play_turtle.forward(50)
        play_turtle.left(90)
        play_turtle.forward(500)
        play_turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()




