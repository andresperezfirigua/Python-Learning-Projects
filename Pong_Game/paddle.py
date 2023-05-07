from turtle import Turtle

SIZE = 40

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.color("white")
        self.settiltangle(0)
        self.seth(90)
        self.penup()
        self.goto(position)

    def move(self):
        pass