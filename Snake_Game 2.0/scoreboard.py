from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.score_count = 0
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_count}  |   Highest score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score_count(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_count > self.high_score:
            with open('data.txt', mode="w") as file:
                file.write(f"{self.score_count}")
            self.high_score = self.score_count
        self.score_count = 0
        self.update_scoreboard()
