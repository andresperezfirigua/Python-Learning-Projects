from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score_count()
        food.set_food_location()
        snake.extend()

    # Detect collision with wall
    if (snake.head.xcor() < -290 or snake.head.xcor() > 290) or (snake.head.ycor() < -290 or snake.head.ycor() > 290):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
