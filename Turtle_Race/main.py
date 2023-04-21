from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
game_is_on = False
y_position = -100


def create_turtle(y_pos, color):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-280, y=y_pos)
    return turtle


for color_index in range(len(colors)):
    new_turtle = create_turtle(y_position, colors[color_index])
    turtles.append(new_turtle)
    y_position += 40

if user_bet:
    game_is_on = True

while game_is_on:
    for turtle in turtles:
        step_length = random.randint(0, 10)
        turtle_color = turtle.fillcolor()
        turtle.forward(step_length)
        if turtle.xcor() > 280:
            game_is_on = False
            print(f"Turtle {turtle_color} is the winner")
            if turtle_color == user_bet:
                print("You win the bet!")
            else:
                print("You lose.")

screen.exitonclick()
