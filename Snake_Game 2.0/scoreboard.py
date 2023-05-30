from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_count = 0
        self.high_score = 0
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
            self.high_score = self.score_count
        self.score_count = 0
        self.update_scoreboard()

    # No need for game over method anymore
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", False, align=ALIGNMENT, font=FONT)
