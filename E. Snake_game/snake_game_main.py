from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Play The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_segments()
        scoreboard.increase_score()

    # Detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        is_game_on = False
        # scoreboard.reset_score()
        # scoreboard.game_over()
        scoreboard.reset_score()
        snake.reset()

    # Detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            # scoreboard.reset_score()
            # scoreboard.game_over()
            scoreboard.reset_score()

            snake.reset()

screen.exitonclick()
