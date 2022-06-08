# used libraries
from turtle import Turtle
import random

# constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# game difficulty levels
DIFFICULTY = {"Kid Turtle": 1,
              "Teen Turtle": 2,
              "Usain Turtle Bolt": 3,
              "Mutant Ninja Turtle": 4,
              "Turtle Avenger": 5,
              "Celestial Turtle": 6
              }


class CarManager:
    """Models the car manager that creates and moves cars"""
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Creates cars in the game window and the amount created of cars is determined by the chosen difficulty"""
        random_chance = random.randint(1, 6)
        if 0 < random_chance <= DIFFICULTY["Celestial Turtle"]:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randrange(-250, 250, 25)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves cars across the game window from the right to the left by the predefined value"""
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        """Increses speed of cars by the predefined value"""
        self.car_speed += MOVE_INCREMENT
