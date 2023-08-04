from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_color = random.choice(COLORS)
        y_pos = random.randint(-250, 250)
        car = Car(car_color, (300, y_pos))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move(self.move_distance)
            if car.xcor() < -300:
                self.delete_car(car)

    def delete_car(self, car):
        car.clear()
        car.hideturtle()
        self.cars.remove(car)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
