import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
loop_counter = 1
while game_is_on:
    # Create new car
    if loop_counter % 6 == 0:
        car_manager.create_car()
    loop_counter += 1

    time.sleep(0.1)
    screen.update()

    # Detect level pass
    if player.passed_level():
        scoreboard.level_up()
        player.reset_position()
        car_manager.increase_speed()

    # Detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    car_manager.move_cars()

screen.exitonclick()
