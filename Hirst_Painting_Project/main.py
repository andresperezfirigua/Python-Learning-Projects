'''
    Below colorgram package code to extract color from painting, commented out code after completing that task
'''
# import colorgram
# Extract colors from an image.
# colors = colorgram.extract('painting.jpg', 50)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(len(colors))
# print(colors)
#
# print(len(rgb_colors))
# print(rgb_colors)

'''
    Actual project from here
'''
from turtle import Turtle, Screen
import random

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

tommy = Turtle()
screen = Screen()
tommy.shape("classic")
tommy.speed(0)
tommy.color("sea green")
tommy.penup()
screen_size = screen.screensize()
tommy.setposition(-(screen_size[0] - 50), -(screen_size[1]))
init_position = (tommy.pos()[0], tommy.pos()[1])
current_position = init_position
screen.colormode(255)


def generate_dot_color():
    return random.choice(color_list)


def draw_dot_line():
    color = generate_dot_color()
    tommy.dot(20, color)
    tommy.forward(50)
    return tommy.pos()


def start_new_line(current_position):
    tommy.setposition(init_position[0], current_position[1] + 50)
    return tommy.pos()


while current_position[1] <= screen_size[1]:
    while current_position[0] < screen_size[0]:
        current_position = draw_dot_line()
    current_position = start_new_line(current_position)

screen.exitonclick()
