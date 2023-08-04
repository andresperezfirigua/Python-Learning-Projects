import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball


game_is_on = True

table = Screen()
table.bgcolor("black")
table.setup(width=800, height=600)
table.title("Pong Game")
table.tracer(0)

scoreboard = Scoreboard()
paddle_1 = Paddle((-350, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()


table.listen()
table.onkey(fun=paddle_1.move_up, key="w")
table.onkey(fun=paddle_1.move_down, key="s")

table.onkey(fun=paddle_2.move_up, key="Up")
table.onkey(fun=paddle_2.move_down, key="Down")

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    table.update()

    # Detect collision with walls
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() < -320 or ball.distance(paddle_2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect ball out of bounds
    if ball.xcor() > 380:
        scoreboard.increase_player_1_score()
        ball.reset_position()

    elif ball.xcor() < -380:
        scoreboard.increase_player_2_score()
        ball.reset_position()

table.exitonclick()
