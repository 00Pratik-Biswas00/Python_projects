from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=500, width=500)
user_choice = screen.textinput(title="Welcome to the Turtle race game!",
                               prompt="Choose your turtle's colour: red, orange, blue, purple, green, yellow")
colours = ["red", "orange", "blue", "purple", "green", "yellow"]
y_positions = [-70, -40, -10, 20, 50, 80]

continue_race = False
total_turtles = []
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colours[turtle_index])
    t.goto(x=-230, y=y_positions[turtle_index])
    total_turtles.append(t)

if user_choice:
    continue_race = True

while continue_race:

    for turtle in total_turtles:
        if turtle.xcor() >= 220:
            continue_race = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_choice:
                print(f"You've won the race! The {winning_colour} turtle is the winner!")

            else:
                print(f"You've lost the race! The {winning_colour} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()





