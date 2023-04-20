from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -100

def create_turtle(y_pos, color):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-280, y=y_pos)
    return turtle


for turtle_index in range(len(colors)):
    tim = create_turtle(y_position, colors[turtle_index])
    y_position += 40

screen.exitonclick()