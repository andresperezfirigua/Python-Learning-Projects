from turtle import Turtle, Screen
import random

snake = Turtle()
snake.hideturtle()
snake.penup()
snake.shape("square")
snake.speed(1)
is_game_on = True
screen = Screen()


def turn_right():
    snake.right(90)


def turn_left():
    snake.left(90)


def draw_snake(parts):
    # Below range sets the snake size after eating
    for i in range(parts):
        # Stamp creates the body of the snake
        snake.stamp()
        snake.fd(20)


def move_snake():
    screen.listen()
    screen.onkey(fun=turn_right, key="d")
    screen.onkey(fun=turn_left, key="a")
    snake.clearstamps(1)
    snake.stamp()
    snake.fd(20)


draw_snake(3)

for _ in range(100):
    move_snake()


screen.exitonclick()
