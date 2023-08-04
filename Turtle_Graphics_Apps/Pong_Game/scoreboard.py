from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"{self.score_player1}       {self.score_player2}", False, align=ALIGNMENT, font=FONT)
        self.draw_net()

    def draw_net(self):
        self.goto(0, 295)
        self.pendown()
        self.pensize(5)
        self.seth(270)
        for _ in range(30):
            self.forward(20)
            if self.isdown():
                self.penup()
            else:
                self.pendown()
        self.penup()

    def increase_player_1_score(self):
        self.score_player1 += 1
        self.update_scoreboard()

    def increase_player_2_score(self):
        self.score_player2 += 1
        self.update_scoreboard()
