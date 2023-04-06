# Normal way to import modules
from turtle import Turtle, Screen

# Testing Turtle class methods, drawing a square
# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("sea green")
# for i in range(4):
#     tommy.forward(100)
#     tommy.left(90)
# screen = Screen()
# screen.exitonclick()



# Importing modules and give them aliases for reference
# from turtle import Turtle as t
# import turtle as tr
# tom = t()



# Drawing a square with dashed line
# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("sea green")
# for _ in range(4):
#     for _ in range(10):
#         tommy.forward(10)
#         if tommy.isdown():
#             tommy.penup()
#         else:
#             tommy.pendown()
#     tommy.left(90)
# screen = Screen()
# screen.exitonclick()



# Drawing multiple shapes
# import random
# tommy = Turtle()
# tommy.shape("classic")
# colors = ["dark green", "cyan", "blue", "dark blue", "red", "medium slate blue", "dim gray"]
#
# sides = 3
# while sides <= 10:
#     for i in range(sides):
#         tommy.color(random.choice(colors))
#         tommy.forward(100)
#         tommy.left(360 - (360 / sides))
#     sides += 1
# screen = Screen()
# screen.exitonclick()



# Generating random walk with random colouring
# import random as r
#
# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
# tim.shape("classic")
# tim.pensize(13)
# tim.speed(7)
# angles = [0, 90, 180, 270]
# for _ in range(200):
#     tim.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
#     tim.setheading(r.choice(angles))
#     tim.forward(20)
# screen.exitonclick()



# Drawing a Spirograph with random colors
# import random as r
#
# tim = Turtle()
# screen = Screen()
# screen.colormode(255)
# tim.shape("classic")
# tim.speed(0)
# for i in range(0, 360, 5):
#     tim.pencolor(r.randint(1, 255), r.randint(1, 255), r.randint(1, 255))
#     tim.setheading(i)
#     tim.circle(100)
#
# screen.exitonclick()