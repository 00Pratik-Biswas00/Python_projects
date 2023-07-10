import random
import turtle as t

play_turtle = t.Turtle()
t.colormode(255)
play_turtle.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


play_turtle.speed("fastest")


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        play_turtle.color(random_color())
        play_turtle.circle(100)
        current_head = play_turtle.heading()
        play_turtle.setheading(current_head + gap_size)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
