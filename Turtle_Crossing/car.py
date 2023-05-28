from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.shape("square")
        self.seth(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.penup()
        self.goto(position)

    def move(self, move_distance):
        self.forward(move_distance)
