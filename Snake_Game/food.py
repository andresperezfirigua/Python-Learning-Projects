from turtle import Turtle
import random

SCREEN_DIMENSIONS = [-280, 280]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.set_food_location()

    def set_food_location(self):
        random_x = random.randint(SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1])
        random_y = random.randint(SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1])
        self.goto(random_x, random_y)