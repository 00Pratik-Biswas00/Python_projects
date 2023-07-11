from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.setup(height=500, width=500)  # Setting the screen size
screen.textinput(title="Sketch App",
                 prompt="Write 'Go' to continue! \n\nBasic rules: \nw -> Move forward \ns -> Move backward \nl -> Turn left \nr -> Turn right \nu -> Pen up \nd -> Pen down\nc -> Clear the screen")


def pen_up():
    t.penup()


def pen_down():
    t.pendown()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def turn_left():
    t.left(10)


def turn_right():
    t.right(10)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "r")
screen.onkey(turn_left, "l")
screen.onkey(clear_screen, "c")
screen.exitonclick()
