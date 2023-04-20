from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_backwards():
    tom.back(10)


def rotate_counter_clockwise():
    tom.left(10)


def rotate_clockwise():
    tom.right(10)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()

# Higher order functions applied knowledge, one function being used by another function as its parameter
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()