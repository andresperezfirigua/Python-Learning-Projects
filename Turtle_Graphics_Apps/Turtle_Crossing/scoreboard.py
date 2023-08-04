from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(-220, 265)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", False, align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", False, align="center", font=FONT)
