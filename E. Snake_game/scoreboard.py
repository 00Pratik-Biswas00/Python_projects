from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align="center", font=("Courier", 15, "normal"))

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over. Your final score is: {self.score}\n\t  High Score: {self.high_score}", align="center",
                   font=("Courier", 18, "normal"))
        self.score = 0
        # self.update_scoreboard()

    # def game_over(self):
    #     # self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over. Your final score is: {self.score}\n\t  High Score: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
