# TODO: Set up game board and components
# Board appearance, board line
# TODO: Get ball moving
# TODO: Detect collision with paddles
# TODO: Create scoreboard

from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
import time

game_is_on = True

table = Screen()
table.bgcolor("black")
table.setup(width=600, height=600)
table.title("Pong Game")
table.tracer(0)
table.listen()

scoreboard = Scoreboard()
paddle_1 = Paddle((-290, 0))
paddle_2 = Paddle((280, 0))

paddle_1.forward(100)
paddle_2.back(200)
table.update()

table.exitonclick()
